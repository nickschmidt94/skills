# Skills

Reusable Codex skills by Nick Schmidt.

The collection separates planning, plan review, local implementation, simplification, closed-loop code review, publication, and durable learning into bounded workflows. Each skill grants only the authority described in its instructions.

See [what's new](CHANGELOG.md) for meaningful skill additions and behavior changes.

## Engineering workflow

The main delivery path is:

`ns-plan → ns-plan-review → ns-work → ns-simplify → ns-code-review → ns-ship-pr`

- [`ns-finish-line`](skills/ns-finish-line/SKILL.md) is an explicit-only workflow for carrying supported decisions to ready artifacts or verified repository work to an open pull request; it stops before merge and deployment.
- [`ns-plan`](skills/ns-plan/SKILL.md) creates grounded, decision-complete plans that make ownership, context, commit boundaries, and verification legible before implementation.
- [`ns-plan-review`](skills/ns-plan-review/SKILL.md) proportionally hardens completed plans with direct Builder review for ordinary work and independent Red-team review for exposed high-risk boundaries.
- [`ns-work`](skills/ns-work/SKILL.md) implements approved work with bounded sub-agent delegation when useful, caller-visible proof, and explicit local verification status.
- [`ns-simplify`](skills/ns-simplify/SKILL.md) cleans up settled implementation before code review, reducing complexity while preserving behavior and unrelated work.
- [`ns-code-review`](skills/ns-code-review/SKILL.md) reviews correctness, repository standards, and accepted requirements as separate axes, repairs proven local findings, and freshly re-reviews until clean or blocked, using independent reviewers when available.
- [`ns-ship-pr`](skills/ns-ship-pr/SKILL.md) publishes an authorized, verified change as one pull request.

Compounding is a supporting path rather than a mandatory delivery step:

- [`ns-compound`](skills/ns-compound/SKILL.md) judges whether completed work produced one learning worth preserving, then captures it in the repository or improves the skill that shaped the run.
- [`ns-compound-sync`](skills/ns-compound-sync/SKILL.md) keeps accumulated repository learnings accurate as the codebase changes.
- [`skill-retrospective`](skills/skill-retrospective/SKILL.md) improves one skill when a completed run exposes a durable, evidence-backed lesson.

## Domain audits

- [`llm-visibility-audit`](skills/llm-visibility-audit/SKILL.md) audits why websites are absent from AI-generated results and prioritizes evidence-backed improvements.

## Invocation

`ns-compound`, `ns-compound-sync`, and `ns-finish-line` are explicit-only skills. The other skills may be selected automatically when their descriptions match the request. Invocation never expands the user's authority: implementation, publication, deployment, and other consequential actions still require the authorization stated by the selected skill.

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
