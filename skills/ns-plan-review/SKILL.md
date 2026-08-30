---
name: ns-plan-review
description: Proportionally review and directly harden a completed software, product, or operational plan for implementation readiness. Use Builder posture for ordinary work and Red-team posture for exposed high-risk boundaries or explicit red-team requests. Apply proven fixes and re-review until ready or blocked; do not use to create the initial plan or review code changes.
---

# NS Plan Review

Review a settled plan as a literal implementation contract. Use the lightest
posture that covers its exposed risk. Find only defects
that could change the outcome, cross authority, lose work, prevent verification,
or force consequential redesign during implementation. Prove each finding,
apply the smallest safe plan amendment without returning control between fixes,
and close the loop with a fresh whole-plan review.

## Leading Concepts

- **Proportional:** Use direct Builder review for ordinary work and blind
  Red-team review only for exposed high-risk boundaries.
- **Literal:** Assume a capable implementer follows only what the plan says.
- **Proven:** Keep findings tied to an exact plan location and authoritative
  evidence.
- **Repair:** Apply proven, decision-complete amendments directly to the plan.
- **Closed-loop:** A hardened plan is not ready until the revised whole plan is
  reviewed again.

## Scope and Authority

The default mode is **harden**: review the plan, apply every proven and
decision-complete amendment directly to the reviewed plan, then re-review it
until ready or blocked. A safe fix is work to complete, not merely a finding to
present.

Use **report-only** mode when the user says `review only`, `report-only`, or
otherwise forbids modifications. In harden mode, treat an inline plan as an
editable deliverable and return its complete revised replacement.

The default posture is **Builder** for reversible, pre-customer, local, and
ordinary product work. Use **Red-team** when explicitly requested or when an
exposed boundary involves customer or irreplaceable data,
authentication/privacy/permissions/money, destructive or irreversible effects,
migrations or compatibility cutovers, uncertain external commits,
correctness-sensitive concurrency or distributed state, or
publication/deployment with expensive recovery. Escalate the affected boundary,
not unrelated plan sections.

This skill may:

- read the plan, its named source material, repository guidance, and current
  read-only state needed to test its claims;
- inspect code, tests, configuration, schemas, APIs, queues, PR state, or live
  read-only surfaces when they are authoritative for the plan;
- edit only the plan artifact, or rewrite the inline plan, in harden mode.

This skill must not:

- execute the plan or change product code, tests, configuration, data, or
  infrastructure; implementing a finding means amending the plan itself;
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
- the current posture: Builder or Red-team, with its trigger;
- the authoritative sources needed to test the plan; for load-bearing third-party library or API behavior, use `$firecrawl-developer-index` when available, with official documentation or repository sources as the fallback;
- whether this agent authored or materially revised the plan.

If the plan, intended outcome, or authority boundary cannot be resolved from
available context, return `Review incomplete` with the exact missing input.

Completion check: the reviewer can state what success means, what must not
happen, what may be edited, and which evidence governs disagreements.

### 2. Establish the review posture

In Builder posture, review the complete plan directly. Do not dispatch an
independent reviewer merely because the current agent helped author the plan.

In Red-team posture, read [Red-team Review](references/red-team.md) and apply its
blind packet, risk lenses, and independence rules. If delegation is unavailable,
perform the same pass directly and disclose the fallback; missing delegation
alone does not make the review incomplete.

Completion check: the selected posture matches the plan's exposed risk, and any
required Red-team packet or disclosed fallback is established.

### 3. Run an implementation pre-mortem

Walk through the plan in execution order. Apply every Builder lens. In Red-team
posture, also apply every exposed risk lens from the referenced review.

#### Core lenses

- **Outcome and traceability:** The smallest coherent product result is clear,
  and every requested outcome, constraint, non-goal, and
  acceptance condition maps to a concrete plan step and verification artifact.
- **Decision completeness:** An implementer does not need to invent a material
  product, architecture, data, security, operational, or UX decision.
- **Executability:** Steps name the real targets, dependencies, order,
  ownership, and completion conditions needed to act safely.
- **Depth and locality:** Meaningful behavior sits behind a small interface at a
  real seam, with policy, change, and verification concentrated in one owner.
- **Legibility:** A fresh human or agent can locate authority, context,
  contracts, ownership, and canonical verification without conversation history.
- **Context placement:** Domain terms, ADR-grade decisions, repository
  learnings, ordinary documentation, tests, and code live in their proper homes.
- **Evidence coverage:** Verification proves the user-visible or operational
  outcome, not merely compilation, deployment, or the existence of changed
  files.

Do not reward verbosity. A short plan can be complete, and a long plan can still
hide a missing decision.

Completion check: each plan step has been simulated literally, every Builder
lens has been applied, and every Red-team risk lens required by the selected
posture has been tested or marked not applicable.

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

In harden mode, directly apply every amendment that:

- fixes a proven finding;
- preserves the settled outcome, constraints, and non-goals;
- is decision-complete rather than a reminder to decide later;
- changes only the plan artifact;
- preserves stable step or requirement IDs when they exist.

Batch compatible amendments into the plan without pausing for confirmation or
returning a safe fix as a recommendation. Resolve a gap from authoritative
evidence and settled constraints when exactly one compatible answer follows.

Record each applied change with its exact plan location and the implementation-
time question, handoff, or recovery gap it removes. Leave disputed,
insufficiently evidenced, authority-expanding, or genuinely choice-dependent
findings unresolved and explain why. In report-only mode, propose amendments
without editing.

Classify every applied or unresolved finding as `Upstream candidate: Yes` when
a reusable planning rule could have exposed the defect before the plan was
settled; otherwise classify it as `No`. This classification explains where the
lesson belongs and does not change severity, adjudication, or readiness.

If a finding reveals a missing user decision that would materially change the
outcome or authority, do not guess. Mark it unresolved.

Completion check: every safe, decision-complete fix has been applied to the
plan; each applied or unresolved finding has an upstream classification; each
remaining finding is rejected with evidence or unresolved for a named reason;
no implementation artifact has changed.

### 6. Re-review the complete revised plan

After any amendment, run a fresh whole-plan consistency review without the
earlier findings steering the pass. In Red-team posture, use the referenced
fresh independent rereview when available. Apply any new proven,
decision-complete findings and repeat the whole-plan review.

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
2. the updated plan artifact, or the complete revised plan when it was inline;
3. applied changes, including exact locations and the implementation-time
   question, handoff, or recovery gap each change removed;
4. upstream candidates, stated as reusable planner rules and omitted when none;
5. unresolved findings, highest severity first;
6. rejected or non-blocking observations only when they clarify a disputed
   point;
7. posture used, plus independence or fallback when Red-team applied;
8. evidence inspected and checks actually performed;
9. the next required action.

If there are no findings, say so directly. Never manufacture findings to make
the review appear valuable.

## Change Formats

Use this compact structure for each applied change:

```text
[Applied] Short repair
Location: Plan step or requirement ID
Change: Exact amendment made
Autonomy gained: Implementation-time question, handoff, or recovery gap removed
Evidence: Authoritative source or plan contradiction
Upstream candidate: Yes | No
```

Use this compact structure for each unresolved or rejected finding:

```text
[P1] Short defect title
Location: Plan step or requirement ID
Trigger: Exact execution scenario
Consequence: Material failure
Evidence: Authoritative source or plan contradiction
Amendment: Smallest exact plan change
Status: Unresolved | Rejected
Confidence: High | Medium | Low
Upstream candidate: Yes | No | N/A
```

Use `N/A` only for a rejected observation because no proven defect remains to
move upstream.

The final output is the updated plan plus its review verdict and applied-change
summary, not a findings report or a second competing plan.
