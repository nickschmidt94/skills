---
name: ship-skill-pr
description: Package one coherent local skill addition or update into the canonical public skills repository, complete its catalog, changelog, metadata, behavioral evals, and validation, then commit, push, and open one pull request. Use only when the user has authorized publishing skill work for review; do not use for ordinary application repositories or installation-only requests.
---

# Ship Skill PR

Publish a local skill change as a complete, reviewable skills-repository pull request.

Invocation authorizes an isolated feature branch or clone, packaging the named local skill changes, updating the public repository surfaces they require, committing owned files, pushing without force, and opening or refreshing one pull request. It does not authorize changing the source skill beyond packaging repairs, deleting unrelated public skills, force-pushing, merging, releasing, tagging, or installing skills for other users.

Use five standards throughout:

- **Canonical** — resolve both the source skill and target skills repository from current evidence.
- **Portable** — publish a skill that remains accurate when optional companion skills or Nick's local paths are absent.
- **Complete** — ship the skill folder, catalog, changelog, metadata, evals, and validation together.
- **Owned** — preserve dirty checkouts and exclude unrelated skill or repository work.
- **Confirmed** — finish only when the remote pull request is open and its head matches the pushed commit.

One invocation publishes one coherent skills-repository change. Multiple skills may share the pull request only when they implement the same outcome or one is required to make the other usable.

## 1. Resolve Source and Target

Resolve the source skill from the explicit name or path, the skill changed in the current task, or the relevant installed skill directory. Read its complete `SKILL.md`, metadata, linked references, scripts, assets, and existing evals. Identify which files are authoritative and which are generated, cached, secret, machine-local, or unrelated.

Resolve the target from an explicit repository, the current checkout when it is the skills repository, or the configured canonical remote. For Nick, use `nickschmidt94/skills` when no different target is explicit. Confirm the authenticated user can publish there and establish its actual default branch, repository instructions, catalog, changelog, validator, eval format, and public-skill conventions from the current `origin` state.

Work from a clean isolated clone or worktree based on fresh `origin/<default>` unless the current target checkout is already clean, current, and dedicated to this task. Preserve existing user changes without stashing, resetting, rebasing, or rewriting them.

**Complete when:** every source path is classified, the target and default branch are verified, the public packaging contract is understood, and the working checkout contains no unrelated change.

## 2. Package the Skill

Copy the complete owned source into `skills/<name>/`, preserving its internal structure and executable bits. Exclude caches, logs, credentials, local environment files, generated scratch output, and documentation that the target contract does not publish. When updating an existing public skill, compare the full old and new folders so removed resources, renamed links, invocation policy, and behavioral changes are intentional.

Apply writing-for-agents guidance when that companion is installed. Otherwise enforce these equivalent standards directly:

- the name and description discriminate the actual invocation branches;
- every step has an observable completion criterion;
- substantial conditional material is linked and progressively disclosed;
- concepts, rules, and caveats are co-located without duplicated instructions;
- environment facts are looked up rather than cached in prose;
- optional companion skills have a plain-language fallback;
- authorization boundaries and terminal states are explicit; and
- local absolute paths, private assumptions, and unsupported claims are removed.

Make packaging-only repairs in the source and target copies together so the installed source does not immediately diverge from what is published. Keep product or workflow redesign outside this shipping task unless the user included it in scope.

**Complete when:** the public folder is self-contained, portable, internally linked, metadata-complete, and byte-consistent with the repaired authoritative source.

## 3. Complete the Public Surfaces

Update the target repository according to its live conventions:

- add or revise exactly one catalog entry whose direct link reaches the public `SKILL.md`;
- add a concise entry under `CHANGELOG.md` → `Unreleased`, using Added, Changed, Removed, or the repository's equivalent category;
- describe the behavioral outcome rather than the editing session;
- preserve invocation-policy documentation and cross-skill fallback promises; and
- add or update behavioral evals for every material invocation branch or authority boundary changed.

Evals should use realistic prompts and outcome-focused expectations. Cover the primary success path and each material branch that could cause premature completion, unsafe publication, missing-companion failure, or incorrect authority. Do not test headings, exact prose, or implementation trivia.

Inspect the full repository diff for catalog drift, duplicate changelog text, stale references, secrets, absolute machine paths, unintended deletions, and unrelated changes.

**Complete when:** every added or changed public skill is cataloged once, its meaningful behavior appears once under Unreleased, representative evals cover the changed contract, and the complete diff is coherent and owned.

## 4. Prove Publication Readiness

Run the target repository's authoritative validator using its documented environment and dependencies. Also run the relevant eval harness when one exists; otherwise exercise representative prompts as a behavioral contract review. Validate changed skill folders with any available generic skill validator only as supplemental evidence.

Repair owned failures and rerun the failing evidence. Review the complete change against the verified base, using `$ns-code-review` when available or the same prove-repair-rereview loop directly. Treat structural validation as necessary but insufficient: confirm discovery, optional-companion behavior, authority, and terminal criteria from the actual instructions and evals.

**Complete when:** authoritative validation is green, every changed behavior has representative evidence, a fresh final review finds no actionable issue, and remaining uncertainty is non-blocking and documented.

## 5. Open and Confirm the Pull Request

Use `$ns-ship-pr` when available to commit the owned repository change, push the feature branch without force, and create or refresh one ready-for-review pull request. If unavailable, perform that same owned, green, reviewable, and confirmed workflow directly. This skill's invocation supplies the publication authorization required for the skills repository only.

The pull request should lead with what the skill now enables, then summarize packaged skills, catalog and changelog changes, behavioral eval coverage, validation commands and results, and material residual uncertainty. Do not claim release, installation, merge, or deployment.

Reload the pull request and verify its open state, draft state, base, head branch, and head SHA against local `HEAD`.

**Complete when:** one intended non-draft pull request is open, its head equals local `HEAD`, and the reported URL opens the packaged skill change.

## Delivery

Lead with the pull request link. Report the packaged skills, branch and commit, catalog/changelog/eval work, verification actually run, source synchronization, and any excluded or residual local changes. Distinguish installed locally, committed, pushed, PR open, merged, and released states.
