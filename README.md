# Skills

Reusable Codex skills by Nick Schmidt.

## Available skills

| Skill | What it does |
| --- | --- |
| [`ns-plan`](skills/ns-plan/) | Creates grounded, decision-complete plans for multi-step software, product, and operational work. |
| [`ns-work`](skills/ns-work/) | Implements and locally verifies an approved plan or decision-complete change. |
| [`ns-code-review`](skills/ns-code-review/) | Reviews changes for introduced defects and regression risk without modifying them. |
| [`ns-simplify`](skills/ns-simplify/) | Simplifies settled, recently changed code while preserving observable behavior. |
| [`ns-ship-pr`](skills/ns-ship-pr/) | Commits owned changes, pushes a feature branch, and creates or refreshes one verified pull request. |
| [`ns-compound`](skills/ns-compound/) | Captures one durable repository learning from solved or proven work. |
| [`ns-compound-refresh`](skills/ns-compound-refresh/) | Audits and refreshes repository learnings as the codebase evolves. |
| [`llm-visibility-audit`](skills/llm-visibility-audit/) | Audits why websites are absent from AI-generated search results and prioritizes evidence-backed improvements. |

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
