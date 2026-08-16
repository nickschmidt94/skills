---
name: ns-code-review
description: Review a local change, branch, commit range, or pull request for introduced defects and regression risk. Use for an evidence-backed, report-only assessment before committing, publishing, or advancing a verified change.
---

# NS Code Review

Review a change without modifying it. Produce a self-contained report that distinguishes proven findings from testing gaps, pre-existing issues, and unresolved uncertainty.

Use four standards throughout:

- **Scope** — identify the exact change, intent, and comparison point.
- **Introduced** — make the reviewed change responsible only for problems it creates or requirements it fails to implement.
- **Proven** — verify each finding against the surrounding system rather than inferring it from an isolated hunk.
- **Actionable** — state the concrete condition, consequence, and response.

Operate report-only. Preserve the checkout and working tree. Fixes, simplification, commits, pushes, pull requests, and deployment require separately authorized workflows.

## 1. Resolve the Scope

Determine the review target from the request and current repository state:

- current working tree, including staged and unstaged changes;
- an explicit base ref or commit range;
- a named branch; or
- a pull request.

Resolve the correct comparison point and inspect targets without switching branches. For a local review, include untracked files that implement the reviewed intent and disclose every excluded untracked path. For a remote branch or pull request, inspect the target revision rather than similarly named files in the current checkout.

Establish intent from the user request, an explicitly supplied or clearly accepted plan or specification, pull-request context, commit messages, and the diff. Prefer a focused question when two plausible scopes would review materially different changes.

**Complete when:** the target, comparison point, intended outcome, included files, and exclusions are explicit, and the resolved diff covers the whole requested change.

## 2. Ground the Change

Read the complete diff and the current sources needed to understand it:

- applicable repository instructions;
- affected implementation and its callers or consumers;
- nearby tests, configuration, types, schemas, and public contracts;
- accepted requirements and relevant documentation.

Inspect enough surrounding code to trace changed behavior beyond the diff hunk. In remote reviews, read source from the reviewed revision. Treat repository configuration and scripts as the current source of truth instead of restating cached commands or conventions.

Record the repository baseline before running verification so pre-existing and tool-generated changes remain distinguishable.

**Complete when:** every changed file is accounted for, every changed behavior is understood in its runtime context, and the governing requirements and standards are known.

## 3. Inspect the Risks

Review correctness for every changed behavior. Apply the other lenses only when the change presents their surface:

- tests and failure coverage;
- authentication, authorization, input, secrets, and destructive operations;
- persistence, migrations, and data integrity;
- public APIs, types, serialization, and compatibility;
- errors, retries, timeouts, background work, and partial failure;
- concurrency, ordering, and lifecycle behavior;
- queries, transforms, caching, and material performance cost;
- agent-facing instructions, tools, and automation;
- user-visible behavior and accessibility.

Trace inputs, state transitions, outputs, error paths, and affected callers. Treat complexity as a finding only when the change introduces a concrete correctness, regression, testability, or repository-standards risk. Leave preference-driven cleanup to a separate simplification pass.

For an explicitly requested deep or independent review, or a change that crosses a material trust boundary such as authorization, payments, persistence, destructive operations, concurrency, or a public contract, dispatch one independent in-platform reviewer with the exact scope and relevant risk lens. Give it the diff and task-local context, collect it before synthesis, and verify its findings normally. If independent review is unavailable, continue and disclose the missing coverage.

**Complete when:** every changed behavior has received correctness review, each material risk lens was applied or found irrelevant, and any required independent pass has returned or its absence is recorded.

## 4. Prove the Findings

For every candidate finding:

1. Read the cited code and enough surrounding control flow to rule out handling elsewhere.
2. Confirm the reviewed change introduced the defect or omitted an accepted requirement.
3. Identify the triggering condition and concrete consequence.
4. Verify the exact file and line against the reviewed revision.
5. Run focused tests or checks when they can materially confirm or refute the claim.
6. State the smallest credible response and the remaining confidence.

Discard speculative findings, stylistic preferences, and duplicates of authoritative automated output. Keep missing or unavailable verification under testing gaps unless it proves a defect. Mention a pre-existing issue separately only when it affects the reviewed change, blocks verification, or materially changes the verdict.

Calibrate severity:

- **P0:** exploitable breakage, data loss, or critical system failure.
- **P1:** high-impact defect likely on a normal path or a broken contract.
- **P2:** real moderate downside on an edge case or maintainability boundary.
- **P3:** narrow, low-impact issue worth correcting at the user's discretion.

**Complete when:** every reported finding is introduced, accurately located, consequence-backed, actionable, non-duplicative, and severity-calibrated.

## 5. Deliver the Review

Put findings first, ordered by severity. For each finding provide:

```markdown
[P1] Short outcome-focused title — path/to/file:line
Condition and consequence. Evidence. Recommended response. Confidence: high|medium|low.
```

Keep each finding concise while preserving the evidence needed to act. If there are no findings, state `No actionable findings.` explicitly.

After the findings, report:

- reviewed scope and comparison point;
- verification actually run and its result;
- testing gaps and residual risks;
- relevant pre-existing issues;
- unavailable or degraded coverage; and
- one verdict: **No blocking findings**, **Changes requested**, or **Review incomplete**.

Use **Changes requested** when a proven finding should be addressed before the next stage. Use **Review incomplete** when missing scope or evidence prevents a trustworthy assessment. A clean review means no proven defects were found within the stated coverage; it is not proof that none exist.

Stop after the report. Route accepted fixes through a separately authorized implementation workflow such as `$ns-work`.

**Complete when:** the report stands alone, every conclusion is supported by fresh evidence, and the user can decide what to address without relying on earlier commentary.
