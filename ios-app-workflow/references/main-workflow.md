# Main Workflow

Use this for staged iOS app work. Keep phases small and do not turn the workflow into a full product bureaucracy.

## Contents

- Workflow
- Phase Gates
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

## Workflow

1. App Scale
2. App Brief
3. PRD
4. UX Spec
5. UI Reference, when visual quality matters
6. Implementation Plan
7. Build
8. Test
9. Polish
10. Release or Handoff

## Phase Gates

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
