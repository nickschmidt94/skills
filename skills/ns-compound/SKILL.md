---
name: ns-compound
disable-model-invocation: true
description: "Use after a completed task when the user asks to preserve feedback, compound a correction, or decide whether one durable repository standard, repository learning, or reusable skill improvement is worth keeping. No capture is a valid outcome. Do not use for source-code changes, memory updates, or publication."
metadata:
  version: "1.0.1"
---

# NS Compound

Judge whether completed work earned a durable future-facing change. Capturing nothing is a complete outcome.

Use four standards throughout:

- **Qualified** — evidence-backed, behavior-changing, and worth more than its retrieval and maintenance cost.
- **Singular** — one coherent learning and one primary destination per invocation.
- **Placed** — stored where a future agent will encounter it at the decision point.
- **Lean** — the change replaces, sharpens, or removes weak guidance before adding more.

A user request to preserve or compound the completed run authorizes one local capture only after qualification: one active repository standard, one repository learning document, or one targeted improvement to one user-owned or workspace skill. Do not run automatically merely because a task completed. It does not authorize source-code changes, memory updates, unrelated documentation edits, git publication, or external actions. Preserve pre-existing changes.

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

- **Repository standard** — an evidence-backed judgment rule should constrain future implementation, test design, or review throughout this repository, but the failure is not fully mechanically detectable.
- **Repository learning** — the truth is specific to a codebase: a solved engineering problem, settled technical decision, proven repository pattern, or non-obvious operational constraint.
- **Skill improvement** — the run exposed a durable issue in a skill's trigger, instruction, sequence, completion criterion, reference, or script that could affect future uses across tasks or repositories.
- **Wrong home** — the needed change belongs in product code, ordinary documentation, the active domain glossary, an ADR, an automation, a user preference store, memory, an upstream package, or another system outside this skill's authority.

Route a canonical domain term or relationship to the repository's established terminology owner, such as a glossary, domain model, or context file. Use `CONTEXT-MAP.md` and `CONTEXT.md` only when repository evidence establishes that convention. Route a hard-to-reverse, surprising choice produced by a real trade-off to the repository's established decision-record owner, such as an ADR, RFC, design document, or decision log; use an ADR only when repository evidence establishes that convention. When no terminology or decision-record owner exists, identify the missing ordinary documentation destination without creating it under this skill. Identify each destination without mutating it under this skill.

Route to **Wrong home** when executable enforcement fully captures the learning’s future value; name the exact owner—verifier, lint rule, type, schema, or test—and do not mutate source code under this skill. Detectability alone does not exclude investigation context that independently passes the Value gate. Keep standards and learnings distinct: the standard is the compact active rule; an evidence-rich learning is justified only when its investigation or decision context has separate retrieval value. One invocation never writes both.

Prefer the skill branch only when changing the skill would have changed the run. Prefer the repository branch when the lesson would be wrong or noisy outside that repository. If both could benefit, select the upstream cause that prevents recurrence; capture the other only in a separate invocation. Ask the user only when the destinations are equally plausible and would produce materially different changes.

**Complete when:** the qualified outcome has one justified destination and no second mutation is bundled into the run.

## 3. Compound

### Repository standard

Read and follow [references/repository-standard.md](references/repository-standard.md). Load it only for this branch.

### Repository learning

Read and follow [references/repository-learning.md](references/repository-learning.md). Load it only for this branch.

### Skill improvement

Resolve the exact target skill from the request and current run. Before judging or editing it, use `$writing-for-agents` when available, including its skill-mechanics reference. When it is unavailable, continue with the direct Lean and validation standards below and report the missing companion in validation. Then follow `$skill-retrospective` when available. If the retrospective skill is unavailable, apply its equivalent loop directly: reconstruct the run evidence, classify the lesson, pass the improvement gate, make the smallest targeted edit, and validate the complete changed surface.

Use the **Lean test** while applying that workflow:

1. Remove stale or counterproductive guidance when that fully fixes the issue.
2. Replace or sharpen the instruction nearest the failed decision point.
3. Move branch-only detail behind an existing or justified context pointer.
4. Add new prose only when the first three treatments cannot express the learning.

Keep one meaning in one place. Do not append a lessons-learned section, transcript detail, or a rule that merely restates capable-agent defaults. Add a script only for demonstrated repeated deterministic work. If the target is a system-managed, plugin-cache, or otherwise externally owned skill, leave it unchanged and report the source-owned patch that would be needed.

Before final validation of a user-owned local skill, record the change with [scripts/record_skill_update.py](scripts/record_skill_update.py), resolving the script relative to this skill directory. Choose `patch` for a correction or refinement, `minor` for a backward-compatible capability, and `major` only for an incompatible behavioral change. An unversioned skill starts at `1.0.0`; otherwise the script bumps `metadata.version` and prepends one concise entry to that skill's `CHANGELOG.md`. This local record is part of completing the skill improvement, requires no publication, and must describe the behavior change rather than the editing process. Do not version externally owned or plugin-cache skills.

Validate the edited and locally versioned skill with the active skill validator when available. Re-read the complete changed surface, including frontmatter, changelog, routing pointers, relevant references, scripts, UI metadata, and invocation policy. A valid file is not sufficient: the change must be likely to alter the future decision that failed.

**Complete when:** one target skill is minimally improved, validated, and locally versioned when eligible, or the evidence supports `no capture` or `wrong home` without mutation.

## 4. Deliver

Report:

- `Decision: standard captured | standard updated | learning captured | learning updated | skill updated | no capture | wrong home | needs user input`;
- the qualified learning, or the first Value-gate condition that failed;
- the selected destination and exact changed path, or why nothing changed;
- evidence and validation actually used; and
- the recorded local skill version when a skill was updated; and
- any remaining uncertainty or separately useful follow-up.

Keep the report short. The compounding value is the future behavior change, not the ceremony around recording it.
