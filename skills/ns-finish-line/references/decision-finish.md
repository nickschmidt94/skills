# Decision Finish

Use this branch when the requested destination is a resolved decision set, plan, specification, wayfinding map, or implementation tickets rather than completed implementation.

## Authority

NS Finish Line's explicit recommendation mode replaces ordinary interview and approval pauses. It does not impersonate the user: every answer selected without the user is an **agent-selected recommendation** with its basis preserved.

When an installed companion normally waits for the user after presenting recommendations, select the best supported recommendation and continue. When Wayfinder normally limits a session to one ticket, continue across the frontier until the requested map is decision-complete. Preserve its claim, dependency, concurrency, and single-source-of-truth rules. When `to-tickets` normally asks for breakdown approval, evaluate its own questions, apply the recommended breakdown, and publish it.

## 1. Resolve the Destination

Inspect the conversation, referenced documents, tracker, repository guidance, glossary, ADRs, current artifacts, and relevant environment evidence. State the terminal decision artifact and its scope. Build a dependency tree of every material question between the current state and that destination; keep downstream questions blocked until their prerequisites settle.

Use an installed companion when it fits:

- Wayfinder for a large or multi-session decision map.
- Grill with Docs or grilling for a branching interview.
- Domain modeling when terms, boundaries, or architectural decisions need durable project documentation.
- `to-spec` when the resolved context should become a buildable specification.
- `to-tickets` when resolved work should become implementation tickets.

If a companion is unavailable, use the same artifact shape already present in the project. If no tracker is configured, use a local Markdown map and one local Markdown file per ticket with stable titles and explicit dependencies.

**Complete when:** the destination, scope, sources of truth, artifact location, and full visible decision frontier are known.

## 2. Resolve Every Question by Recommendation

Work the unblocked frontier in dependency order. For each question:

1. Find facts from available sources instead of manufacturing them or asking the user to retrieve them.
2. Identify viable options and the trade-offs that affect the destination.
3. Produce one recommended answer using the NS Finish Line authority order.
4. Stress-test it against constraints, edge cases, glossary terms, and dependent decisions.
5. Select it and record `Agent-selected recommendation`, its rationale, consequential assumptions, and material uncertainty in the owning artifact.
6. Recompute the frontier, adding newly visible questions and removing invalidated ones.

Select the recommendation even when confidence is imperfect if the choice is reversible and evidence favors it. Apply the hard-blocker rule only to materially divergent, irreversible choices with no supported recommendation.

For a Wayfinder map, resolve and close each decision ticket, add its linked gist to Decisions so far, graduate all specifiable fog into tickets, and continue until both the frontier and Not yet specified are empty for the destination. Preserve decision details in their owning tickets instead of duplicating them in the map.

**Complete when:** every material branch has a recorded recommended resolution, no decision prerequisite remains open or hidden in fog, terminology is internally consistent, and consequential uncertainty is explicit.

## 3. Produce Decision-Complete Handoff Artifacts

Update the requested plan, specification, glossary, ADRs, map, or ticket resolutions as decisions settle. Create an ADR only for a hard-to-reverse, surprising trade-off. Keep facts, recommendations, user-stated decisions, and assumptions distinguishable.

When implementation tickets are part of the destination, create dependency-ordered tracer-bullet tickets. Each ticket must:

- deliver one narrow, end-to-end, independently verifiable behavior;
- fit one fresh implementation context;
- state concrete acceptance criteria;
- name actual blockers and expose the unblocked frontier;
- use project vocabulary and the configured tracker shape; and
- be marked ready for agent execution.

Review the complete set yourself using the questions an approval round would ask: Is the granularity executable? Are slices vertical? Are blocking edges necessary and sufficient? Is every accepted decision represented exactly once? Revise until the recommended answer to each is yes, then publish or write the tickets without pausing for approval.

**Complete when:** the durable decision artifacts agree, every requested implementation ticket exists in the actual tracker or local fallback, all tickets have acceptance criteria and correct dependencies, and no unresolved decision prevents an implementation agent from starting at the frontier.

## 4. Confirm the Decision Finish

Reload the published or local artifacts. Verify links, titles, states, dependencies, labels or status, and the absence of unresolved decision tickets or fog. Confirm that autonomous selections are labeled as agent-selected recommendations and that no artifact falsely attributes approval to the user.

If the user's requested destination was planning only, stop here. If the request also authorized implementation, return to NS Finish Line and begin Delivery Finish from these artifacts.

**Complete when:** the decision system itself shows the intended work decision-complete and ready for execution.
