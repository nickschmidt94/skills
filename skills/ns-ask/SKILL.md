---
name: ns-ask
description: Answer questions about a codebase, interview the user to settle requirements before planning, advise on a technical decision, or explain an existing plan, in one repeatable evidence-backed format. Use when the user asks how, where, or why something works, wants requirements clarified, asks which option to choose, or wants a plan explained. Do NOT use to write or review a plan, or to change code.
---

# NS Ask

Give the user a grounded, structured answer they can act on, then point to the next step.

Use four standards throughout:

- **Grounded** — every load-bearing claim cites current evidence, a settled user decision, or a visible assumption.
- **Direct** — lead with the answer; explanation supports it rather than replacing it.
- **Repeatable** — every response uses the same sections in the same order, so answers are easy to scan and compare.
- **Bounded** — answer the question asked; record adjacent concerns under Open questions instead of expanding scope.

This skill authorizes read-only work: reading files, searching, and inspecting repository status and history. Editing files, running tests or builds, installing dependencies, and any command with side effects require a separately authorized workflow.

## 1. Classify

Infer the mode from the user's request and current context:

- **Codebase Q&A** — how, where, or why something in the code works or came to be.
- **Requirements interview** — the user wants to build or change something whose scope, behavior, or edge cases are not yet settled.
- **Decision advice** — the user asks which of several approaches to take, or whether to do something.
- **Plan explanation** — the user asks what an existing plan, specification, or ticket means, how its parts fit, or why it chose something.

Choose the single mode that best fits. When a request spans modes, answer in the primary mode and record the rest under Open questions. Name the mode at the top of the response; when the user redirects to another mode, switch without re-asking.

**Complete when:** one mode is selected and the question it must answer is stated in a sentence.

## 2. Ground

Inspect the smallest source set that can support the answer:

- applicable repository instructions and any named file, plan, ticket, or URL;
- the implementation, tests, configuration, and documentation around the affected surface;
- git history or blame only when the question is about why or when something changed.

Prefer the environment over memory or cached prose for discoverable facts. Treat decisions already settled in the conversation as authoritative unless current evidence shows they cannot work.

Label each load-bearing claim:

- **Verified:** confirmed from the current source of truth, cited as `path:line`.
- **Settled:** decided by the user or an authoritative product source.
- **Assumed:** necessary to answer but not yet confirmed.

**Complete when:** the answer rests on cited evidence, settled decisions, or explicit assumptions, and any claim that could not be grounded is identified.

## 3. Work the Mode

- **Codebase Q&A:** answer exactly what was asked. Trace the real path through the code rather than describing what similar code usually does.
- **Requirements interview:** identify the unresolved choices that would change behavior, scope, architecture, or risk, and order them by consequence. Ask exactly one question per response, with a recommended answer and why the choice matters. After each reply, record the settled decision and ask the next question. Stop asking when the remaining unknowns would not change the plan, then produce a requirements brief covering goal, scope, non-goals, behavior, edge cases, constraints, and success signal.
- **Decision advice:** compare the credible options on the criteria that matter for this codebase, such as correctness, complexity, reversibility, operational risk, and fit with existing patterns. Recommend one option and state what would change the recommendation.
- **Plan explanation:** walk through the plan in its own order, explaining what each part produces, why it exists, and how it depends on the others. Flag contradictions, gaps, or stale assumptions against the current code without rewriting the plan.

**Complete when:** the mode's question is answered, or, during an interview, the single most consequential open question is ready to ask.

## 4. Respond

Use these sections in this order every time. Omit only the mode section for Codebase Q&A, and write `None` under Open questions when nothing remains open.

```markdown
**Mode:** <Codebase Q&A | Requirements interview | Decision advice | Plan explanation>

## Answer
The direct answer in one to three sentences. In an interview, summarize what is settled so far.

## Evidence
- `path:line` — Verified: ...
- Settled: ...
- Assumed: ...

## Explanation
How it works or why, in plain language.

## <Mode section>

## Open questions

## Next step
```

Mode sections:

- **Requirements interview:** `## Question` with the one current question, the recommended answer, and why it matters; replaced by `## Requirements brief` when the interview is complete.
- **Decision advice:** `## Options` with a trade-off comparison of each option, followed by the recommendation.
- **Plan explanation:** `## Walkthrough` with the plan's parts in order, followed by any flagged gaps.

**Complete when:** the response follows the format, every claim in Answer and Explanation is backed by an Evidence entry, and Next step names one concrete action.

## 5. Hand Off

Name the next step that fits the result:

- a settled requirements brief or chosen option: create an implementation plan, using `$ns-plan` when available;
- an explained plan that is ready: review it with `$ns-plan-review` or implement it with `$ns-work` when available;
- a Q&A answer that reveals needed change: plan that change, using `$ns-plan` when available;
- a Q&A answer that resolves the question: state that no further step is needed.

When a suggested companion is unavailable, describe the equivalent next step in plain language. Do not run the next step; stop after delivering the response.

**Complete when:** the user can act on the response without earlier commentary, and no file or repository state has changed.
