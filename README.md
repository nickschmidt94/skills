# Skills

Reusable Codex skills by Nick Schmidt.

The collection separates planning, local implementation, simplification, closed-loop review, publication, and durable learning into bounded workflows. Each skill grants only the authority described in its instructions.

See the [changelog](CHANGELOG.md) for meaningful skill improvements and additions.

## Engineering workflow

The main delivery path is:

`ns-plan → ns-work → ns-simplify → ns-code-review → ns-ship-pr`

- [`ns-plan`](skills/ns-plan/SKILL.md) creates grounded, decision-complete plans and stops before implementation.
- [`ns-work`](skills/ns-work/SKILL.md) implements approved work and leaves a locally verified working tree.
- [`ns-simplify`](skills/ns-simplify/SKILL.md) reduces structural cost without changing observable behavior.
- [`ns-code-review`](skills/ns-code-review/SKILL.md) reviews introduced defects and regression risk, repairs proven local findings, and independently re-reviews until clean or blocked. An explicit report-only mode preserves read-only review when requested.
- [`ns-ship-pr`](skills/ns-ship-pr/SKILL.md) publishes an authorized, verified change as one pull request.

Compounding is a supporting path rather than a mandatory delivery step:

- [`ns-compound`](skills/ns-compound/SKILL.md) judges whether completed work produced one learning worth preserving, then captures it in the repository or improves the skill that shaped the run.
- [`ns-compound-sync`](skills/ns-compound-sync/SKILL.md) keeps accumulated repository learnings accurate as the codebase changes.
- [`skill-retrospective`](skills/skill-retrospective/SKILL.md) improves one skill when a completed run exposes a durable, evidence-backed lesson.

## Product decisions

- [`mvp-it`](skills/mvp-it/SKILL.md) reduces an idea or existing product to its smallest evidence-backed sellable form, with separate modes for shipping, reviewing, brainstorming, and deciding whether to keep, pivot, retire, or sell.

## Domain audits

- [`llm-visibility-audit`](skills/llm-visibility-audit/SKILL.md) audits why websites are absent from AI-generated results and prioritizes evidence-backed improvements.

## Invocation

`ns-compound` and `ns-compound-sync` are explicit-only skills. The other skills may be selected automatically when their descriptions match the request. Invocation never expands the user's authority: implementation, publication, deployment, and other consequential actions still require the authorization stated by the selected skill.

Skills can be installed individually. References to sibling skills are optional routing suggestions, not hard dependencies. When a suggested companion is unavailable, describe the equivalent next step in plain language instead of blocking the current workflow.

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
