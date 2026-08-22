---
name: finish-line
description: "Carry work autonomously to its requested terminal artifact: resolve interviews and wayfinding into decision-complete artifacts and ready tickets, or implement and verify repository work through one open pull request. Use when the user invokes Finish Line to accept recommended answers and continue without ordinary approval pauses; stop before implementation when the requested destination is planning only, and before merge or deployment for delivery work."
---

# Finish Line

Own the current work until its requested finish line is real and verified.

## Route

Resolve the destination from the user's request and current artifacts:

- **Decision finish** — the work is an interview, wayfinding map, plan, design, specification, or ticket breakdown. Read [Decision Finish](references/decision-finish.md) and end with every decision ticket resolved plus any requested plan, specification, or implementation tickets ready.
- **Delivery finish** — the work is an implementation, repair, or repository change. Read [Delivery Finish](references/delivery-finish.md) and end with one accurate, open pull request ready for review.
- **End to end** — the request includes both. Complete Decision Finish first, then carry its approved-by-recommendation artifacts through Delivery Finish.

Use the narrowest route that reaches the requested destination. Planning-only invocation authorizes creating, updating, and resolving its in-scope planning artifacts and tracker issues. Delivery invocation authorizes the branch, edits, verification, commits, non-force push, and one pull request required by Delivery Finish. Neither route authorizes merge, deployment, unrelated publication or messages, destructive cleanup, history rewriting, or unrelated work.

## Operating Contract

Use these standards throughout:

- **Relentless** — continue through ordinary uncertainty, questions, failed checks, findings, and recoverable tool errors.
- **Recommended** — produce the best supported answer to every in-scope question and select it automatically.
- **Truthful** — record an autonomous choice as an agent-selected recommendation, never as the user's stated answer or approval.
- **Owned** — preserve pre-existing and unrelated work; mutate only the coherent task.
- **Confirmed** — finish only when the route's terminal criteria are observable in the actual artifacts or external system.

Answer questions in this order:

1. The user's latest request and explicit constraints.
2. Accepted decisions, specifications, issues, and current task context.
3. Applicable repository instructions and project documentation.
4. Evidence from the environment, code, tests, history, research, and established conventions.
5. The smallest reversible recommendation that is correct, coherent, and within scope.

When a companion skill presents a recommendation, treat it as the candidate answer. Validate it against higher-authority evidence, revise it when necessary, then select the best supported recommendation and continue. Record consequential assumptions and trade-offs in the durable artifact.

Companion skills are accelerators, not dependencies. Load and follow the narrowest applicable installed skills, subject to this operating contract. If Wayfinder, Grill with Docs, grilling, domain modeling, spec, or ticketing companions are absent, perform the Decision Finish fallback directly. If work, review, shipping, or specialized verification companions are absent, perform the Delivery Finish behavior directly. Never claim an unavailable skill ran.

A **hard blocker** exists only when no safe in-scope path remains because completion requires unavailable credentials or access, an external dependency the agent cannot restore, a destructive or consequential action outside this authorization, or a decision whose plausible answers create materially different irreversible outcomes with no evidence favoring one. Exhaust safe alternatives first. Report the evidence, attempts, and smallest action needed to resume; never claim the finish line.

## Delivery

Lead with the terminal artifact: ticket/map/spec links for Decision Finish or the pull request link for Delivery Finish. State which route ran, the recommendations selected or implementation outcome, verification performed, and any excluded work or residual uncertainty. Distinguish agent-selected recommendations from user decisions, and distinguish local, published, open, merged, and deployed states.
