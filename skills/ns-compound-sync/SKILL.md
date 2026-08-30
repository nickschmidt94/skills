---
name: ns-compound-sync
description: Invoke explicitly with a standards file, stable rule locator, learning path, area, keyword, or repository-wide scope when existing repository standards or learnings may be stale, contradictory, overlapping, superseded, automated, or broken by codebase change. Do not use to capture new guidance or change source code.
disable-model-invocation: true
---

# NS Compound Sync

Keep repository standards and learnings accurate, distinct, and trustworthy as the codebase evolves.

Use four standards throughout:

- **Current** — present-tense claims match authoritative repository evidence.
- **Distinct** — each rule or document earns separate retrieval value.
- **Conservative** — uncertainty narrows claims or marks them stale; it never invents current guidance.
- **Complete** — every in-scope rule or document receives an evidence-backed outcome.

This skill authorizes local maintenance inside the repository's existing standards file, conventionally `CODING_STANDARDS.md`, or learning store, normally `docs/learnings/`. It may update rules or documents and apply a visible stale marker. Consolidation, replacement, and deletion require the user's approval of the exact proposed action. Preserve source code, repository instructions, glossaries, unrelated documentation, git state, and external systems. Capture new guidance through a separate explicit Value-gated, single-destination workflow; use `$ns-compound` when available. Publish authorized owned changes through a separate verified commit, non-force push, and pull-request workflow; use `$ns-ship-pr` when available.

## 1. Scope

Resolve the repository and requested corpus from the request and current tree. Follow established repository locations for standards and learnings; conventionally inspect root `CODING_STANDARDS.md` and `docs/learnings/`. If the requested corpus does not exist, report that a separate explicit capture workflow should establish it only after a candidate passes a Value gate; use `$ns-compound` when available, and stop this sync run.

Resolve candidates using the narrowest supplied scope:

1. exact standards file, stable rule locator, learning path, or filename;
2. directory or area;
3. frontmatter field or tag;
4. module, component, or content keyword; or
5. the entire standards-and-learning corpus when the user explicitly requests a repository-wide sync.

For standards, use the repository's stable rule locator: its rule ID when present, otherwise its exact heading, section path, or another unambiguous repository-native identifier. When the selected scope is a multi-rule standards file, expand it into one candidate per identifiable rule by default. Treat the entire standards file as one mutation candidate only when the user explicitly requests file-wide treatment and the action packet names the file plus every affected stable rule locator. A file path alone does not authorize file-wide mutation.

When no scope is supplied, inventory the available corpus without editing, group rules and documents by area, identify the highest-value maintenance scope using visible drift, overlap, or contradiction signals, and ask whether to proceed with that scope. When a supplied scope matches nothing, report the miss without widening it.

Record repository status and preserve all pre-existing changes. Exclude catalog or index files from classification, but maintain their links when an approved action changes a listed document.

**Complete when:** the repository, existing corpus, exact candidate set, requested breadth, and pre-existing changes are explicit, or the run has ended without mutation because no valid scope exists.

## 2. Ground

Read every candidate rule or document and the smallest current source set needed to test its load-bearing claims: referenced implementation, configuration, tests, contracts, related standards or learnings, and repository history only when current files cannot explain a transition.

Check independently for:

- missing or renamed paths, symbols, commands, and links;
- snippets or procedures that no longer match current behavior;
- claims contradicted by current code or configured workflows;
- overlap, supersession, or contradiction among candidates; and
- historical or operational claims the repository cannot currently witness.

For a standard, also determine whether executable enforcement now fully owns the rule, whether its exception or rationale still adds value, and whether another active rule duplicates or contradicts it. For a learning, preserve evidence-rich investigation or decision context that has separate retrieval value. Do not collapse the two corpus roles.

Match documentation to repository reality; source-code changes are outside this skill. Treat missing evidence as a verification gap, not proof that a plausible claim is false. Mark removed behavior and obsolete paths as historical when they remain useful to the learning.

For each candidate, record the claims tested, supporting or contradicting evidence, verification gaps, inbound standards or learning links, and any relationship to another candidate.

**Complete when:** every candidate's load-bearing claims and relationships have been checked against the best available evidence, and every uncertainty is distinguished from a contradiction.

## 3. Classify

Assign exactly one outcome to every candidate:

- **Keep** — accurate, useful, and separately findable; leave unchanged.
- **Update** — the rule or learning remains correct but factual references, snippets, links, metadata, scope, or historical framing drifted; repair in place.
- **Stale** — current guidance cannot be trusted and the available evidence cannot support a replacement; add the corpus's established stale marker. For one rule in a multi-rule standards file, use an established rule-local marker or add a concise status and reason inside that rule's own block; never mark the whole file stale. When the file structure cannot localize the marker unambiguously, propose the exact scope and ask before widening it. For a learning document, add `status: stale`, a concise `stale_reason`, and `stale_date: YYYY-MM-DD` to YAML frontmatter, or a clear top-of-document stale notice when frontmatter is absent.
- **Consolidate** — rules or documents substantially duplicate the same guidance and one canonical destination can retain every unique, useful point; propose merging and removing the subsumed material.
- **Replace** — the recommended approach is misleading and current evidence can support a trustworthy successor; propose the successor's scope and disposition of the old document.
- **Delete** — the rule or learning is wholly redundant or both its implementation and problem domain are gone; propose removal.

Use these boundaries:

- A changed recommendation is Replace, not Update.
- Age, cosmetic quality, or a missing referenced file alone does not establish staleness.
- Shared code does not establish duplication; the candidates must address the same retrievable rule, problem, decision, or pattern.
- Consolidate only when the canonical document can preserve all unique value.
- Delete only after checking the problem domain and every inbound repository-document link.
- A substantive inbound link favors Keep, Replace, or Consolidate over Delete.
- A standard fully owned by an actionable verifier, lint rule, type, schema, or test may be Delete only when no rationale or exception remains useful; otherwise Update it to retain only the part automation cannot express.

**Complete when:** every candidate has one outcome, every outcome cites concrete evidence, and every proposed removal accounts for unique content, domain relevance, and inbound links.

## 4. Decide

Apply Keep, Update, and Stale outcomes without additional approval when they are unambiguous and remain inside a rule-local standards scope or one learning-document scope. Any file-wide standards mutation requires an approval packet naming the exact file, every affected stable rule locator, and the aggregate disposition, even when classified Update or Stale.

Before Consolidate, Replace, or Delete, present one approval packet containing:

- every affected repository-relative path and exact stable rule locator for a standards-rule action;
- the evidence supporting the classification;
- the content retained, rewritten, or removed;
- inbound-link and catalog cleanup required; and
- the exact proposed action.

Ask for approval before executing those actions. Approval covers only the listed actions and paths. Preserve declined or unresolved candidates and include their recommendations in the final report.

When evidence supports several plausible outcomes, recommend the least destructive trustworthy option and ask. When a broad scope contains many judgment calls, decide in coherent topic batches so the user can evaluate related documents together.

**Complete when:** every unambiguous non-destructive outcome is ready to apply, and every destructive or materially rewriting outcome is approved, declined, or recorded as unresolved.

## 5. Apply and Validate

Apply approved actions one coherent rule, document, or overlap cluster at a time:

- **Update:** change only facts required for current accuracy and retrieval.
- **Stale:** preserve the existing rule or learning while making only that candidate's untrusted status unmistakable.
- **Consolidate:** for standards rules, integrate every unique useful point into the approved canonical rule inside its owning standards file, update inbound rule references, and remove only the approved subsumed rule block. For learning documents, select the broader, more current document, integrate every unique useful point, update inbound links and catalog entries, then remove the approved subsumed document.
- **Replace:** for a standards rule, rewrite only the approved rule block in its owning standards file with the grounded successor and update direct rule references. For a learning document, write a standalone successor grounded in Step 2, preserve useful historical context and failed approaches, update inbound links and catalogs, then remove or explicitly supersede the old document as approved.
- **Delete:** for a standards rule, remove only the approved rule block and mechanically clean its direct references; never remove the owning standards file. For a learning document, remove the approved document and mechanically clean decorative links and catalog entries.

Never widen approval for one rule into mutation of its entire standards file. Any whole-file standards mutation requires a separately approved action naming that exact file, every affected rule, and each disposition.

After each mutation, reread the complete affected documents and verify:

- present claims against current repository evidence;
- historical claims are recognizable as historical;
- paths, commands, snippets, and relative links resolve or are intentionally historical;
- metadata parses and follows the corpus convention;
- no unique content was lost during consolidation or replacement;
- no inbound standards, learning-document, instruction, or catalog link now dangles; and
- the owned diff contains only approved standards or learning maintenance.

Run an applicable documentation check when the repository configures one. Classify failures as sync-owned, pre-existing, unrelated, environmental, or blocked. Fix sync-owned failures. Revert an action whose central claim or safe content disposition cannot be validated.

**Complete when:** every applied action matches its classification and approval, the affected standards or learning corpus is internally consistent, applicable checks are green or classified, and the owned diff contains no unverified or out-of-scope mutation.

## 6. Deliver

Report:

- the scope and number of rules or documents examined;
- every rule or document and its classification;
- evidence and verification gaps for each outcome;
- every file created, changed, or removed;
- approved actions applied and proposals declined or unresolved;
- validation actually run and its result;
- pre-existing or unrelated failures; and
- remaining uncertainty or recommended future Value-gated capture, using `$ns-compound` when available.

Group unchanged Keeps for readability, but account for every in-scope rule or document. End with the locally validated standards or learning changes. Leave repository instructions, commits, pushes, pull requests, and deployment to their owning workflows.

**Complete when:** the user can account for every candidate and mutation from the report, and future agents encounter standards and learnings whose remaining guidance is accurate or visibly stale.
