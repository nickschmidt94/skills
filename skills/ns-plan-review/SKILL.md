---
name: ns-plan-review
description: Independently red-team a completed software, product, or operational plan for implementation readiness, harden proven gaps, and re-review until ready or blocked. Use after planning and before implementation; do not use to create the initial plan or review code changes.
---

# NS Plan Review

Review a settled plan as a literal implementation contract. Find only defects
that could change the outcome, cross authority, lose work, prevent verification,
or force consequential redesign during implementation. Prove each finding,
make the smallest safe plan amendment when authorized, and close the loop with
a fresh whole-plan review.

## Leading Concepts

- **Blind:** Preserve independence from the plan author's reasoning and favored
  solution.
- **Literal:** Assume a capable implementer follows only what the plan says.
- **Proven:** Keep findings tied to an exact plan location and authoritative
  evidence.
- **Closed-loop:** A hardened plan is not ready until the revised whole plan is
  reviewed again.

## Scope and Authority

The default mode is **harden**: review the plan and edit only the reviewed plan
artifact when a proven finding has a decision-complete amendment.

Use **report-only** mode when the user says `review only`, `report-only`, or
otherwise forbids modifications. If the plan exists only in conversation,
default to report-only unless the user explicitly asks for a rewritten plan.

This skill may:

- read the plan, its named source material, repository guidance, and current
  read-only state needed to test its claims;
- inspect code, tests, configuration, schemas, APIs, queues, PR state, or live
  read-only surfaces when they are authoritative for the plan;
- edit only the plan artifact in harden mode.

This skill must not:

- implement the plan or change product code, tests, configuration, data, or
  infrastructure;
- commit, push, deploy, merge, publish, send, trade, purchase, or trigger other
  consequential external effects;
- silently expand the plan's outcome, non-goals, authority, or acceptance bar;
- replace the plan with a preferred architecture when the existing approach is
  workable.

If the supplied material is not yet a completed plan, stop and say that initial
planning is required. Do not invent the missing plan under this skill.

## Review Procedure

Follow every step in order. Do not issue a readiness verdict early.

### 1. Resolve the review contract

Identify:

- the plan artifact or exact inline plan under review;
- the intended outcome and acceptance evidence;
- constraints, non-goals, and authority boundaries;
- the current mode: harden or report-only;
- the authoritative sources needed to test the plan;
- whether this agent authored or materially revised the plan.

If the plan, intended outcome, or authority boundary cannot be resolved from
available context, return `Review incomplete` with the exact missing input.

Completion check: the reviewer can state what success means, what must not
happen, what may be edited, and which evidence governs disagreements.

### 2. Establish an independent review

If the current agent authored or materially revised the plan, dispatch one
independent in-platform reviewer when delegation is available. If the current
context is already a fresh review packet from another agent, review it directly.

Give the independent reviewer only:

- the goal, constraints, non-goals, and authority boundary;
- the complete plan;
- the minimum authoritative sources needed to verify it;
- the review prompt below.

Withhold the author's reasoning, suspected problems, proposed fixes, and desired
verdict. The reviewer is read-only and may not implement or edit the plan.

Use this prompt:

> Act as an implementation-readiness auditor. Assume a capable implementer will
> follow the plan literally without access to its author's reasoning. Simulate
> execution and report only plan defects that could cause an incorrect outcome,
> unauthorized effect, lost work, unverifiable completion, or forced redesign.
> For each finding, give the trigger, consequence, evidence, and smallest exact
> amendment. Do not produce an alternative plan or preference-driven rewrite.

If independent delegation is unavailable, perform the same pass directly and
disclose that independence was not achieved. Lack of delegation alone does not
make the review incomplete.

Completion check: either an independent reviewer has received a blind packet,
or the final report explicitly identifies the non-independent fallback.

### 3. Run an implementation pre-mortem

Walk through the plan in execution order. Apply all core lenses and every risk
lens exposed by the plan.

#### Core lenses

- **Traceability:** Every requested outcome, constraint, non-goal, and
  acceptance condition maps to a concrete plan step and verification artifact.
- **Decision completeness:** An implementer does not need to invent a material
  product, architecture, data, security, operational, or UX decision.
- **Executability:** Steps name the real targets, dependencies, order,
  ownership, and completion conditions needed to act safely.
- **Evidence coverage:** Verification proves the user-visible or operational
  outcome, not merely compilation, deployment, or the existence of changed
  files.

#### Risk lenses

Apply each relevant lens:

- failure paths, retry behavior, partial completion, recovery, rollback, and
  idempotency;
- concurrency, ordering, duplicate delivery, stale state, and race conditions;
- authentication, authorization, secrets, privacy, destructive actions, and
  external side effects;
- persistence, migrations, schemas, contracts, compatibility, and data
  integrity;
- repository state, build/runtime differences, deployment gates, and real-app
  acceptance;
- scope pressure, unnecessary machinery, and steps that conflict with stated
  non-goals.

Do not reward verbosity. A short plan can be complete, and a long plan can still
hide a missing decision.

Completion check: each plan step has been simulated literally, every core lens
has been applied, and every exposed risk lens has either been tested or marked
not applicable.

### 4. Prove and rank findings

Keep a finding only when it contains all of:

1. exact plan location;
2. concrete trigger or execution scenario;
3. material consequence;
4. authoritative evidence or a direct contradiction inside the plan;
5. the smallest exact amendment that closes the gap;
6. confidence: high, medium, or low.

Discard:

- style preferences and wording polish without implementation consequence;
- generic cautions without a reachable failure scenario;
- speculative future requirements outside the stated outcome;
- duplicate symptoms of the same root defect;
- alternate designs that do not prove the selected design fails.

Use these severities:

- **P0:** Could cause catastrophic data loss, unauthorized irreversible action,
  or another critical failure.
- **P1:** The normal path cannot achieve the outcome, crosses authority, or
  requires consequential redesign during implementation.
- **P2:** A reachable edge or integration path can lose, duplicate, misroute, or
  leave the outcome unprovable.
- **P3:** A narrow ambiguity or structural cost is likely to cause an
  implementation error but does not invalidate the main path.

Completion check: every surviving finding is actionable and independently
checkable; preference-only and duplicate findings are gone.

### 5. Adjudicate and harden

Reconcile reviewer findings against the plan and authoritative evidence. Do not
accept a finding merely because another agent produced it.

In harden mode, amend the plan only when the amendment:

- fixes a proven finding;
- preserves the settled outcome, constraints, and non-goals;
- is decision-complete rather than a reminder to decide later;
- changes only the plan artifact;
- preserves stable step or requirement IDs when they exist.

Record the finding as fixed with its exact amendment. Leave disputed,
insufficiently evidenced, or authority-expanding findings unresolved and explain
why. In report-only mode, propose the amendment without editing.

If a finding reveals a missing user decision that would materially change the
outcome or authority, do not guess. Mark it unresolved.

Completion check: each finding is fixed, rejected with evidence, or unresolved
for a named reason; no implementation artifact has changed.

### 6. Re-review the complete revised plan

After any amendment, run a fresh whole-plan review. Prefer a fresh independent
reviewer and send the revised plan as a clean packet without the earlier
findings, defenses, or change explanations.

Do not limit the second pass to edited sections. Amendments can create new
contradictions elsewhere.

Allow at most two hardening attempts for the same root finding. If it survives
two attempts, stop revising and return `Amendments required` with the unresolved
decision or evidence gap.

Completion check: the latest full plan, not merely its diff, has received a
fresh review and all new findings have been adjudicated.

### 7. Deliver the verdict

Use exactly one verdict:

- **Ready for implementation:** No unresolved P0-P2 findings remain, all
  amendments have passed fresh whole-plan review, and acceptance evidence is
  executable. Any P3 observations must be explicitly non-blocking.
- **Amendments required:** One or more proven findings remain unresolved or the
  plan needs a material user decision.
- **Review incomplete:** The plan, authority, or authoritative evidence needed
  for a defensible review was unavailable.

Report in this order:

1. verdict;
2. fixed findings, including exact amendments;
3. unresolved findings, highest severity first;
4. rejected or non-blocking observations only when they clarify a disputed
   point;
5. independence used or fallback disclosed;
6. evidence inspected and checks actually performed;
7. the next required action.

If there are no findings, say so directly. Never manufacture findings to make
the review appear valuable.

## Finding Format

Use this compact structure for each surviving finding:

```text
[P1] Short defect title
Location: Plan step or requirement ID
Trigger: Exact execution scenario
Consequence: Material failure
Evidence: Authoritative source or plan contradiction
Amendment: Smallest exact plan change
Status: Fixed | Unresolved | Rejected
Confidence: High | Medium | Low
```

The final output is the hardened plan plus its review verdict, not a second
competing plan.
