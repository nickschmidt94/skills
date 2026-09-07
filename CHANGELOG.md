# What's New

Meaningful additions and behavior changes for people who install these skills are recorded here. Typo-only, formatting-only, and maintainer-only changes are omitted.

## 2026-09-07

### Changed

- [`ns-simplify`](skills/ns-simplify/SKILL.md) 1.0.1 focuses cleanup on the selected implementation and matches regression checks to the cleanup’s risk. It permits simplifying in-scope work while protecting unrelated edits, and hands off to complete-diff review unless that review was already requested.

- [`ns-work`](skills/ns-work/SKILL.md) now allows bounded sub-agent delegation and independent tasks to proceed concurrently, while the primary agent verifies their combined result. Routine implementation choices no longer require a question, and unavailable checks pause dependent work while independent work continues; delivery distinguishes verified outcomes from incomplete evidence. Shipping still requires separate authorization.

## 2026-08-30

### Changed

- [`ns-plan`](skills/ns-plan/SKILL.md) and [`ns-plan-review`](skills/ns-plan-review/SKILL.md) now make ownership, context placement, commit boundaries, and real proof explicit, reserve independent Red-team review for plans with exposed high-risk boundaries, and surface reusable planner rules when a proven gap should be prevented upstream.
- [`ns-work`](skills/ns-work/SKILL.md) now uses caller-visible seams, independent test oracles, comment integrity, and explicit simplification handoffs to keep implementation focused on observable behavior.
- [`ns-simplify`](skills/ns-simplify/SKILL.md) now tests concrete ownership, locality, interface, and test-surface costs before changing a verified implementation.
- [`ns-code-review`](skills/ns-code-review/SKILL.md) now reports correctness, repository standards, and accepted requirements separately, always preserves separate axis passes, and uses independent reviewers when available before a clean verdict.
- [`ns-finish-line`](skills/ns-finish-line/SKILL.md) is now explicit-only and requires a direct simplification check before repository work advances to review and publication.

## 2026-08-22

### Added

- [`ns-finish-line`](skills/ns-finish-line/SKILL.md) selects supported recommendations and continues through decision work or repository delivery without repetitive approval rounds. Use it to reach ready planning artifacts or an open pull request while keeping autonomous choices explicit and stopping before merge or deployment.

## 2026-08-21

### Added

- [`ns-plan-review`](skills/ns-plan-review/SKILL.md) independently red-teams completed plans, directly applies proven implementation-readiness fixes without pausing between safe amendments, and re-reviews the revised whole plan before implementation.

### Changed

- [`ns-compound`](skills/ns-compound/SKILL.md) now treats `writing-for-agents` as an optional quality companion and applies its own Lean and validation standards when that skill is not installed.
- [`ns-code-review`](skills/ns-code-review/SKILL.md) now repairs proven, decision-complete local findings and independently re-reviews the complete change until clean or blocked. Explicit report-only requests preserve its former read-only behavior.

## 2026-08-20

### Added

- [`skill-retrospective`](skills/skill-retrospective/SKILL.md) turns evidence from a completed skill run into one justified skill improvement, while treating `no change` as a valid result.

### Changed

- [`ns-compound`](skills/ns-compound/SKILL.md) now decides whether a learning is worth preserving before creating anything. Its Value gate requires evidence, recurrence, a specific future behavior change, a real retrieval gap, and expected value greater than maintenance cost.
- [`ns-compound`](skills/ns-compound/SKILL.md) can now route a qualified learning to either repository guidance or the reusable skill that shaped the run. Repository-only instructions load through a branch-specific reference.
- Cross-skill routes now include plain-language fallbacks so individually installed skills remain usable without their suggested companions.
