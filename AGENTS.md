# Skills Repository

This repository publishes independently installable agent skills. Keep the collection small, portable, and internally consistent.

## Structure

- Place each public skill at `skills/<skill-name>/SKILL.md`.
- Match the directory name to the `name` in `SKILL.md` frontmatter.
- Use lowercase letters, digits, and hyphens for skill names.
- Give every skill an `agents/openai.yaml` with `interface.display_name`, `interface.short_description`, and `interface.default_prompt`.
- Keep detailed evidence, schemas, examples, and other conditional material in the owning skill's `references/`, `scripts/`, `assets/`, or `evals/` directories only when they add reusable value.

## Catalog and invocation

- List every public skill exactly once in the top-level `README.md` and link its name directly to `skills/<skill-name>/SKILL.md`.
- Keep the README's invocation description synchronized with `policy.allow_implicit_invocation` in `agents/openai.yaml`.
- Treat cross-skill `$ns-*` references as optional routing suggestions because users may install skills individually. If the companion is unavailable, explain the equivalent next step in plain language.
- Never let skill invocation broaden the authority granted by the user or the selected skill.

## Changes

- Preserve unrelated user changes and follow the nearest applicable repository instructions.
- When renaming a skill, update its directory, frontmatter, agent metadata, README entry, cross-skill references, evals, and installed-source documentation together.
- Keep `SKILL.md` focused on operative instructions. Do not add auxiliary setup guides or duplicate detailed reference material in the skill body.
- Install `requirements-dev.txt`, then run `python3 scripts/validate_skills.py` before considering a repository change complete.
- For behavior changes, also exercise relevant evals or representative prompts. Structural validation alone does not prove skill behavior.
