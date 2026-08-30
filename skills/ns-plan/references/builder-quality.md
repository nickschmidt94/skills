# Builder Quality

Use this reference only when the work is cross-cutting, architectural, agent-facing, or domain-bearing. Apply the exposed lenses; do not force an architecture report or fixed ledger.

## Outcome

Name the smallest coherent product result. Exclude speculative infrastructure, abstraction, or cleanup that does not help prove that result.

## Domain

When terms, identities, states, or relationships change, resolve the active context through root `CONTEXT-MAP.md` when present; otherwise use the repository root. Read its `CONTEXT.md` when available. Planning may challenge or settle domain language; implementation should consume the accepted model rather than silently redefine it. Offer an ADR only for a hard-to-reverse, surprising choice produced by a real trade-off.

## Depth and locality

Put meaningful behavior behind a small interface at a real seam. Concentrate policy, change, and verification in one owner. A proposed seam or cleanup must remove a concrete cost such as duplicated authority, scattered change, caller-visible implementation knowledge, a shallow pass-through, competing sources of truth, or tests coupled to internals. Preference alone is not a planning defect.

## Legibility and context placement

A fresh human or agent must be able to locate the owning module, authoritative context, public contract, and canonical verification without conversation history. Keep glossary terms in the active `CONTEXT.md`, qualifying decisions in the appropriate ADR scope, ordinary behavior in product documentation and tests, and repository learnings in their established store.

## Proof

Choose the shortest authoritative feedback loop that demonstrates the product result and the affected interface. Name the real integration or user-visible path when compilation or isolated tests cannot prove it.

**Complete when:** every exposed domain, ownership, interface, context-placement, and proof decision is explicit enough to implement without inventing architecture, and every quality claim names a concrete cost or observable result.
