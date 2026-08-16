---
name: ns-plan
description: Create or revise a grounded, decision-complete plan for multi-step software, product, or operational work. Use when consequential choices must be resolved into an implementation-ready plan and the current phase should stop before execution.
---

# NS Plan

Produce a plan an implementer can execute without redesigning the solution.

Use three standards throughout:

- **Grounded** — each load-bearing claim comes from current evidence, a settled user decision, or a visible assumption.
- **Decision-complete** — resolve choices that would otherwise force the implementer to redesign the work.
- **Observable** — express completion as behavior or state someone can verify.

This skill authorizes read-only research and creation or revision of the plan artifact. Stop after delivering the reviewed plan. Implementation, commits, pushes, deployments, publication, and external messages require a separate user request.

## 1. Frame

Identify the target workspace, requested outcome, meaningful scope boundary, non-goals, and success signal. Treat a named file, document, URL, tool, or prior plan as an input to inspect rather than a hint to replace.

When revising an existing plan, update that artifact unless the user requests a new version. Preserve stable identifiers that downstream work may reference.

Ask one focused question only when its answer could materially change product behavior, scope, architecture, sequencing, risk, or an irreversible action. Otherwise make the smallest reasonable inference and mark it as an assumption.

**Complete when:** the problem, intended outcome, consequential boundaries, and observable success signal are stated or the unresolved item is identified as a blocker.

## 2. Ground

Inspect the smallest current source set that can support the plan:

- applicable repository instructions and named sources;
- current implementation, tests, configuration, and documentation around the affected surface;
- repository status and existing user changes when they constrain sequencing;
- history or external primary documentation only when a decision depends on it.

Prefer the environment over cached prose for discoverable facts such as scripts, versions, paths, and configuration. Honor decisions already settled in the conversation; reopen one only when current evidence shows it cannot work.

Use evidence labels only where provenance affects judgment:

- **Verified:** confirmed from the current source of truth.
- **Settled:** decided by the user or an authoritative product source.
- **Assumed:** necessary to proceed but not yet confirmed.

**Complete when:** every major recommendation is supported by current evidence, a settled decision, or an explicit assumption, and relevant existing patterns and constraints are known.

## 3. Decide

Separate product choices from implementation choices. Preserve requested behavior and decide the technical approach, boundaries, sequencing, and verification strategy.

Record rationale where a credible alternative would lead to materially different work. Keep useful adjacent improvements outside active scope under follow-up work.

Defer details that genuinely depend on execution, such as exact helper names or behavior revealed only by a failing runtime check. Surface an unresolved item as a blocker when either possible answer would materially change the plan.

**Complete when:** the implementer can follow the chosen approach without inventing architecture, changing product scope, or selecting between consequential alternatives.

## 4. Structure

Choose the smallest useful plan shape:

- **Lightweight:** low-risk, well-bounded work with no more than three independent implementation units. Return inline unless the user requests a file.
- **Durable:** cross-cutting, risky, handoff-oriented, or four-or-more-unit work. Save it as a repository artifact.

For every implementation unit, provide:

- **Outcome:** the meaningful state this unit creates.
- **Files or surfaces:** repo-relative paths or system areas expected to change.
- **Dependencies:** prior units or conditions required first.
- **Approach:** the decisions and boundaries governing the change.
- **Verification:** specific input or setup, action, and expected result.

Name test files when current evidence identifies them. Include exact commands only when they are canonical repository commands and remove ambiguity. Use stable unit IDs only when units depend on or refer to one another; retain those IDs during later revisions.

Describe design direction rather than writing implementation code. Add a diagram only when relationships, state, or sequence would otherwise be harder to understand.

**Complete when:** every unit is dependency-ordered, bounded, and observable, and every feature-bearing unit has specific behavioral verification.

## 5. Write

For a durable plan, follow the repository's existing plan location and naming convention. If none exists, use `docs/plans/YYYY-MM-DD-<type>-<short-name>-plan.md`. Create only the required plan directory and file. Keep every path inside the plan repo-relative.

Use this structure, omitting sections that carry no material information:

```markdown
# [Outcome]

## Frame
## Evidence
## Decisions
## Implementation
## Risks and Open Questions
## Completion
```

Keep `Completion` distinct from implementation detail: list the observable outcomes, required verification, and relevant documentation or operational state that prove the entire task is finished.

**Complete when:** the plan is concise, internally consistent, saved when durable, and contains no empty or ceremonial sections.

## 6. Audit and Deliver

Audit the complete plan against these questions:

- Does every requested outcome map to an implementation unit or an explicit deferral?
- Is every load-bearing statement grounded, settled, or assumed?
- Can each unit be completed without redesigning another unit?
- Does verification cover happy paths and the material edge, failure, integration, and real-app cases?
- Are unrelated cleanup and speculative features outside active scope?
- Do scope, decisions, units, risks, and completion criteria agree?

Revise until every answer is yes or the remaining gap is clearly marked as a blocker.

Deliver the self-contained inline plan or the absolute path to the saved artifact. Summarize material assumptions and blockers. Stop at the planning boundary.

**Complete when:** the user can review the plan or hand it to an implementer without needing earlier commentary to interpret it.
