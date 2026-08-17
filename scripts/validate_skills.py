"""Validate the structure and catalog of this skills collection."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
README_SKILL_LINK_PATTERN = re.compile(r"\(skills/([a-z0-9-]+)/SKILL\.md\)")
NS_REFERENCE_PATTERN = re.compile(r"\$((?:ns)-[a-z0-9-]+)")
REQUIRED_INTERFACE_FIELDS = ("display_name", "short_description", "default_prompt")


def load_yaml(path: Path, content: str, errors: list[str]) -> object | None:
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError as error:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {error}")
        return None


def validate_skill(skill_dir: Path, skill_names: set[str], errors: list[str]) -> None:
    relative_dir = skill_dir.relative_to(ROOT)
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{relative_dir}: missing SKILL.md")
        return

    content = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(content)
    if match is None:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter at the top of the file"
        )
    else:
        frontmatter = load_yaml(skill_file, match.group(1), errors)
        if isinstance(frontmatter, dict):
            unsupported = sorted(set(frontmatter) - {"name", "description"})
            if unsupported:
                errors.append(
                    f"{skill_file.relative_to(ROOT)}: unsupported frontmatter fields: {', '.join(unsupported)}"
                )

            name = frontmatter.get("name")
            description = frontmatter.get("description")
            if not isinstance(name, str) or not name:
                errors.append(
                    f"{skill_file.relative_to(ROOT)}: name must be a non-empty string"
                )
            else:
                if len(name) > 64 or NAME_PATTERN.fullmatch(name) is None:
                    errors.append(
                        f"{skill_file.relative_to(ROOT)}: name must be at most 64 lowercase letters, digits, or hyphens"
                    )
                if name != skill_dir.name:
                    errors.append(
                        f"{skill_file.relative_to(ROOT)}: frontmatter name {name!r} does not match directory {skill_dir.name!r}"
                    )
            if not isinstance(description, str) or not description.strip():
                errors.append(
                    f"{skill_file.relative_to(ROOT)}: description must be a non-empty string"
                )
        elif frontmatter is not None:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: frontmatter must be a mapping"
            )

    validate_agent_metadata(skill_dir, errors)
    validate_local_links(skill_file, content, errors)

    for reference in sorted(set(NS_REFERENCE_PATTERN.findall(content))):
        if reference not in skill_names:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: references missing sibling skill ${reference}"
            )


def validate_agent_metadata(skill_dir: Path, errors: list[str]) -> None:
    metadata_file = skill_dir / "agents" / "openai.yaml"
    if not metadata_file.is_file():
        errors.append(f"{metadata_file.relative_to(ROOT)}: missing Codex metadata")
        return

    metadata = load_yaml(
        metadata_file,
        metadata_file.read_text(encoding="utf-8"),
        errors,
    )
    if not isinstance(metadata, dict):
        if metadata is not None:
            errors.append(
                f"{metadata_file.relative_to(ROOT)}: metadata must be a mapping"
            )
        return

    interface = metadata.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"{metadata_file.relative_to(ROOT)}: interface must be a mapping")
        return

    for field in REQUIRED_INTERFACE_FIELDS:
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(
                f"{metadata_file.relative_to(ROOT)}: interface.{field} must be a non-empty string"
            )

    short_description = interface.get("short_description")
    if isinstance(short_description, str) and not 25 <= len(short_description) <= 64:
        errors.append(
            f"{metadata_file.relative_to(ROOT)}: interface.short_description must be 25-64 characters"
        )

    default_prompt = interface.get("default_prompt")
    expected_reference = f"${skill_dir.name}"
    if isinstance(default_prompt, str) and expected_reference not in default_prompt:
        errors.append(
            f"{metadata_file.relative_to(ROOT)}: interface.default_prompt must mention {expected_reference}"
        )

    policy = metadata.get("policy")
    if policy is not None:
        if not isinstance(policy, dict):
            errors.append(
                f"{metadata_file.relative_to(ROOT)}: policy must be a mapping"
            )
        elif "allow_implicit_invocation" in policy and not isinstance(
            policy["allow_implicit_invocation"], bool
        ):
            errors.append(
                f"{metadata_file.relative_to(ROOT)}: policy.allow_implicit_invocation must be a boolean"
            )


def validate_local_links(source: Path, content: str, errors: list[str]) -> None:
    for raw_target in MARKDOWN_LINK_PATTERN.findall(content):
        target = raw_target.strip().split(maxsplit=1)[0]
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if not path_part:
            continue
        resolved = (source.parent / path_part).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(
                f"{source.relative_to(ROOT)}: local link escapes the repository: {target}"
            )
            continue
        if not resolved.exists():
            errors.append(f"{source.relative_to(ROOT)}: broken local link: {target}")


def validate_readme(skill_names: set[str], errors: list[str]) -> None:
    if not README.is_file():
        errors.append("README.md: missing repository catalog")
        return

    content = README.read_text(encoding="utf-8")
    linked_names = README_SKILL_LINK_PATTERN.findall(content)
    for name in sorted(skill_names):
        count = linked_names.count(name)
        if count != 1:
            errors.append(
                f"README.md: expected one direct SKILL.md link for {name}, found {count}"
            )
    for name in sorted(set(linked_names) - skill_names):
        errors.append(f"README.md: catalog links unknown skill {name}")
    validate_local_links(README, content, errors)


def main() -> int:
    errors: list[str] = []
    if not SKILLS_DIR.is_dir():
        print("skills: missing skills directory", file=sys.stderr)
        return 1

    skill_dirs = sorted(
        path
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    skill_names = {path.name for path in skill_dirs}
    if not skill_dirs:
        errors.append("skills: no skill directories found")

    for skill_dir in skill_dirs:
        validate_skill(skill_dir, skill_names, errors)
    validate_readme(skill_names, errors)

    if errors:
        print(f"Skill validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
