# Initialization

Use this when the user says to initialize, start, resume, take over, or use this workflow for a new or existing iOS project.

## Purpose

Initialization creates a small project memory so the next turn or thread can continue without reopening every durable document.

## Required Actions

1. Read `AGENTS.md` if present.
2. Read `config.json`.
3. Identify the starting state:
   - empty repo
   - docs-only planning repo
   - existing Xcode project
   - partially built iOS app
   - resumed workflow with existing docs
4. Classify the request as app-level or feature-level.
5. Create or update `docs/WORKFLOW_STATE.md` when the workflow will continue beyond one short task.
6. Do not create full PRD, UX, plan, and test docs just because initialization happened.

## WORKFLOW_STATE.md Template

```markdown
# WORKFLOW_STATE

## Context Summary
- Current stage:
- App scale:
- Launch intent:
- Product goal:
- Current build slice:
- Last verified state:
- Next recommended action:

## Key Decisions
-

## Open Questions
-

## Durable Docs
- APP_BRIEF.md:
- PRD.md:
- UX_SPEC.md:
- UI_REFERENCE.md:
- IMPLEMENTATION_PLAN.md:
- TEST_PLAN.md:
- docs/specs/:

## Do Not Do Yet
-

## Context Budget Notes
- Read this file first when resuming.
- Read durable doc summaries before details.
- Do not reopen the full app workflow unless app-level scope changed.
```

## Resume Rule

When resuming from `docs/WORKFLOW_STATE.md`:

1. Read `Context Summary` and `Key Decisions` first.
2. Read only the durable doc sections needed for the current task.
3. State the stage, scope, next artifact or action, and verification boundary.
4. Ask only if a blocking decision would change scope, data risk, UI direction, cost, release path, or testing depth.
