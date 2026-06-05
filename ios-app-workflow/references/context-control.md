# Context Control

Use this when documents, screenshots, logs, or conversation history are getting large.

## Document Reading Boundary

Every durable workflow doc should start with:

- `Context Summary`
- `Key Decisions`
- `Open Questions`
- `Details`

Default reading order:

1. Read `Context Summary`.
2. Read `Key Decisions`.
3. Read only the `Details` section needed for the current task.
4. Do not read every workflow doc unless the task truly crosses all phases.

## Stage Reading Sets

| Stage | Read |
| --- | --- |
| App scale | `APP_BRIEF.md` summary, current user request |
| PRD update | `APP_BRIEF.md`, `PRD.md` relevant details |
| UX update | `APP_BRIEF.md`, `PRD.md` summary, `UX_SPEC.md` relevant screen |
| UI work | `UX_SPEC.md` relevant screen, `UI_REFERENCE.md`, latest screenshot/design target |
| Implementation | `IMPLEMENTATION_PLAN.md` slice, relevant PRD/UX details |
| Testing | `TEST_PLAN.md`, changed files, relevant stage docs |
| Debugging | failing command/log, changed files, minimal related docs |
| Handoff | summaries, latest decisions, current blockers, not full docs |

## New Thread Triggers

Recommend a new thread when:

- a full phase is complete
- conversation contains many screenshots, long logs, or long docs
- next work is UI polish or hard debugging
- requirements changed direction
- the agent would need to re-read many files to proceed
- context compaction has likely reduced answer quality

When recommending a new thread, also recommend using `handoff` if the next agent needs continuity.

## New Branch Triggers

Recommend a new branch when:

- starting an independently shippable feature
- doing risky refactor
- redesigning multiple screens
- changing persistence or data model
- changing test strategy or project structure

Do not recommend a new branch for:

- docs-only edits
- one small visual tweak
- throwaway exploration outside production files

## Handoff Contents

A handoff should include:

- current stage and app scale
- durable docs and paths
- latest decisions
- open questions
- suggested skills for next session
- verification already run
- explicit do-not-do-yet items

Do not duplicate full PRDs or plans inside the handoff. Reference paths instead.
