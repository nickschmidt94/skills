# Spec Review

Use this branch only for the independently reported Spec axis.

## Inputs

Require the pinned comparison point, commit list when present, complete diff including in-scope untracked files, and the complete ordered set of independently resolved accepted Spec sources: explicit user requests, accepted plans or paths, referenced issues, and pull-request requirements. Record source precedence and any unresolved conflict. Later explicit user constraints override earlier artifacts; when precedence remains unclear, return `Spec: unresolved`, prohibit repair against either source, and require the parent to return **Review incomplete** until the conflict is resolved.

If no accepted source exists, return `Spec: no spec available`. Do not reverse-engineer requirements from the implementation or invent them from a historical plan.

## Review

Compare every requirement and explicit boundary from every accepted source with the complete changed behavior. Separate an omitted requirement from a standards or correctness concern. Name the source and requirement supporting each candidate.

Review directly. Do not invoke `ns-code-review` and do not spawn another agent.

## Output

Return `Spec: pass`, `Spec: no spec available`, `Spec: unresolved`, or concise candidates with the exact requirement, source, changed location, and observable mismatch. The parent will independently prove each candidate and repair it only when the accepted response is locally scoped and decision-complete; an unresolved source conflict blocks repair and requires **Review incomplete**.
