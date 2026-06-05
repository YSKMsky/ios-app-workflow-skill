# Document Templates

Use these when creating or updating workflow docs. Keep documents short enough to read quickly.

## Contents

- Global Rules
- APP_BRIEF.md
- PRD.md
- UX_SPEC.md
- UI_REFERENCE.md
- IMPLEMENTATION_PLAN.md
- TEST_PLAN.md

## Global Rules

- Put `Context Summary`, `Key Decisions`, `Open Questions`, and `Details` at the top level.
- Keep `Context Summary` under 12 bullets.
- Keep `Key Decisions` concrete and dated when useful.
- Put long explanations under `Details`.
- Update summaries after major phase changes.

## APP_BRIEF.md

```markdown
# APP_BRIEF

## Context Summary
- Product:
- Primary user:
- Core problem:
- V1 loop:
- App scale:

## Key Decisions
- V1 includes:
- V1 excludes:
- V2/V3 candidates:

## Open Questions
- 

## Details
### Product Goal
### User And Use Case
### V1 Scope
### Non-Goals
### Success Criteria
```

## PRD.md

```markdown
# PRD

## Context Summary
- V1 goal:
- Core user journey:
- Required data:
- Excluded scope:

## Key Decisions
- 

## Open Questions
- 

## Details
### Features
### User Stories
### Data Save / Discard Rules
### Acceptance Criteria
### Out Of Scope
```

## UX_SPEC.md

```markdown
# UX_SPEC

## Context Summary
- Key screens:
- Primary flow:
- Agent-manual interactions:

## Key Decisions
- 

## Open Questions
- 

## Details
### Navigation
### Screens
### States
### Empty / Loading / Error
### Edge Cases
### Manual Checklist Items
```

## UI_REFERENCE.md

```markdown
# UI_REFERENCE

## Context Summary
- Direction:
- Key screens:
- Source references:

## Key Decisions
- 

## Open Questions
- 

## Details
### Page Structure
### Mood / Visual Direction
### References
### Do Not Want
### Key Screens
### Reusable Visual Rules
```

## IMPLEMENTATION_PLAN.md

```markdown
# IMPLEMENTATION_PLAN

## Context Summary
- Current slice:
- Build order:
- Dependencies:
- Verification:

## Key Decisions
- 

## Open Questions
- 

## Details
### Build Slices
### File / Module Boundaries
### Credential Gates
### Data Boundaries
### Verification Per Slice
### Do Not Do Yet
```

## TEST_PLAN.md

```markdown
# TEST_PLAN

## Context Summary
- App scale:
- Required verification:
- Explicit skips:

## Key Decisions
- 

## Open Questions
- 

## Details
### Change-Type Matrix
### Simulator Scenarios
### Screenshot Scenarios
### Persistence Scenarios
### API Scenarios
### Manual Checklist
### Skipped Tests And Why
```
