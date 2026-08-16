# Platform Evidence

Use this file when an audit needs platform-specific claims. Guidance changes quickly: open the relevant first-party source and verify it before presenting the claim as current.

## Eligibility and crawler controls

- **Google:** generative Search features use the core Search index. A page must be indexed and eligible for a snippet; Google documents no additional AI-specific technical requirement. Googlebot and normal Search controls govern inclusion. [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- **OpenAI:** `OAI-SearchBot` supports search inclusion; `GPTBot` concerns potential training. Check both `robots.txt` and published IP access where a CDN or WAF is present. [Publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) and [ChatGPT Search](https://help.openai.com/en/articles/9237897-chatgpt-search)
- **Anthropic:** `Claude-SearchBot` supports search indexing, `Claude-User` supports user-directed retrieval, and `ClaudeBot` is the training crawler. [Crawler controls](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- **Perplexity:** `PerplexityBot` supports search results and `Perplexity-User` supports user-requested retrieval. Verify the current published IP ranges when diagnosing WAF access. [Crawler documentation](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- **Microsoft/Bing:** use normal crawl/index controls, accurate sitemaps, and IndexNow for meaningful additions, changes, and removals. These improve discovery and freshness, not guaranteed citation. [Sitemaps in AI-powered search](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search)

## Retrieval and citation selection

- Google says its generative Search features use retrieval-augmented generation and query fan-out on top of core Search ranking and quality systems. Its strongest stated long-term recommendation is unique, useful, non-commodity content. [Optimizing for generative AI](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Google's quality guidance emphasizes original reporting or research, completeness, first-hand expertise, clear sourcing, authorship, topic focus, and trust. [Helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- Microsoft recommends depth, clear structure, evidence, freshness, and entity consistency. Its AI Performance reporting exposes cited URLs and sampled grounding queries. [AI Performance in Bing Webmaster Tools](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- Perplexity describes hybrid lexical and semantic retrieval at sub-document granularity. This supports complete, self-contained evidence passages; it does not establish a universal formatting formula. [Architecting an AI-first search API](https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api)

## Claims to reject unless new first-party evidence supports them

- `llms.txt` is a general ranking or citation lever.
- A special “AI schema” guarantees or materially boosts citations.
- Allowing a model-training crawler improves live-search inclusion.
- FAQ markup, artificial chunking, keyword density, or a specific word count is a universal GEO advantage.
- Indexing guarantees retrieval, citation, placement, or traffic.
- A one-off answer-engine result is a stable rank.

## Evidence hierarchy

When sources conflict, prefer:

1. current platform documentation or standards;
2. current first-party engineering explanations;
3. reproducible original research;
4. direct observation from webmaster tools, logs, and live tests;
5. third-party studies and commentary as qualified supporting evidence only.

Separate documented facts, observed facts, inference, and unknowns in the final audit.
