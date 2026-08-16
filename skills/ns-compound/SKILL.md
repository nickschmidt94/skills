---
name: ns-compound
description: Capture one earned repository learning from a solved engineering problem, settled technical decision, or proven pattern. Invoke explicitly after work when the learning should be preserved for future engineering.
---

# NS Compound

Preserve one durable learning that will make similar future work easier.

Use four standards throughout:

- **Earned** — verified, reusable, non-obvious, and cheaper to retrieve than rediscover.
- **Singular** — one coherent problem, decision, or pattern per invocation.
- **Grounded** — factual claims match current evidence or are clearly marked as historical.
- **Findable** — location, title, metadata, terminology, and links support later retrieval.

This skill authorizes creating or updating one repository-local learning document and its required parent directory. When a repository first adopts a learning store or changes its path, the skill may propose one setup pointer in the active repository instructions. Apply that instruction-file edit only after the user explicitly approves the exact change; invoking this skill alone is not that approval. Keep source code, glossaries, other learning documents, git state, and external systems unchanged unless the user separately authorizes that work.

## 1. Qualify

Resolve the target repository and the candidate learning from the request and current conversation. Classify it as one of three branches:

- **Problem:** a diagnosed failure with a verified resolution.
- **Decision:** a settled technical choice with durable rationale or consequences.
- **Pattern:** a repeatedly useful approach supported by working evidence.

Apply the Earned test. Preserve the learning only when all four conditions hold:

1. The outcome is solved, settled, or proven.
2. Current evidence supports it.
3. It could materially improve later work.
4. The important insight is not obvious from reading one current source file.

When several distinct learnings qualify, use the one named by the user or ask which one to capture. When none qualifies, report why documentation was skipped and leave the repository unchanged.

**Complete when:** exactly one problem, decision, or pattern passes every Earned condition, or the run has ended without writing.

## 2. Ground

Inspect the smallest current source set that can support the learning:

- applicable repository instructions and existing documentation conventions;
- the affected implementation, configuration, tests, or operational evidence;
- the owned change and fresh verification that established the outcome; and
- relevant history only when it explains a failed approach, constraint, or decision that current files cannot reveal.

Use current repository evidence for present behavior. Use the conversation and available memory as supplementary context. Mark pre-fix behavior, removed paths, and superseded approaches as historical. Include lifecycle or publication state only when it matters to the learning and can be verified from its authoritative source.

For every load-bearing claim, locate supporting evidence or rewrite it as bounded context rather than fact. A verified local outcome may be documented without claiming that it has been committed, pushed, merged, deployed, or published.

**Complete when:** every load-bearing claim is verified, explicitly historical, bounded by attributed uncertainty, or removed, and the evidence proves the learning's outcome.

## 3. Reconcile

Inspect the live repository for an established learning store, naming convention, metadata shape, taxonomy, and terminology. Search existing learnings by the affected area, symptoms, root cause, decision, pattern, and likely tags before choosing a destination.

Choose the target by overlap:

- **Same learning:** update the existing document, preserving its path and established metadata shape.
- **Related learning:** create a distinct document and add a useful relationship link in the new document.
- **No related learning:** create a distinct document normally.

Follow the repository's established location. If none exists, use `docs/learnings/<descriptive-slug>.md`. Choose a stable descriptive slug without a date; metadata records when the learning was captured. Keep every destination inside the repository.

Run discoverability setup only when creating a learning store, adopting an existing store that active repository instructions do not yet surface, or changing the store's established path. Once the instructions surface the unchanged concrete path, later runs skip this setup branch entirely.

For setup, use the active substantive repository instruction file. The pointer must name the concrete repo-relative store path, describe it as verified problems, technical decisions, and proven patterns, and tell agents to search it before related planning, implementation, debugging, or review. Draft the smallest addition that fits the file's existing structure and voice. A suitable fallback shape is:

```markdown
`docs/learnings/` contains verified repository learnings—solved problems, technical decisions, and proven patterns. Search it by area and tags before related planning, implementation, debugging, or review.
```

Record the exact file, placement, and proposed text, but leave repository instructions unchanged until the learning passes Step 5. When no repository instruction file exists, prepare a minimal repo-root `AGENTS.md` proposal containing the pointer.

**Complete when:** the create-or-update decision is supported by a corpus search, the exact target path is known, no known document already owns the same learning under another path, and the setup branch is either unnecessary or represented by one exact pending proposal.

## 4. Write

Match the existing corpus when it has a stable format. Otherwise begin with:

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

Use the branch-specific structure that fits the learning:

- **Problem:** Problem, Evidence, Investigation, Resolution, Why It Works, Verification, Prevention.
- **Decision:** Context, Decision, Alternatives, Rationale, Consequences, When It Applies.
- **Pattern:** Context, Pattern, Evidence, Examples, Boundaries, When It Applies.

Include only sections carrying material information. Preserve failed approaches when they prevent a likely repeated dead end. Use concise code or command excerpts only when the learning depends on their exact shape; prefer repository-relative references to duplicating discoverable implementation. Add related links when they materially improve navigation.

Write for a future agent with no access to this conversation. Explain the reusable insight and the evidence needed to trust it rather than narrating the work session.

**Complete when:** the document stands alone, preserves one learning, follows the repository's corpus or the default format, and contains no empty, duplicated, or ceremonial sections.

## 5. Validate

Re-read the complete document against its evidence. Check every factual behavior, path, command, code excerpt, internal link, historical statement, and countable assertion. Confirm that:

- current claims still match the working tree and verification evidence;
- historical claims are recognizable as historical;
- paths and links resolve or are intentionally described as removed;
- excerpts preserve the semantics required by the learning;
- metadata parses and follows the chosen corpus convention;
- the title and terminology make the document discoverable; and
- no placeholder, drafting scaffold, unsupported certainty, or session-only reference remains.

Run a configured repository documentation check when one exists and applies. Correct contradictions from authoritative evidence. Soften or remove claims that cannot be verified without weakening the central learning; if the central learning itself cannot be supported, remove the draft and report that capture was skipped.

After the learning passes every check, resolve any pending one-time discoverability proposal from Step 3. Show the exact file, placement, and text, then request explicit consent before editing. Prior authorization counts only when the user specifically authorized adding the missing pointer. If approved, make one targeted edit and reread the instruction file to verify the pointer and preserve surrounding content. If consent is declined or unavailable, preserve the instructions and report the proposal.

**Complete when:** every check above passes, applicable documentation verification is green or classified, the final document contains no unsupported load-bearing claim, and any pending setup is either verified or reported without an unapproved edit.

## 6. Deliver

Report:

- the learning captured;
- whether the document was created or updated;
- its repository-relative path;
- the evidence and verification used;
- related material linked from the document;
- one-time discoverability setup performed or proposed, when that branch ran; and
- remaining uncertainty or unavailable checks.

Stop with the validated learning document and, when approved, its single discoverability pointer. Leave broader documentation maintenance and publication to separately authorized work.

**Complete when:** a future agent can find, understand, trust, and apply the learning without the original conversation, and the user can identify exactly what changed from the delivery report.
