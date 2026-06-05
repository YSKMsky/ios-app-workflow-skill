# Main Workflow

Use this for staged iOS app work. Keep phases small and do not turn the workflow into a full product bureaucracy.

## Contents

- Workflow
- App-Level vs Feature-Level Gate
- Phase Gates
- Product Owner Mode
- App Scale
- App Brief
- PRD
- UX Spec
- UI Reference
- Implementation Plan
- Build
- Test
- Polish
- Release or Handoff

## App-Level vs Feature-Level Gate

Before creating or updating `APP_BRIEF.md`, `PRD.md`, `UX_SPEC.md`, `IMPLEMENTATION_PLAN.md`, or `TEST_PLAN.md`, decide whether the request is app-level or feature-level.

Use app-level workflow when the task changes:

- new app direction
- V1 scope
- core navigation or product loop
- data model or persistence boundary
- backend, auth, payment, or cloud architecture
- product positioning

Use Feature Spec Mode when the task is:

- one feature
- one screen
- one UI polish pass
- one bugfix
- one testing, routing, or context-control change

For feature-level work, read `references/feature-spec-mode.md` and do not reopen the full app workflow unless the feature changes app-level scope.

## Workflow

1. App Scale
2. Product Owner Mode, when launch intent or user-control checkpoints matter
3. App Brief
4. PRD
5. UX Spec
6. Feature Spec, when the task is feature-level
7. UI Reference, when visual quality matters
8. Implementation Plan
9. Build
10. Test
11. Polish
12. Release or Handoff

## Phase Gates

### 0. Product Owner Mode

Output:

- launch intent: exploring, personal use, share with others, or public launch
- one sentence naming the next product decision Codex can drive
- one sentence naming any decision that must stay with the user

Read:

- `references/product-owner-mode.md`

Do not:

- use "technical co-founder" style role text as a substitute for concrete workflow rules
- ask for approval on every low-impact implementation detail

### 1. App Scale

Output:

- `tiny`, `small`, or `medium`
- one sentence explaining the deciding risks

Read:

- `references/app-scale.md`

Do not:

- classify by screen count alone

### 2. App Brief

Output:

- `APP_BRIEF.md`

Must include:

- user and problem
- launch intent
- V1 learning or product loop
- V2/V3 deferred scope
- success criteria
- non-goals

Gate:

- user can explain what V1 does in one paragraph

### 3. PRD

Output:

- `PRD.md`

Must include:

- V1 features
- non-goals
- user stories
- data saved or discarded
- acceptance criteria

Gate:

- there is no ambiguity about what V1 excludes

### 4. UX Spec

Output:

- `UX_SPEC.md`

Must include:

- screens
- navigation
- empty/loading/error states
- key flows
- manual-only interactions, if agent cannot operate them

Gate:

- Codex can build screens without inventing major IA

### 5. UI Reference

Output:

- `UI_REFERENCE.md`, only when UI direction matters

Read:

- `references/ui-workflow.md`

Gate:

- visual target or direction is clear enough to implement or generate concepts

### 6. Implementation Plan

Output:

- `IMPLEMENTATION_PLAN.md`

Must include:

- build slices
- file/module boundaries
- dependency and credential gates
- verification per slice

Gate:

- implementation can proceed in small, testable chunks

### 7. Build

Use:

- `swiftui-ui-patterns` for screen composition, navigation, controls, and state
- `swiftui-view-refactor` when SwiftUI files become too large or state ownership is unclear
- OpenAI credential/docs skills before live API work

Gate:

- each slice has a cheap proof before moving on
- each major slice has a visible or user-understandable checkpoint

### 8. Test

Read:

- `references/testing.md`

Gate:

- required tests and explicit skips are listed

### 9. Polish

Read:

- `references/ui-workflow.md`
- `references/skill-routing.md`

Gate:

- P0/P1 visual issues fixed
- P2 issues capped to the few that matter most

### 10. Release or Handoff

Read:

- `references/context-control.md`

Gate:

- current state can be resumed by a fresh thread in under one minute
