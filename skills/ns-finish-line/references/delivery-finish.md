# Delivery Finish

Use this branch when the requested destination includes implementing repository work and opening a pull request.

## 1. Resolve the Task

Inspect the conversation, current workspace, repository state, applicable instructions, and any plan, specification, or issue that defines the work. Infer the intended outcome and acceptance evidence. Classify current changes and untracked files as task-owned or excluded, using history and content when provenance is unclear.

If substantial unresolved decisions remain, complete Decision Finish first. Otherwise form the smallest decision-complete, evidence-backed implementation plan and continue directly into execution.

**Complete when:** one coherent outcome, its scope, ownership boundary, settled decisions, and observable acceptance evidence are resolved.

## 2. Implement to Green

Load and follow `$ns-work` when available for baseline, implementation, focused checks, integration checks, and real-interface verification. NS Finish Line's operating contract governs ordinary questions and continuation between phases.

Preserve the existing checkout. Prefer an isolated branch or worktree when it cleanly protects unrelated local changes; otherwise work in place while keeping every excluded change intact. Make the smallest coherent change that satisfies the task, including focused documentation when a durable contract changes.

**Complete when:** every requested outcome is implemented, owned failures are repaired, relevant local verification is green, and the complete diff contains only intended work.

## 3. Close the Review Loop

Load and follow `$ns-code-review` in repair mode when available. Review against the intended base, repair every proven decision-complete finding, rerun proportional verification, and review the complete updated change again. Continue until no actionable finding remains.

Use specialized security, interface, browser, data, or platform skills only when the change presents that surface. Apply the hard-blocker rule to a finding that cannot be repaired safely within scope; never omit a repairable finding to publish sooner.

**Complete when:** a fresh final review finds no actionable finding and no owned verification failure remains.

## 4. Publish One Pull Request

Load and follow `$ns-ship-pr` when available. Create or reuse the correct feature branch, commit only owned work, push the live `HEAD` without force, and create or refresh one non-draft pull request against the verified base. NS Finish Line invocation supplies this publication authorization.

Build the title and body from the complete pushed range. Include the outcome, meaningful decisions or assumptions, verification actually run, and residual non-blocking uncertainty. Exclude secrets and unrelated local state.

Reload the GitHub pull request. Confirm it is open and ready for review and that its repository, head branch, head SHA, and base branch match the intended local state. Repair stale metadata or a mismatched push before finishing.

**Complete when:** exactly one intended open, non-draft pull request exists and its head SHA equals local `HEAD`.
