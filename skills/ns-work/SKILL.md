---
name: ns-work
description: Implement and locally verify an approved plan or decision-complete repository change. Use when the current phase should produce a verified working tree without committing, pushing, opening a pull request, or deploying.
---

# NS Work

Implement the requested change and leave a locally verified working tree.

Use four standards throughout:

- **Decision-complete** — the request or accepted plan resolves product behavior, scope, and consequential technical choices.
- **Baseline** — repository state and pre-existing changes recorded before the first edit.
- **Owned** — changes introduced for the current request.
- **Green** — relevant verification passes, or every non-passing result is classified and reported.

`ns-work` owns local implementation and verification. Branch creation, commits, pushes, pull requests, deployment, publication, and external messages remain with separately authorized workflows.

## 1. Resolve

Use an explicit plan or specification, the single plan clearly accepted in the current conversation, or a concrete work request. Ask which source to use when more than one is plausible; never select a plan merely because it is newest.

Apply this authority order:

1. Active instructions and the latest user request
2. The accepted plan or specification
3. Current repository evidence

Repository evidence may invalidate an assumption but does not silently authorize new scope. Treat the plan as a decision artifact rather than an execution script.

Confirm that the work is decision-complete. Ask the smallest focused question that can close a material gap. When substantial product framing or architectural planning remains, stop and recommend that the user invoke `$ns-plan`.

**Complete when:** the target workspace, in-scope outcomes, consequential boundaries, settled decisions, and observable verification are known.

## 2. Establish the Baseline

Inspect the current sources of truth for the affected surface:

- owning implementation and nearby patterns;
- relevant tests, configuration, and documentation;
- canonical repository verification commands;
- repository status, current checkout, and pre-existing changes.

Identify the files or surfaces likely to become owned. Continue in the current checkout unless active repository instructions or the user require a branch or worktree.

Preserve every pre-existing change. When an owned edit cannot be separated safely from existing work in the same file, stop and ask how the user wants that overlap handled.

**Complete when:** existing behavior and constraints are understood, pre-existing changes are recorded, likely owned surfaces are identified, and no unsafe overlap blocks editing.

## 3. Decompose

Execute trivial work inline. For multi-unit work, create a dependency-ordered task list from the accepted plan or request.

Each task must name:

- its observable outcome;
- expected owned files or surfaces;
- dependencies that affect ordering;
- focused verification proving completion.

Keep progress in the task tracker and repository state. Leave the accepted plan unchanged unless the user separately requests a plan revision.

**Complete when:** every in-scope outcome maps to one task, dependencies determine a safe order, and no task requires redesigning the solution.

## 4. Implement to Green

For each task:

1. Read its owning code, tests, and referenced patterns.
2. Choose the evidence strategy.
3. Make the smallest coherent change that produces the task outcome.
4. Run focused verification.
5. Inspect the actual owned diff for scope and correctness.
6. Return the affected surface to green before starting the next task.

Choose evidence by change shape:

- **Regression or bug:** reproduce the failure before changing behavior.
- **Fragile legacy behavior:** establish characterization coverage first.
- **New testable behavior:** prefer a failing proof when it accurately represents the desired contract.
- **Configuration or packaging:** prefer a focused runtime or smoke check.
- **User-visible interface:** exercise the real interface and relevant viewport or interaction states.

Fix failures caused by the owned change. Investigate ambiguous failures until they are classified. Preserve scope when a failure is pre-existing or unrelated, and record it for delivery. Stop when authoritative verification cannot run and no in-scope remediation can restore it.

**Complete when:** the task outcome is observable, focused verification is green, and the task diff contains only owned changes.

## 5. Integrate

After all tasks are individually green:

- inspect the complete owned diff, including untracked and generated files;
- reconcile interactions across tasks and shared contracts;
- simplify settled code where doing so reduces accidental complexity without changing scope;
- run broader checks proportional to the affected surface and risk;
- exercise the real application when behavior is user-visible or integration-dependent.

Classify every remaining failure as owned, pre-existing, unrelated, environmental, or blocked. Resolve owned failures before delivery.

**Complete when:** every in-scope outcome works with the others, relevant broader verification is green, no unintended change remains, and unresolved evidence gaps are explicit.

## 6. Deliver

Report:

- the implemented outcome;
- every owned file changed;
- verification actually run and its result;
- pre-existing or unrelated failures encountered;
- remaining uncertainty or blockers;
- confirmation that pre-existing work was preserved.

Make completion claims only from fresh evidence gathered during this run. End with the verified working tree and leave shipping decisions to the user.

**Complete when:** the user can inspect, commit, or hand off the change without relying on earlier commentary to understand its state.
