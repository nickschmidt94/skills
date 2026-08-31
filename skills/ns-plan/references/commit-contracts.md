# Commit Contracts

A commit boundary is where planned work makes an effect durable or externally observable. Apply every relevant rule below to each exposed boundary; use the smallest plan representation that makes the decisions clear.

## Authority

Name the source of truth for the operation and the inputs that determine its result. Treat caches, pointers, generated artifacts, and client-provided identifiers as evidence unless the system explicitly makes one authoritative.

## Commit and stages

Identify the final commit or linearization point. Separate preparation, durable commit, activation, invalidation, delivery, and recovery when their success can diverge. Define every reachable aggregate outcome from durable evidence, including complete, partial, blocked, unknown, not applicable, and not reached when those states are possible.

## Failure and repetition

For each external write or provider call, define acknowledgement-unknown behavior, the authoritative reconciliation read, the idempotency identity, and the safe retry rule. Make crash recovery preserve already-committed work.

## Concurrency

List mutable inputs whose change could invalidate prepared work. Name the production concurrency primitive, where each input is snapshotted, and where stale state is fenced at the final commit point. State what wins when mutation occurs immediately before and immediately after that fence.

## Projections

Trace the committed result through every material secondary surface, such as rendered output, accessibility data, metadata, caches, stored assets, exports, logs, analytics, recovery catalogs, and compatibility paths. When a public contract changes, trace it through serialization, adapters, interfaces, and cross-language consumers. Preserve access and redaction rules across those surfaces.

## Proof

Require verification through the authoritative source path and observable result. Compilation, successful decoding, object existence, or a cached read is sufficient only when it directly proves the contract being claimed.

**Complete when:** for every exposed boundary, an implementer can identify the authority, commit point, divergent stages, failure and retry behavior, concurrency protection, affected projections, and real proof wherever each can change the outcome. No material recovery, propagation, or verification decision remains implicit.
