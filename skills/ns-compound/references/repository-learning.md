# Repository learning branch

Use this branch only for one qualified learning whose truth belongs to a repository.

This branch authorizes creating or updating one repository-local learning document and its required parent directory. When a repository first adopts a learning store or changes its path, it may propose one setup pointer in the active repository instructions. Apply that instruction-file edit only after the user explicitly approves the exact change.

## Ground

Inspect the smallest current source set that supports the learning:

- applicable repository instructions and documentation conventions;
- affected implementation, configuration, tests, or operational evidence;
- the owned change and fresh verification that established the outcome; and
- relevant history only when current files cannot reveal a failed approach, constraint, or decision.

Use repository evidence for present behavior and the conversation or available memory as supplementary context. Mark removed behavior and superseded approaches as historical. Do not turn local verification into claims of commit, push, merge, deployment, publication, or production state.

For every load-bearing claim, locate evidence or rewrite it as bounded context. The branch is grounded when every central claim is verified, explicitly historical, attributed with uncertainty, or removed.

## Reconcile

Inspect the live repository for its established learning store, naming convention, metadata, taxonomy, and terminology. Search existing learnings by area, symptom, root cause, decision, pattern, and likely tags before choosing a destination.

- **Same learning:** update the existing document in place.
- **Related learning:** create a distinct document and add a useful relationship link in the new document.
- **No related learning:** create a distinct document normally.

Follow the established location. If none exists, use `docs/learnings/<descriptive-slug>.md`. Use a stable descriptive slug without a date and keep the destination inside the repository.

Run discoverability setup only when creating a store, adopting a store that active repository instructions do not surface, or changing the established path. Propose the smallest pointer that names the concrete repo-relative store, describes it as verified problems, technical decisions, and proven patterns, and tells agents when to search it. A fallback is:

```markdown
`docs/learnings/` contains verified repository learnings—solved problems, technical decisions, and proven patterns. Search it by area and tags before related planning, implementation, debugging, or review.
```

Record the exact file, placement, and text, but leave repository instructions unchanged until the learning validates and the user explicitly approves the pointer. When no substantive instruction file exists, propose a minimal root `AGENTS.md`.

This stage is complete when corpus search supports the create-or-update decision, the target path is known, and any setup need is one exact pending proposal.

## Write

Match a stable existing corpus format. Otherwise begin with:

```markdown
---
date: YYYY-MM-DD
kind: problem
area: repository-specific-area
tags:
  - relevant-term
---

# Descriptive learning title
```

Classify the learning as one of these shapes and include only sections carrying material information:

- **Problem:** Problem, Evidence, Investigation, Resolution, Why It Works, Verification, Prevention.
- **Decision:** Context, Decision, Alternatives, Rationale, Consequences, When It Applies.
- **Pattern:** Context, Pattern, Evidence, Examples, Boundaries, When It Applies.

Preserve failed approaches only when they prevent a likely repeated dead end. Prefer repository-relative references over duplicated implementation. Write for a future agent with no access to the conversation: preserve the reusable insight and evidence, not the session narrative.

## Validate

Re-read the complete document against its evidence. Confirm that:

- current and historical claims are correctly framed;
- paths and links resolve or are intentionally historical;
- commands and excerpts preserve the semantics the learning depends on;
- metadata follows the corpus convention and parses;
- title, area, tags, and terminology support retrieval; and
- no placeholder, scaffold, unsupported certainty, duplicate explanation, or session-only reference remains.

Run a configured repository documentation check when one applies. Correct contradictions, narrow unsupported claims, and remove the draft when its central learning cannot be supported.

After validation, show any pending instruction pointer with its exact file, placement, and text. Apply it only with specific approval, then re-read the instruction file.

The branch is complete when the standalone learning is findable and evidence-backed, applicable checks are green or classified, and any discoverability setup is verified or reported as an unapproved proposal.

## Branch report

Report the learning, whether the document was created or updated, its repository-relative path, evidence and verification, related links, any discoverability setup, and remaining uncertainty. Stop without broader documentation maintenance or publication.
