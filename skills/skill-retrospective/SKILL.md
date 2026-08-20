---
name: skill-retrospective
description: Reviews a just-finished skill run and improves the source skill when the run exposed a durable, generalizable lesson. Use after running another skill when a correction, failure, or repeated workaround suggests the skill itself should improve.
---

# Skill Retrospective

Use this as an after-action pass for another skill. Decide whether the run revealed a durable improvement and, when it did, make the smallest useful edit.

Before judging or editing the target, read `$writing-for-agents` completely, including its skill-mechanics reference. When that companion is unavailable, apply its equivalent standards directly: protect the information hierarchy, sharpen context pointers and completion criteria, keep one meaning in one place, and prune before adding. Report the unavailable companion in validation.

## Quick Start

Identify the target skill, read its `SKILL.md`, reconstruct what happened in the run, then choose `updated`, `no change`, or `needs user input`. Patch the target only when the lesson is concrete, reusable, and belongs in that skill.

Example prompt: `run skill-retrospective on tradingwebsite-report-qa for the last run`.

## Operating Mode

Treat the previous run as evidence. Prefer concrete changes to `SKILL.md`, reference files, or bundled scripts over vague "remember this" notes. If the lesson is one-off, context-specific, or better handled in the project itself, leave the skill unchanged and say why.

Do not update Codex memory, user profile memory, or unrelated skills unless the user explicitly asks. Skill edits are local tool improvements, not personal memory updates.

## Workflow

1. Resolve the target skill.
   - Use the skill name or path the user gave.
   - If the user only says "that skill" or "the one we just used", infer from the current conversation when there is only one plausible target.
   - If more than one skill could be the target, ask one short clarifying question before editing.
   - Check likely personal, shared, and workspace skill roots.
   - Completion criterion: you can name the target skill and exact file path.

2. Read the target skill before judging it.
   - Read the target `SKILL.md` completely.
   - Read linked references only when the observed issue touches that reference.
   - Notice the skill's trigger, workflow, completion criteria, bundled scripts, and explicit constraints.
   - Completion criterion: you can point to the section that should absorb the lesson, or explain why no section should change.

3. Reconstruct the run evidence.
   - Capture the original ask, instructions used, important outputs or errors, user corrections, final result, and repeated workarounds.
   - Use concrete evidence that would help the next run behave better.
   - If the current thread lacks enough evidence, ask for the missing run summary rather than inventing a lesson.
   - Completion criterion: you have a concise evidence summary, even if it remains in working notes.

4. Classify the lesson.
   - **Skill bug:** instructions were misleading, stale, vague, too strict, missing a prerequisite, or missing a completion check.
   - **Trigger bug:** the skill should have been used but did not trigger, or triggered for a near miss.
   - **Reusable procedure:** future runs keep needing the same deterministic script, checklist, or reference.
   - **Stable preference:** a recurring preference belongs in this skill's domain.
   - **One-off:** the lesson depends on transient state or task-specific detail.
   - **Wrong home:** the fix belongs in project code, documentation, automation, another skill, or an upstream report.
   - Completion criterion: choose exactly one primary classification before editing.

5. Apply the edit only when it passes the improvement gate.
   Edit only when the lesson is evidenced, likely to recur, actionable, compatible with the skill's purpose, and small enough to explain clearly.

   When editing:
   - Preserve the skill name unless the user asked for a rename.
   - Keep the change near the decision it affects.
   - Prefer removing, replacing, or sharpening guidance over adding broad warnings.
   - Use progressive disclosure for branch-only detail and keep each meaning in one authoritative place.
   - Remove or soften instructions that caused waste or overfitting.
   - Add a bundled script only for repeated deterministic work.
   - Keep private values, transcripts, stale dates, and sensitive operational details out of the skill.

6. Validate the result.
   - Re-read the complete changed surface and frontmatter.
   - Confirm the description still states what the skill does and when to use it.
   - Run the active skill validator and a lightweight visibility check when available.
   - Note when a restart may be needed before the update surfaces in a fresh session.

## Output

Report:

```markdown
Decision: updated | no change | needs user input
Target: <skill name and path>
Lesson: <one-sentence general lesson, or why there is no durable lesson>
Changed: <files or sections changed, or "none">
Validation: <checks run and discoverability note>
```

Keep the explanation short. The user asked for a learning loop, not a ceremony.
