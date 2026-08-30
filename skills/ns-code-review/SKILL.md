---
name: ns-code-review
description: Review a local change, branch, commit range, or pull request for introduced defects and regression risk, repair proven local findings, and independently re-review until clean or blocked. Use before committing, publishing, or advancing a verified change; request report-only mode when no edits are wanted.
---

# NS Code Review

Review a change, repair proven introduced defects, and re-review the complete change until it is locally clean or genuinely blocked. Produce a self-contained final report that distinguishes repaired findings from testing gaps, pre-existing issues, and unresolved uncertainty.

Use four standards throughout:

- **Scope** — identify the exact change, intent, and comparison point.
- **Introduced** — make the reviewed change responsible only for problems it creates or requirements it fails to implement.
- **Proven** — verify each finding against the surrounding system rather than inferring it from an isolated hunk.
- **Closed-loop** — repair decision-complete findings and prove the updated change with a fresh review.

Operate in local repair mode by default. Invocation authorizes local implementation and verification only for proven, decision-complete findings introduced by the reviewed change. Preserve pre-existing work. Commits, pushes, pull requests, deployment, publication, and external actions require separately authorized workflows.

When the user explicitly requests `report-only`, `review only`, or no modifications, preserve the checkout and deliver the review without remediation.

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

Establish **evidence coverage** from the shape of the change. For every material failure mode the change introduces, identify and run an authoritative check that can expose it. Behavioral tests do not substitute for structural checks such as compilation, loading, linking, parsing, schema validation, packaging, or generation when they do not exercise those paths. Choose checks by failure mode regardless of whether the changed artifacts are production code, tests, scripts, configuration, or documentation.

For an explicitly requested deep or independent review, or a change that crosses a material trust boundary such as authorization, payments, persistence, destructive operations, concurrency, or a public contract, dispatch one independent in-platform reviewer with the exact scope and relevant risk lens. Give it the diff and task-local context, collect it before synthesis, and verify its findings normally. If independent review is unavailable, continue and disclose the missing coverage.

**Complete when:** every changed behavior and material structural failure mode has authoritative evidence or is explicitly unresolved, each material risk lens was applied or found irrelevant, and any required independent pass has returned or its absence is recorded.

## 4. Prove the Findings

For every candidate finding:

1. Read the cited code and enough surrounding control flow to rule out handling elsewhere.
2. Confirm the reviewed change introduced the defect or omitted an accepted requirement.
3. Identify the triggering condition and concrete consequence.
4. Verify the exact file and line against the reviewed revision.
5. Run focused tests or checks when they can materially confirm or refute the claim.
6. State the smallest credible response and the remaining confidence.

Discard speculative findings, stylistic preferences, and duplicates of authoritative automated output. Classify missing or unavailable verification by evidence coverage: report it as a testing gap only when the remaining evidence supports a trustworthy verdict; otherwise return **Review incomplete**. Mention a pre-existing issue separately only when it affects the reviewed change, blocks verification, or materially changes the verdict.

Calibrate severity:

- **P0:** exploitable breakage, data loss, or critical system failure.
- **P1:** high-impact defect likely on a normal path or a broken contract.
- **P2:** real moderate downside on an edge case or maintainability boundary.
- **P3:** narrow, low-impact issue worth correcting at the user's discretion.

**Complete when:** every reported finding is introduced, accurately located, consequence-backed, actionable, non-duplicative, and severity-calibrated.

## 5. Close the Loop

When there are no actionable findings, proceed to delivery.

In explicit report-only mode, preserve the working tree and proceed to delivery with the findings unresolved.

Otherwise, route the proven findings through `$ns-work` when available. When it is not installed, apply the equivalent local implementation loop directly: preserve the baseline, implement only the proven responses, verify them, and inspect the owned diff.

Use one decision-complete remediation scope:

1. Preserve the original comparison point and recorded repository baseline.
2. Implement only the smallest credible responses established while proving the findings.
3. Run focused verification for each repaired failure mode and broader checks proportional to the integrated change.
4. Inspect the complete updated change, including untracked files, against the original comparison point.
5. Start a fresh review of that complete change. Use a new independent in-platform reviewer when available so the fixer does not grade its own work.

Repeat remediation and fresh review while new or surviving actionable findings remain. Stop and deliver the unresolved finding as a blocker when:

- remediation requires an unapproved product, architecture, data, authorization, or destructive decision;
- authoritative verification cannot be restored within scope;
- an external action or unavailable dependency is required; or
- the same finding survives two remediation attempts.

Keep remediation scoped to introduced, proven findings. Leave pre-existing issues, unrelated failures, speculative concerns, and preference-driven cleanup unchanged.

**Complete when:** a fresh review finds no actionable findings, explicit report-only mode applies, or a specific blocker prevents safe local completion.

## 6. Deliver the Review

When the loop repaired findings, report those first, ordered by severity:

```markdown
[P1] Short outcome-focused title — fixed
Original condition and consequence. Response applied. Verification proving the repair.
```

For report-only or blocked findings, use the original finding format:

```markdown
[P1] Short outcome-focused title — path/to/file:line
Condition and consequence. Evidence. Recommended response. Confidence: high|medium|low.
```

Keep each item concise while preserving the evidence needed to evaluate it. State `No actionable findings remain.` after a clean final review.

After the findings, report:

- reviewed scope and comparison point;
- verification actually run and its result;
- testing gaps and residual risks;
- relevant pre-existing issues;
- unavailable or degraded coverage; and
- one final verdict: **No blocking findings**, **Changes requested**, or **Review incomplete**.

Use **No blocking findings** when the fresh final review is clean. Use **Changes requested** when report-only mode or a decision blocker leaves a proven finding unresolved. Use **Review incomplete** when missing scope or evidence prevents a trustworthy assessment. A clean review means no proven defects were found within the stated coverage; it is not proof that none exist.

**Complete when:** the report stands alone, every repair and conclusion is supported by fresh evidence, and the user can advance the locally reviewed change without another mechanical handoff.
