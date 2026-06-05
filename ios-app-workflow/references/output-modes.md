# Output Modes

Use this when choosing the right deliverable shape. Different outputs should not use the same level of detail.

## App-Level Docs

Use for `APP_BRIEF.md`, `PRD.md`, `UX_SPEC.md`, `IMPLEMENTATION_PLAN.md`, and `TEST_PLAN.md`.

- Keep short and decision-oriented.
- Put `Context Summary`, `Key Decisions`, `Open Questions`, and `Details` at top level.
- Update summaries after phase changes.
- Do not copy entire conversation history into docs.

## Feature Spec

Use `docs/specs/spec{n}_<slug>.md` for one feature, screen, bugfix, polish pass, or testing/routing/context-control change.

- Capture the bounded change.
- Reference main docs instead of rewriting them.
- Include goals, non-goals, implementation boundaries, testing notes, and acceptance criteria.
- Sync main docs only when a durable app-level decision changes.

## UI Reference

Use `UI_REFERENCE.md` to preserve visual direction.

- Keep it compact.
- Store page structure, mood, references, do-not-want, key screens, and reusable visual rules.
- Do not turn it into a large design system unless the app scale and user request require it.

## Test Plan

Use `TEST_PLAN.md` to make risk-driven verification explicit.

- List required tests.
- List skipped tests and why.
- Prefer the cheapest credible proof for the current change.
- Do not test V2/V3 features that are explicitly deferred.

## Handoff

Use handoff when context is large, a phase ends, or a new thread is recommended.

- Include current stage, scale, durable docs, latest decisions, open questions, suggested skills, verification already run, and do-not-do-yet items.
- Reference files instead of duplicating full docs.
- Make the next action clear enough for a fresh thread to resume quickly.

## Final Answer

For normal workflow completion, report:

- what changed
- what was verified
- what was skipped or remains uncertain
- current stage
- next recommended action

Keep it concise. Do not restate full PRDs, plans, or long logs.
