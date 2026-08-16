---
name: llm-visibility-audit
description: Audit and improve a website's grounding visibility in ChatGPT Search, Google AI Overviews or AI Mode, Microsoft Copilot or Bing, Claude web search, and Perplexity. Use when the user asks about LLM visibility, AI search citations, GEO, AEO, answer-engine optimization, crawler access, or why a site is absent from AI-generated results.
---

# LLM Visibility Audit

Treat LLM visibility as **grounding**: a page must first be eligible for retrieval, then useful enough to select and cite. Do not substitute cosmetic “AI optimization” for either condition.

## 1. Establish the target

Identify:

- the site, live URLs, repository, or supplied pages in scope;
- the answer engines that matter;
- the audience and highest-value questions the site should answer;
- whether the user wants diagnosis, recommendations, implementation, or measurement.

If the request is broad, choose a representative set of commercially or editorially important questions and state the assumption. Do not require the user to invent a keyword list before useful work can begin.

This step is complete when the audit has a bounded surface, named engines, and a representative question set.

## 2. Prove eligibility

Inspect the real surface before judging content. Where access permits, verify:

- HTTP status, redirects, canonical URL, `noindex`, and snippet controls;
- `robots.txt` rules for each relevant search or retrieval crawler;
- CDN, WAF, rate-limit, authentication, or cookie barriers;
- rendered access to important text, including JavaScript-dependent content;
- internal discovery, XML sitemap coverage, and truthful `lastmod` values;
- duplicate, obsolete, or conflicting URLs;
- current indexing evidence in available webmaster tools or search indexes.

Distinguish a search/retrieval crawler from a model-training crawler. Never imply that permitting training improves live-answer visibility without current first-party evidence.

This step is complete when every relevant gate is marked **pass**, **fail**, or **unknown**, with observed evidence and the consequence of each failure.

## 3. Map grounding demand to sources

For each representative question, identify:

- the intended page that should answer it;
- the direct answer or claim the engine would need;
- the evidence supporting that claim;
- the source's unique information gain;
- the independent sources that corroborate the site or entity;
- the fact's freshness requirements.

Use query fan-out: include the definitions, comparisons, constraints, proof, objections, and follow-up questions a user needs to reach a decision. Do not manufacture near-duplicate pages for every phrasing.

This step is complete when every priority question has one intended source and every missing answer, evidence asset, or corroboration gap is explicit.

## 4. Assess sourceworthiness

Judge pages in this order:

1. **Information gain** — original data, first-hand experience, expert analysis, methods, concrete comparisons, definitions, procedures, or current first-party facts.
2. **Authority** — relevant earned links, citations, reviews, coverage, authorship, credentials, editorial accountability, and entity consistency.
3. **Citation readiness** — a clear subject, direct answer, supportable facts, provenance, units, dates, scope, limitations, and passages that remain accurate out of context.
4. **Freshness** — substantive maintenance appropriate to how quickly the claim changes.
5. **Presentation** — descriptive titles and headings, accessible text, useful tables or lists, and media that strengthens rather than hides the evidence.

Formatting cannot rescue a weak source. Do not reward FAQ templates, forced chunking, generic schema, keyword permutations, fake freshness, or mass-produced summaries merely because they look machine-readable.

This step is complete when each recommendation points to an observed grounding failure and explains why fixing it increases eligibility, retrieval relevance, trust, or citation accuracy.

## 5. Prioritize the work

Order recommendations by dependency and expected value:

1. blocked eligibility;
2. missing or commodity source material;
3. weak authority or corroboration;
4. ambiguous or difficult-to-extract evidence;
5. stale or conflicting facts;
6. measurement gaps.

For each action, include impact, effort, owner or surface, prerequisite, and verification method. Separate confirmed findings from inference and unknowns. Prefer a short high-confidence queue over a long generic checklist.

This step is complete when the user can execute the highest-value work without having to reinterpret the audit.

## 6. Close the measurement loop

Use the strongest available first-party evidence:

- indexing and crawl reports;
- cited URLs and grounding queries;
- verified crawler logs;
- AI-search referral parameters;
- conversions or useful post-click behavior;
- a stable panel of representative questions tested over time.

Measure citation quality and business outcome, not citation count alone. Generated answers vary by engine, model, prompt, location, and time; do not present a one-off prompt result as a stable rank.

This step is complete when the report names a baseline, the next observation date or cadence, and the signals that would confirm or falsify each major recommendation.

## Platform-specific evidence

When the audit makes current claims about crawler names, platform controls, ranking guidance, or reporting features, read [`references/evidence.md`](references/evidence.md) completely and verify drift-prone facts against the linked first-party source. Prefer the platform owner, standards body, or original research over SEO commentary.

## Report format

Lead with the actual constraint and highest-value opportunity.

1. **Verdict** — one paragraph stating what most limits visibility.
2. **Evidence** — observed eligibility, sourceworthiness, authority, and measurement findings.
3. **Priority actions** — ordered by dependency and expected value.
4. **What not to spend time on** — only myths relevant to this site.
5. **Verification** — checks run, unknowns, baseline, and follow-up measurement.

If the user requested implementation, make the in-scope changes and verify the real site. If the user requested only an audit or explanation, remain read-only.
