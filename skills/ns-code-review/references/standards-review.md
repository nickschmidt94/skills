# Standards Review

Use this branch only for the independently reported Standards axis.

## Inputs

Require the pinned comparison point, commit list when present, complete diff including in-scope untracked files, the exact applicable standards sources, and relevant authoritative verifier results classified as introduced, pre-existing, or unrelated. Sources may include repository `AGENTS.md`, root `CODING_STANDARDS.md`, relevant contribution rules, and focused subsystem contracts. Historical audits, superseded plans, and generic preference are not standards.

## Review

Read the supplied standards before judging the diff. Report a hard finding only when the reviewed change introduces a concrete breach and cite the exact rule ID or governing passage. Repository rules override generic heuristics. Label any useful uncodified concern as a judgment call rather than a standards failure.

Treat an introduced standards failure from authoritative lint, typecheck, compiler, schema, or a focused verifier as Standards-axis evidence. Do not restate its diagnostic as an independent candidate; return `Standards: fail (authoritative tool finding)` with the tool name and governing rule or changed location when the output supplies one. The parent reports the authoritative diagnostic once and reflects it in the operational verdict. Pre-existing or unrelated verifier failures do not fail the axis. Do not infer a process-only violation from final code shape; require commits, traces, or supplied implementation evidence.

When repository standards do not decide a concern, use this heuristic baseline only to focus investigation:

- duplicated policy or shotgun changes that create a concrete drift path;
- feature envy or leaky ownership that couples a change to another module's internals;
- primitive or flag-heavy interfaces that permit invalid states on the changed path;
- deep conditional or temporal coupling that creates an evidenced lifecycle risk; and
- speculative abstractions or pass-through layers that add a concrete testability or maintenance boundary without present behavior.

These are prompts for evidence, never hard laws. Report a useful uncodified concern as a separate non-blocking `Judgment call`, name its concrete consequence, and keep the Standards axis passing unless Correctness or Spec independently proves a failure. Let any repository rule or deliberate local pattern override it.

Review directly. Do not invoke `ns-code-review` and do not spawn another agent.

## Output

Return `Standards: pass`, `Standards: unavailable`, `Standards: fail (authoritative tool finding)`, or concise candidates with exact citations, changed locations, triggering conditions, and consequences. The parent will independently prove and classify every candidate while reporting authoritative diagnostics only once.
