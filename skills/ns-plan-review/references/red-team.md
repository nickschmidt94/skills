# Red-team Review

Use this branch only for an explicit Red-team request or an exposed boundary involving customer or irreplaceable data, authentication, privacy, permissions, money, destructive or irreversible effects, migrations or compatibility cutovers, uncertain external commits, correctness-sensitive concurrency or distributed state, or publication/deployment with expensive recovery.

## Blind packet

When delegation is available, dispatch one independent reviewer with only:

- the goal, constraints, non-goals, and authority boundary;
- the complete plan;
- the minimum authoritative sources needed to verify it; and
- the prompt below.

Withhold the author's reasoning, suspected problems, proposed fixes, and desired verdict. The reviewer is read-only and may not implement or edit the plan.

> Act as an implementation-readiness auditor. Assume a capable implementer will follow the plan literally without access to its author's reasoning. Simulate execution and report only plan defects that could cause an incorrect outcome, unauthorized effect, lost work, unverifiable completion, or forced redesign. For each finding, give the trigger, consequence, evidence, and smallest exact amendment. Do not produce an alternative plan or preference-driven rewrite.

If delegation is unavailable, run the same pass directly and disclose the fallback.

## Risk lenses

Apply each lens exposed by the affected boundary:

- failure paths, retry behavior, partial completion, recovery, rollback, and idempotency;
- concurrency, ordering, duplicate delivery, stale state, and race conditions;
- authentication, authorization, secrets, privacy, destructive actions, and external side effects;
- persistence, migrations, schemas, contracts, compatibility, and data integrity;
- repository state, build/runtime differences, deployment gates, and real-app acceptance; and
- scope pressure, unnecessary machinery, and conflict with stated non-goals.

## Fresh rereview

After amendments, prefer a fresh independent reviewer. Send the revised whole plan as a clean packet without earlier findings, defenses, or change explanations. Adjudicate and repair new proven findings under the main skill. Do not limit rereview to edited sections.

**Complete when:** the affected high-risk boundary received every applicable risk lens, the complete revised plan received a clean fresh pass, and independence or its disclosed fallback is recorded.
