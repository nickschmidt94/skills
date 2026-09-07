#!/usr/bin/env python3
"""Bump a local skill version and record one concise changelog entry.

Supports flat, two-space metadata with a plain or quoted version and no
inline version comment. Unsupported formatting fails before either file is written.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
FRONTMATTER = re.compile(r"\A---\n(?P<body>.*?)\n---(?P<rest>\n.*)\Z", re.DOTALL)


def next_version(current: str | None, bump: str) -> str:
    if current is None:
        return "1.0.0"
    match = SEMVER.fullmatch(current)
    if not match:
        raise ValueError(f"metadata.version must be semantic x.y.z, got {current!r}")
    major, minor, patch = (int(part) for part in match.groups())
    if bump == "major":
        return f"{major + 1}.0.0"
    if bump == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def render_frontmatter(skill_md: Path, bump: str) -> tuple[str, str]:
    content = skill_md.read_text()
    match = FRONTMATTER.fullmatch(content)
    if not match:
        raise ValueError(f"{skill_md} has invalid YAML frontmatter")

    body = match.group("body")
    metadata_line = re.search(r"(?m)^metadata:(?P<value>[^\n]*)$", body)
    if metadata_line and metadata_line.group("value").strip():
        raise ValueError("metadata must use a block mapping before versioning")
    metadata = metadata_line
    current = None

    if metadata:
        block_start = metadata.end()
        next_top_level = re.search(r"(?m)^\S[^\n]*$", body[block_start:])
        block_end = block_start + next_top_level.start() if next_top_level else len(body)
        block = body[block_start:block_end]
        # This dependency-free editor supports only flat, two-space metadata.
        # Reject other YAML shapes instead of treating an unreadable version as absent.
        for line in block.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if not re.fullmatch(r"  [A-Za-z_][A-Za-z0-9_-]*:[^\n]*", line):
                raise ValueError("metadata must be a flat mapping with two-space indentation")
        version_keys = re.findall(r"(?m)^  version:", block)
        if len(version_keys) > 1:
            raise ValueError("metadata contains duplicate version keys")
        version_match = re.search(
            r'(?m)^  version:\s*["\']?([^"\'\s]+)["\']?\s*$', block
        )
        if version_match:
            current = version_match.group(1)
            version = next_version(current, bump)
            new_block = (
                block[: version_match.start()]
                + f'  version: "{version}"'
                + block[version_match.end() :]
            )
        else:
            if version_keys:
                raise ValueError("metadata.version must be a plain or quoted x.y.z value without an inline comment")
            version = next_version(None, bump)
            new_block = f'\n  version: "{version}"' + block
        body = body[:block_start] + new_block + body[block_end:]
    else:
        version = next_version(None, bump)
        body += f'\nmetadata:\n  version: "{version}"'

    return version, f"---\n{body}\n---{match.group('rest')}"


def render_changelog(path: Path, version: str, date: str, summary: str) -> str:
    entry = f"## {version} - {date}\n\n- {summary}\n"
    if not path.exists():
        return f"# Changelog\n\n{entry}"

    content = path.read_text()
    if re.search(rf"(?m)^## {re.escape(version)}(?:\s|$)", content):
        raise ValueError(f"{path} already contains version {version}")
    heading = re.match(r"\A# Changelog\s*\n", content)
    if not heading:
        raise ValueError(f"{path} must begin with '# Changelog'")
    remainder = content[heading.end() :].lstrip("\n")
    return f"# Changelog\n\n{entry}\n{remainder}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_directory", type=Path)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--bump", choices=("patch", "minor", "major"), default="patch")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    args = parser.parse_args()

    skill_directory = args.skill_directory.resolve()
    skill_md = skill_directory / "SKILL.md"
    if not skill_md.is_file():
        raise SystemExit(f"SKILL.md not found in {skill_directory}")

    summary = " ".join(args.summary.split()).strip().rstrip(".")
    if not summary:
        raise SystemExit("--summary must contain visible text")

    changelog = skill_directory / "CHANGELOG.md"
    version, skill_content = render_frontmatter(skill_md, args.bump)
    changelog_content = render_changelog(
        changelog, version, args.date, f"{summary}."
    )
    skill_md.write_text(skill_content)
    changelog.write_text(changelog_content)
    print(version)


if __name__ == "__main__":
    main()
