---
name: ns-ship-pr
description: Commit owned local changes, push the current feature branch, and create or refresh one GitHub pull request. Use only when the user has authorized publishing a verified change for review.
---

# NS Ship PR

Publish one coherent change as one reviewable GitHub pull request.

Invoking this skill authorizes creating one necessary feature branch, committing the owned changes, pushing the live branch without force, and creating or refreshing one pull request. It does not authorize rebasing, rewriting published history, force-pushing, stacking pull requests, promoting drafts, monitoring, merging, deployment, or unrelated repository changes.

Use four standards throughout:

- **Owned** — only the intended change enters the commit and pull request.
- **Green** — publication is supported by current verification.
- **Reviewable** — the commit and pull request explain one coherent outcome.
- **Confirmed** — local, remote, and GitHub state agree after publication.

## 1. Establish Readiness

Inspect the current sources of truth:

- repository root and applicable instructions;
- status, `HEAD`, current branch, upstream, remotes, and default branch;
- complete committed, staged, unstaged, and untracked state;
- the full change against the intended base;
- open pull requests for the exact head repository and branch;
- repository commit, pull-request-template, and contribution conventions; and
- verification evidence for the publishable change.

Classify every changed and untracked path as owned or excluded. Inspect owned content for credentials, local environment files, unintended generated output, and unrelated work. Stop on ambiguous ownership or mixed owned and excluded work within one file because file-level staging cannot preserve that boundary safely.

Accept verification from earlier in the current task only when the checkout has not changed since it ran. Otherwise run the smallest relevant checks that establish readiness. A failing required check blocks a ready pull request. Proceed with known failures only when the user explicitly requested a draft, and disclose them in its body.

Distinguish the starting state:

- uncommitted owned work requires a commit;
- committed but unpushed work requires a push;
- pushed work requires a new or refreshed pull request; and
- no unpublished or stale pull-request state means there is nothing to ship.

**Complete when:** every path is classified, the owned outcome and comparison base are known, verification is current, GitHub access and PR state are known, and no ownership or publication ambiguity remains.

## 2. Prepare the Branch

Continue on a named feature branch when it contains the intended work. On the default branch or detached `HEAD`, create one outcome-named feature branch at the current commit so existing commits and working changes remain intact.

Establish the actual default branch from the remote or repository metadata. Ask when the base, push remote, head ownership, or unpushed commit ownership cannot be established safely. Preserve history in place; branch preparation must not reset, rebase, cherry-pick, stash, or rewrite it.

After any branch creation, reread the branch, `HEAD`, status, and intended base. Confirm that the complete owned change remains present and excluded work is unchanged.

**Complete when:** the work is on a named non-default branch, the base and push remote are verified, the intended change is intact, and no history was rewritten.

## 3. Commit Owned Work

Preserve existing commits. When owned changes remain uncommitted, create one new commit by default. If the scope contains unrelated outcomes that should not share a pull request, stop and ask whether to separate them rather than inventing commit boundaries.

Stage explicit owned paths only. Inspect the staged diff and compare it with the owned scope before committing. When unrelated paths were already staged, use an explicit commit pathspec after confirming every selected file is wholly owned; leave the other staged paths untouched.

Derive the message from the user-visible or system outcome and the repository's current convention. Use the correct change type from intent rather than defaulting an ambiguous change to `fix` or `feat`. Allow commit hooks to run. Investigate their output instead of bypassing them.

After committing, inspect the new commit and repository status. Confirm that every owned change appears exactly once, excluded work remains outside the commit, and no hook-generated change was silently left behind.

If all owned work was already committed, create no additional commit.

**Complete when:** the publishable range contains the owned work exactly once, its commits are coherent and convention-matched, and excluded local work remains preserved.

## 4. Push and Open

Immediately before publishing, reread the live branch, `HEAD`, push remote, upstream, and existing PR state. Push the live `HEAD` to the verified remote without force and establish upstream tracking when needed.

Recheck GitHub for an open pull request matching the exact head repository and branch. Treat a failed query as unknown state to resolve, not proof that no PR exists.

Compose the title and body from the complete pushed range against the verified base. Follow repository templates and required fields. Lead with what became possible or fixed, then include only the decisions, risks, verification, evidence, and residual uncertainty that help a reviewer decide. Use issue-closing syntax only when the pull request fully resolves the identified issue and the repository host supports that syntax. Pass multiline body content through a temporary body file.

When no matching PR exists, create one against the verified base. Create it ready for review when verification is Green; create a draft only when explicitly requested.

When a matching PR exists, recompute its title and body from the complete pushed range. Preserve still-valid issue references, evidence links, required template fields, and draft state. Refresh materially stale or incomplete metadata automatically; skip the edit when the proposed content is equivalent.

**Complete when:** the exact local `HEAD` is pushed and one unambiguous open pull request exists with an accurate head, base, title, body, and requested draft state.

## 5. Confirm and Deliver

Verify from GitHub that the pull request's head repository, branch, and SHA match local `HEAD`. Confirm its base branch, URL, open state, draft state, title, and body. Inspect final repository status so excluded or newly generated local changes remain visible.

Report:

- whether a branch or commit was created;
- commit SHA and branch;
- push remote and result;
- pull request URL and number;
- whether PR metadata was created, refreshed, or already current;
- verification used to establish Green;
- excluded or remaining local changes; and
- any unresolved uncertainty.

Distinguish committed, pushed, open, ready, and merged as separate states. Stop after the confirmed pull request; monitoring and merging require separate authorization.

**Complete when:** local `HEAD`, the remote head, and the PR head agree, the reported URL opens the intended pull request, and every publication claim is supported by fresh evidence.
