---
name: ns-compound-sync
description: Audit and sync an existing repository learning store when captured guidance may be stale, contradictory, overlapping, superseded, or broken by codebase change. Invoke explicitly with a file, area, module, keyword, or repository-wide scope after learnings have accumulated.
---

# NS Compound Sync

Keep repository learnings accurate, distinct, and trustworthy as the codebase evolves.

Use four standards throughout:

- **Current** — present-tense claims match authoritative repository evidence.
- **Distinct** — each document earns separate retrieval value.
- **Conservative** — uncertainty narrows claims or marks them stale; it never invents current guidance.
- **Complete** — every in-scope document receives an evidence-backed outcome.

This skill authorizes local maintenance inside the repository's existing learning store, normally `docs/learnings/`. It may update documents and apply a visible stale marker. Consolidation, replacement, and deletion require the user's approval of the exact proposed action. Preserve source code, repository instructions, glossaries, unrelated documentation, git state, and external systems. Use `$ns-compound` to capture a new learning and `$ns-ship-pr` for publication.

## 1. Scope

Resolve the repository and learning store from the request and current tree. Follow an established repository location when one exists; otherwise inspect `docs/learnings/`. If no learning store exists, report that `$ns-compound` should establish it during the first qualified capture and stop.

Resolve candidates using the narrowest supplied scope:

1. exact document path or filename;
2. directory or area;
3. frontmatter field or tag;
4. module, component, or content keyword; or
5. the entire store when the user explicitly requests a repository-wide sync.

When no scope is supplied, inventory the store without editing, group documents by area, identify the highest-value maintenance scope using visible drift, overlap, or contradiction signals, and ask whether to proceed with that scope. When a supplied scope matches nothing, report the miss without widening it.

Record repository status and preserve all pre-existing changes. Exclude catalog or index files from classification, but maintain their links when an approved action changes a listed document.

**Complete when:** the repository, existing store, exact candidate set, requested breadth, and pre-existing changes are explicit, or the run has ended without mutation because no valid scope exists.

## 2. Ground

Read every candidate document and the smallest current source set needed to test its load-bearing claims: referenced implementation, configuration, tests, contracts, related learnings, and repository history only when current files cannot explain a transition.

Check independently for:

- missing or renamed paths, symbols, commands, and links;
- snippets or procedures that no longer match current behavior;
- claims contradicted by current code or configured workflows;
- overlap, supersession, or contradiction among candidate documents; and
- historical or operational claims the repository cannot currently witness.

Match documentation to repository reality; source-code changes are outside this skill. Treat missing evidence as a verification gap, not proof that a plausible claim is false. Mark removed behavior and obsolete paths as historical when they remain useful to the learning.

For each candidate, record the claims tested, supporting or contradicting evidence, verification gaps, inbound learning-document links, and any relationship to another candidate.

**Complete when:** every candidate's load-bearing claims and relationships have been checked against the best available evidence, and every uncertainty is distinguished from a contradiction.

## 3. Classify

Assign exactly one outcome to every candidate:

- **Keep** — accurate, useful, and separately findable; leave unchanged.
- **Update** — the learning remains correct but factual references, snippets, links, metadata, or historical framing drifted; repair in place.
- **Stale** — current guidance cannot be trusted and the available evidence cannot support a replacement; add the corpus's established stale marker. When none exists, add `status: stale`, a concise `stale_reason`, and `stale_date: YYYY-MM-DD` to YAML frontmatter, or a clear top-of-document stale notice when frontmatter is absent.
- **Consolidate** — documents substantially duplicate the same learning and one canonical document can retain every unique, useful point; propose merging and removing the subsumed document.
- **Replace** — the recommended approach is misleading and current evidence can support a trustworthy successor; propose the successor's scope and disposition of the old document.
- **Delete** — the learning is wholly redundant or both its implementation and problem domain are gone; propose removal.

Use these boundaries:

- A changed recommendation is Replace, not Update.
- Age, cosmetic quality, or a missing referenced file alone does not establish staleness.
- Shared code does not establish duplication; the documents must address the same retrievable problem, decision, or pattern.
- Consolidate only when the canonical document can preserve all unique value.
- Delete only after checking the problem domain and every inbound repository-document link.
- A substantive inbound link favors Keep, Replace, or Consolidate over Delete.

**Complete when:** every candidate has one outcome, every outcome cites concrete evidence, and every proposed removal accounts for unique content, domain relevance, and inbound links.

## 4. Decide

Apply Keep, Update, and Stale outcomes without additional approval when they are unambiguous and remain inside the selected learning scope.

Before Consolidate, Replace, or Delete, present one approval packet containing:

- every affected repository-relative path;
- the evidence supporting the classification;
- the content retained, rewritten, or removed;
- inbound-link and catalog cleanup required; and
- the exact proposed action.

Ask for approval before executing those actions. Approval covers only the listed actions and paths. Preserve declined or unresolved candidates and include their recommendations in the final report.

When evidence supports several plausible outcomes, recommend the least destructive trustworthy option and ask. When a broad scope contains many judgment calls, decide in coherent topic batches so the user can evaluate related documents together.

**Complete when:** every unambiguous non-destructive outcome is ready to apply, and every destructive or materially rewriting outcome is approved, declined, or recorded as unresolved.

## 5. Apply and Validate

Apply approved actions one coherent document or overlap cluster at a time:

- **Update:** change only facts required for current accuracy and retrieval.
- **Stale:** preserve the existing learning while making its untrusted status unmistakable.
- **Consolidate:** select the broader, more current document; integrate every unique useful point in its natural location; update inbound links and catalog entries; then remove the subsumed document.
- **Replace:** write a standalone successor grounded in Step 2, preserve useful historical context and failed approaches, update inbound links and catalogs, then remove or explicitly supersede the old document as approved.
- **Delete:** remove the approved document and mechanically clean decorative links and catalog entries.

After each mutation, reread the complete affected documents and verify:

- present claims against current repository evidence;
- historical claims are recognizable as historical;
- paths, commands, snippets, and relative links resolve or are intentionally historical;
- metadata parses and follows the corpus convention;
- no unique content was lost during consolidation or replacement;
- no inbound learning-document or catalog link now dangles; and
- the owned diff contains only approved learning maintenance.

Run an applicable documentation check when the repository configures one. Classify failures as sync-owned, pre-existing, unrelated, environmental, or blocked. Fix sync-owned failures. Revert an action whose central claim or safe content disposition cannot be validated.

**Complete when:** every applied action matches its classification and approval, the affected learning set is internally consistent, applicable checks are green or classified, and the owned diff contains no unverified or out-of-scope mutation.

## 6. Deliver

Report:

- the scope and number of documents examined;
- every document and its classification;
- evidence and verification gaps for each outcome;
- every file created, changed, or removed;
- approved actions applied and proposals declined or unresolved;
- validation actually run and its result;
- pre-existing or unrelated failures; and
- remaining uncertainty or recommended future capture with `$ns-compound`.

Group unchanged Keeps for readability, but account for every in-scope document. End with the locally validated learning-store changes. Leave repository instructions, commits, pushes, pull requests, and deployment to their owning workflows.

**Complete when:** the user can account for every candidate and mutation from the report, and future agents encounter a learning set whose remaining guidance is accurate or visibly stale.
