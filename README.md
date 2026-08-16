# Skills

Reusable Codex skills by Nick Schmidt.

## Available skills

| Skill | What it does |
| --- | --- |
| [`ns-plan`](skills/ns-plan/) | Creates grounded, decision-complete plans for multi-step software, product, and operational work. |
| [`ns-work`](skills/ns-work/) | Implements and locally verifies an approved plan or decision-complete change. |
| [`ns-code-review`](skills/ns-code-review/) | Reviews changes for introduced defects and regression risk without modifying them. |
| [`ns-simplify`](skills/ns-simplify/) | Simplifies settled, recently changed code while preserving observable behavior. |

## Install

### Codex and other coding agents

```bash
npx skills@latest add nickschmidt94/skills
```

Choose the skills you want and the coding agents where they should be installed.

### Install all skills globally in Codex

```bash
npx skills@latest add nickschmidt94/skills --skill '*' -g -a codex
```

Global installation makes the skill available across all your Codex projects.

### Update installed skills

```bash
npx skills update
```

## License

MIT
