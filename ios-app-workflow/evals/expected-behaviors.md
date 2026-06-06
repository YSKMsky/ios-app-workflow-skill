# Expected Behaviors

Use these cases as a lightweight regression set for `ios-app-workflow`.

## Trigger

- Trigger when the user asks for app workflow, planning, V1 scope, UI direction, implementation planning, risk-driven testing, context control, or handoff for a SwiftUI iOS app.
- Do not trigger for isolated Xcode errors, performance profiling, memory leaks, README-only edits, or one-off SwiftUI fixes when a narrower skill applies.

## Process

- State app-level versus feature-level scope before acting.
- Load only the references needed for the current request.
- Do not read full APP_BRIEF, PRD, UX_SPEC, IMPLEMENTATION_PLAN, and TEST_PLAN by default.
- State current stage, expected artifact or action, routing, and verification boundary.

## Artifacts

- Initialize or resume with `docs/WORKFLOW_STATE.md` when the workflow will continue.
- Use app-level durable docs only when they reduce ambiguity or context cost.
- Use `docs/specs/spec{n}_<slug>.md` for bounded feature work.

## UI

- Normalize design image and app screenshot before judging mismatch.
- Use P0/P1/P2 design delta.
- Use the visual match rubric for "90%" requests.
- Stop after the iteration budget unless the user explicitly asks to continue.

## Testing

- Match completion claims to the cheapest credible proof.
- State skipped tests and why.
- Do not run broad simulator or screenshot sweeps for narrow low-risk changes.
