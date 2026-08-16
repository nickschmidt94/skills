---
name: ns-simplify
description: Simplify settled, recently changed code for clarity, reuse, and lower structural cost while preserving observable behavior. Use after implementation and before independent review when the selected scope may be edited and locally verified.
---

# NS Simplify

Improve settled code without redesigning it. A successful pass leaves behavior unchanged and the implementation easier to understand, maintain, or execute.

Use four standards throughout:

- **Settled** — the intended behavior and consequential design choices are already decided.
- **Bounded** — edits stay within the selected change and its necessary seams.
- **Equivalent** — outputs, errors, side effects, ordering, and public contracts remain intact.
- **Simpler** — cognitive or structural cost decreases; fewer lines alone prove nothing.

This skill authorizes local edits and verification only. Preserve pre-existing work. Behavior changes, unrelated fixes, commits, pushes, pull requests, and deployment require separately authorized workflows.

## 1. Resolve

Resolve the simplification scope in this order:

1. Use the exact files, directory, or change named by the user.
2. Otherwise, in git, use the current branch against its resolved base.
3. Without a usable base, use staged and unstaged changes against `HEAD`.
4. Outside git, use files named or edited in the current conversation.

If no non-empty scope can be established, ask what to simplify. If the scope contains only documentation, generated or vendored files, dependency metadata, lockfiles, or mechanical churn, report that there is no substantive code to simplify and stop. In a mixed scope, retain the human-authored code.

Establish the intended behavior and its best available oracle: existing tests, types, contracts, callers, runtime checks, or directly comparable outputs. Record repository status and the existing diff before editing. Identify the mutation boundary and any import or export seams required to keep the scoped code valid.

**Complete when:** the substantive scope, intended behavior, verification oracle, mutation boundary, and pre-existing changes are explicit.

## 2. Inspect

Read every scoped file plus the callers, dependencies, tests, and contracts needed to prove equivalence. Inspect the code through three lenses:

- **Reuse:** replace new duplication with an existing helper, built-in, or verified platform guarantee only when its semantics match the inputs in play.
- **Clarity:** reduce redundant state, copy-paste variation, unnecessary indirection, deeply nested control flow, leaky abstractions, stale narration, and verified dead code. Preserve named concepts and useful boundaries.
- **Waste:** remove duplicate computation, repeated reads or calls, no-op updates, avoidable broad operations, resource leaks, and objectively redundant hot-path work.

Treat concurrency, caching-policy changes, algorithm replacements, and other timing-sensitive optimizations as implementation work unless exact equivalence is already proven. Preserve validation, authorization, data-loss protection, error handling, accessibility affordances, and other trust-boundary guards.

For each candidate, identify the concrete cost removed, the proposed form, the evidence of equivalence, and the smallest affected surface. Skip preference-only rewrites and abstractions justified only by hypothetical future reuse.

**Complete when:** every scoped file has received all three lenses and each retained candidate has a concrete simplification benefit, a bounded edit, and credible equivalence evidence.

## 3. Apply

Apply one coherent simplification at a time. Edit only the resolved boundary and necessary import or export seams. Keep each change small enough to explain and verify independently.

Preserve observable behavior, including error shapes, side effects, ordering, serialization, locale behavior, accessibility behavior, and public or persisted contracts. Remove compatibility code created earlier in the unshipped change only after proving it was never deployed, persisted, published, externally consumed, or used outside the mutation boundary.

Use tests as behavioral oracles. Preserve their assertions and coverage strength. After each meaningful edit, run the cheapest focused proof that can expose an equivalence failure before proceeding. Revert or skip an edit when available evidence cannot establish equivalence.

**Complete when:** every applied edit is within the mutation boundary, independently understandable, behavior-preserving by current evidence, and green under its focused proof.

## 4. Verify

Inspect the complete simplification-owned diff against the baseline. Confirm that it contains no behavior changes, unrelated cleanup, accidental generated files, or modifications to pre-existing user work.

Run verification proportional to the final blast radius:

- focused tests for changed behavior;
- relevant type, lint, build, or static checks;
- broader tests for shared code or cross-cutting changes; and
- the real interface or integration path when observable behavior depends on it.

Classify every failure as simplification-owned, pre-existing, unrelated, environmental, or blocked. Fix or revert simplification-owned failures. Retain only edits whose equivalence is supported by the available evidence. State explicitly when a relevant verifier is unavailable or not configured.

**Complete when:** the integrated diff is bounded and simpler, relevant verification is green, every remaining failure is classified, and no unproven edit remains.

## 5. Deliver

Report:

- what became simpler and why;
- every file changed;
- verification actually run and its result;
- candidates skipped because value or equivalence was insufficient;
- pre-existing or unrelated failures encountered; and
- remaining uncertainty or blockers.

If no worthwhile simplification survived verification, say so and leave the code unchanged. Do not use net lines removed as the success metric. End with the locally verified working tree and leave independent review to `$ns-code-review`.

**Complete when:** the user can inspect or review the result without relying on earlier commentary, and every completion claim is supported by fresh evidence.
