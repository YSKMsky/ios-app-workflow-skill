# Feature Spec Mode

Use this for feature-level work so small tasks do not reopen the full app workflow.

## Contents

- When To Use
- When Not To Use
- Intake Rules
- Approach Gate
- Low-Risk Fast Path
- Spec File
- Template
- Self-Check
- User Review And Commit Gate
- Main Doc Sync

## When To Use

Use Feature Spec Mode when the task is:

- a single feature
- a single screen
- a single UI polish task
- a single bugfix
- a single testing strategy change
- a single skill-routing change
- a single context-control change
- a bounded implementation slice where app V1 scope remains stable

## When Not To Use

Do not use Feature Spec Mode when the task changes:

- a new app from zero
- V1 scope
- multiple core flows at once
- core navigation or product loop
- major data model or persistence boundary
- backend, auth, payment, or cloud architecture
- product positioning

Use the main workflow instead.

## Intake Rules

Before writing a feature spec:

1. Scan the repo and existing docs enough to avoid asking questions already answered.
2. Ask only blocking questions that affect implementation path, scope, interface, data, UI target, or testing.
3. Ask at most 3 questions per round.
4. Ask at most 10 total questions.
5. Prefer multiple-choice questions when the decision space is clear.

After each user answer, recap in 2-4 sentences:

- confirmed information
- `TBD` items that still matter
- whether any ambiguity still changes implementation path, scope, or interface

Stop asking when no critical ambiguity remains.

## Approach Gate

When enough information exists, present 2-3 approaches.

For each approach include:

- fit
- benefits
- risks
- complexity: low, medium, or high
- affected areas
- future work excluded from this pass

Recommend one approach and explain why it fits the current constraints. Wait for user confirmation before writing the spec.

## Low-Risk Fast Path

Skip the full approach gate when one path is clearly:

- low-risk
- reversible
- consistent with existing docs and project patterns
- limited to one feature, screen, bugfix, polish pass, or test/routing/context-control change

In that case, state the recommended path, why it is safe, and the cheapest verification, then proceed unless the user objects or a product-owner checkpoint is triggered.

## Spec File

Write one spec file:

```text
docs/specs/spec{n}_<slug>.md
```

Numbering:

1. Create `docs/specs/` if missing.
2. Scan existing files matching `spec(\d+)_`.
3. Use `max + 1`, or `1` if none exist.

Slug:

- lowercase
- snake_case
- remove special characters
- keep short and meaningful

## Template

```markdown
# Feature Spec: <title>

## Context Summary

## Confirmed Decisions

## TBD / Open Questions

## Goals

## Non-Goals

## User Flow

## Proposed Approach

## Alternatives Considered

## Implementation Boundaries

## UI Notes

## Testing Notes

## Acceptance Criteria

## Future Work
```

## Self-Check

Before asking the user to review, check and fix:

- placeholder text
- contradictions
- scope creep
- ambiguous requirements
- missing acceptance criteria
- testing notes that do not match the change risk
- UI notes that conflict with `UI_REFERENCE.md`
- unresolved product-owner checkpoint hidden as an implementation detail

## User Review And Commit Gate

After the spec is written:

1. Ask the user to review the spec.
2. If they request changes, revise and rerun the self-check.
3. After approval, ask whether to commit only that spec.
4. If approved, stage only `docs/specs/spec{n}_<slug>.md`.
5. Commit with:

```bash
git commit -m "docs: add spec{n} <slug>"
```

Do not stage unrelated files.

## Main Doc Sync

If the feature spec changes important app decisions, update only the relevant main docs' `Context Summary` or `Key Decisions`.

Do not rewrite full `APP_BRIEF.md`, `PRD.md`, `UX_SPEC.md`, `IMPLEMENTATION_PLAN.md`, or `TEST_PLAN.md` unless the user explicitly asks.
