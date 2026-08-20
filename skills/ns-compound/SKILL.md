---
name: ns-compound
description: "Assess completed work for a durable learning worth preserving, then either capture one repository learning or improve one reusable skill. Invoke explicitly after a task when the user wants a compounding judgment; no capture is a valid outcome."
disable-model-invocation: true
---

# NS Compound

Judge whether completed work earned a durable future-facing change. Capturing nothing is a complete outcome.

Use four standards throughout:

- **Qualified** — evidence-backed, behavior-changing, and worth more than its retrieval and maintenance cost.
- **Singular** — one coherent learning and one primary destination per invocation.
- **Placed** — stored where a future agent will encounter it at the decision point.
- **Lean** — the change replaces, sharpens, or removes weak guidance before adding more.

Invoking this skill authorizes one local capture only after qualification: one repository learning document, or one targeted improvement to one user-owned or workspace skill. It does not authorize source-code changes, memory updates, unrelated documentation edits, git publication, or external actions. Preserve pre-existing changes.

## 1. Assess

Begin with an observed delta from the completed run:

- a user correction;
- a failed assumption with a verified resolution;
- a settled decision with durable rationale;
- a proven pattern; or
- a repeated workaround that reveals a reusable mechanism problem.

When the run contains no observed delta, finish with `no capture`. Difficulty, novelty, or time spent matters only when it creates future decision value.

Apply the **Value gate**. Capture only when all five conditions hold:

1. supported by current evidence from the run;
2. likely to remain true and recur in a plausible future task;
3. able to change a specific future decision or behavior;
4. not already cheap to recover from current code, tests, documentation, or existing learnings; and
5. expected to save more future effort or error than the new guidance will cost to retrieve, maintain, and keep current.

The burden of proof is on capture. A one-off outage, transient state, vague preference, unverified hunch, or already-discoverable fact completes this step as `no capture` with no file changes.

**Complete when:** either a qualified candidate names its evidence, plausible future task, changed behavior, and retrieval gap, or `no capture` names the first Value-gate condition that failed. Both outcomes complete the skill successfully.

## 2. Place

Choose exactly one primary home:

- **Repository learning** — the truth is specific to a codebase: a solved engineering problem, settled technical decision, proven repository pattern, or non-obvious operational constraint.
- **Skill improvement** — the run exposed a durable issue in a skill's trigger, instruction, sequence, completion criterion, reference, or script that could affect future uses across tasks or repositories.
- **Wrong home** — the needed change belongs in product code, ordinary documentation, an automation, a user preference store, memory, an upstream package, or another system outside this skill's authority.

Prefer the skill branch only when changing the skill would have changed the run. Prefer the repository branch when the lesson would be wrong or noisy outside that repository. If both could benefit, select the upstream cause that prevents recurrence; capture the other only in a separate invocation. Ask the user only when the destinations are equally plausible and would produce materially different changes.

**Complete when:** the learning has one justified destination and no second mutation is bundled into the run.

## 3. Compound

### Repository learning

Read and follow [references/repository-learning.md](references/repository-learning.md). Load it only for this branch.

### Skill improvement

Resolve the exact target skill from the request and current run. Before judging or editing it, read `$writing-for-agents` completely, including its skill-mechanics reference, then follow `$skill-retrospective` when available. If the retrospective skill is unavailable, apply its equivalent loop directly: reconstruct the run evidence, classify the lesson, pass the improvement gate, make the smallest targeted edit, and validate the complete changed surface.

Use the **Lean test** while applying that workflow:

1. Remove stale or counterproductive guidance when that fully fixes the issue.
2. Replace or sharpen the instruction nearest the failed decision point.
3. Move branch-only detail behind an existing or justified context pointer.
4. Add new prose only when the first three treatments cannot express the learning.

Keep one meaning in one place. Do not append a lessons-learned section, transcript detail, or a rule that merely restates capable-agent defaults. Add a script only for demonstrated repeated deterministic work. If the target is a system-managed, plugin-cache, or otherwise externally owned skill, leave it unchanged and report the source-owned patch that would be needed.

Validate the edited skill with the active skill validator when available. Re-read the complete changed surface, including frontmatter, routing pointers, relevant references, scripts, UI metadata, and invocation policy. A valid file is not sufficient: the change must be likely to alter the future decision that failed.

**Complete when:** one target skill is minimally improved and validated, or the evidence supports `no change` or `wrong home` without mutation.

## 4. Deliver

Report:

- `Decision: captured | updated | no capture | wrong home | needs user input`;
- the qualified learning, or the first Value-gate condition that failed;
- the selected destination and exact changed path, or why nothing changed;
- evidence and validation actually used; and
- any remaining uncertainty or separately useful follow-up.

Keep the report short. The compounding value is the future behavior change, not the ceremony around recording it.
