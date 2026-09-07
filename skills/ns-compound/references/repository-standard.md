# Repository Standard Capture

Use this branch only after the Value gate passes and placement selects one active repository standard.

## Resolve the owner

Follow repository instructions and locate the existing standards source, conventionally root `CODING_STANDARDS.md`. Verify that an applicable repository instruction contains a trigger-to-path pointer for that source. Search current standards, executable checks, focused contracts, and `docs/learnings/` for the same mechanism before writing. Update an existing rule instead of duplicating it.

When no standards file exists, or an existing standards source lacks that pointer, prepare the standards-file change plus the exact trigger-to-path pointer needed in the applicable `AGENTS.md` as one pending discoverability proposal. A new file also needs a compact ownership and admission note. Do not write either file change until the user explicitly approves the pointer mutation. If approval is declined or unavailable, report `needs user input` and leave the standards source unchanged with no undiscoverable draft.

## Write one rule

Select one stable rule ID or the repository's established identifier scheme. Express:

- when the rule applies;
- the positive behavior required;
- why the failure mechanism matters;
- the real exception boundary; and
- the proof surface available to implementation or review.

Do not copy an investigation transcript, tool command catalog, or architecture prose. If an executable check with an actionable failure can fully own the behavior, stop with `wrong home` and name that check instead of adding prose policy.

## Validate

Validate the proposed or changed standard against current evidence, confirm the ID is unique and every required field is present, and run any focused documentation or standards verifier. When a new or existing standards source lacks a discoverability pointer, present the exact pending pointer with its file, placement, and text; after approval, write both changes, resolve the standards pointer from a fresh repository context, and inspect the owned diff. If the pointer is not approved, report `needs user input` and leave both files unchanged. Change exactly one primary standards destination plus its approved discoverability pointer.
