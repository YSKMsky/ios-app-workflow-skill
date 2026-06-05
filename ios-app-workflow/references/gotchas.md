# Gotchas

Use this when the workflow starts drifting, the agent overuses tools, or the work feels heavier than the request deserves.

## High-Risk Habits

- Do not use the full app-level workflow for a single feature, screen, bugfix, polish pass, or test change.
- Do not read full `APP_BRIEF.md`, `PRD.md`, `UX_SPEC.md`, `IMPLEMENTATION_PLAN.md`, and `TEST_PLAN.md` for every task.
- Do not start coding before V1 scope, data boundaries, and the next build slice are clear enough.
- Do not turn V2/V3 ideas into architecture unless the current V1 slice requires it.
- Do not treat "reserved cloud interface" as permission to call Supabase or build cloud sync.

## UI Gotchas

- Do not call polish skills when the user only has page structure or mood words.
- Do not use Figma by default when page structure, references, mood boards, generated concepts, SwiftUI previews, or simulator screenshots are enough.
- Do not compare a design image and app screenshot by raw dimensions before checking device frame, safe area, scale, orientation, and scroll position.
- Do not run full app screenshot sweeps for one small visible change.
- Do not keep polishing P2 subjective issues after P0/P1 issues are resolved and the user has no new visual target.

## Testing Gotchas

- Do not run simulator, screenshot, or UI tests for docs-only or planning-only edits.
- Do not use UI tests for subjective polish, early exploration, or manual-only reader gestures.
- Do not invoke performance, memory, or tracing skills without symptoms.
- Do not claim OpenAI/API behavior is verified without mock proof, live smoke proof, or a clearly stated block.

## Routing Gotchas

- Do not call skills just because their topic sounds related.
- Do not call OpenAI troubleshooting before an actual API failure.
- Do not call web frontend builder skills for final native SwiftUI implementation.
- Do not call `impeccable` before there is a rendered interface or concrete visual target.
- Do not call broad design ideation after the user has selected a visual direction.

## Product Owner Gotchas

- Do not silently decide high-impact scope, architecture, UI direction, account, cost, or release choices.
- Do not ask the user to approve low-impact implementation details that preserve approved direction.
- Do not hide uncertainty. State the decision, recommendation, and cheapest verification.
- Do not end a phase without a next concrete action or handoff recommendation.
