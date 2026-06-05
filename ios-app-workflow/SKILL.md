---
name: ios-app-workflow
description: Use when a non-coding user asks Codex to guide a SwiftUI iOS app through idea clarification, V1 scope, short planning docs, UI reference, implementation planning, risk-driven testing, skill routing, context boundaries, or handoff. Do not use for isolated Xcode errors, performance profiling, memory leaks, or one-off SwiftUI fixes when a narrower iOS skill applies.
---

# iOS App Workflow

## Purpose

Use this skill as an orchestration layer, not as an iOS encyclopedia.
It keeps Codex from jumping into code too early, over-reading docs, over-testing small changes, or calling heavyweight UI skills at the wrong time.

## First Action

1. Read `AGENTS.md` if it exists.
2. Identify the current request type:
   - new app or new feature planning
   - continuing an existing iOS project
   - UI direction, design matching, or polish
   - implementation planning or SwiftUI build
   - testing, debugging, or release handoff
3. Decide whether this is app-level or feature-level work:
   - app-level change: new app, V1 scope, core workflow, data model, backend, auth, payment, or product positioning
   - feature-level change: one feature, screen, UI polish pass, bugfix, testing change, routing change, or context-control change
4. If app scale is unknown for app-level work, read `references/app-scale.md` and classify `tiny`, `small`, or `medium`.
5. Read only the reference files needed for the current request. Do not load every reference by default.
6. Read `config.json` before asking for a recurring user preference already stored there.
7. State the current stage, scale or feature scope, required output, likely skill routing, and verification boundary before acting.

## Reference Loading Map

Read these files only when their condition applies:

| Reference | Read when |
| --- | --- |
| `references/app-scale.md` | App size, document depth, testing depth, or V1 scope is unclear. |
| `references/product-owner-mode.md` | Product seriousness, user control, visible checkpoints, or launch/share quality is unclear. |
| `references/main-workflow.md` | Starting or continuing the staged app workflow. |
| `references/feature-spec-mode.md` | The task is feature-level rather than app-level. |
| `references/ui-workflow.md` | UI direction, mood board, reference images, design image matching, screenshot mismatch, or polish is involved. |
| `references/testing.md` | Choosing verification commands, simulator use, screenshots, UI tests, or explicit skips. |
| `references/skill-routing.md` | Deciding which skill/plugin to invoke, or avoiding over-invocation. |
| `references/context-control.md` | Docs are long, context is large, phase is ending, or thread/branch/handoff may be needed. |
| `references/doc-templates.md` | Creating or updating workflow docs. |
| `examples/workflow-examples.md` | The agent needs a concrete model for applying the workflow to a realistic request. |
| `references/gotchas.md` | The workflow is drifting, over-reading, over-testing, over-polishing, or over-routing skills. |
| `references/output-modes.md` | The expected deliverable format is unclear or differs by artifact type. |

## Operating Rules

- Prefer one clear gate at a time. Ask one question when a blocked decision would change scope, data risk, UI direction, or testing depth.
- Treat the user as product owner: recommend and execute, but do not silently decide high-impact scope, architecture, UI direction, account, cost, or release choices.
- Do not start large implementation before the current phase has enough brief/spec/plan context, unless the user explicitly asks to skip planning.
- Keep docs short. Each durable doc must have `Context Summary`, `Key Decisions`, `Open Questions`, and `Details`.
- Read summaries before details. Do not read full PRD, UX spec, implementation plan, and test plan "just in case".
- Use risk-driven testing. Skipping a test is allowed when the skip is explicit and justified by change type.
- Avoid railroading the workflow. Skip irrelevant stages when the current task is narrow, and state the skipped boundary.
- Treat UI as a separate track. Do not call polish skills before there is a visual target or rendered interface to polish.
- Use Feature Spec Mode for feature-level work instead of reopening the full app workflow.
- Figma is not the default. Use page structure, UI references, mood boards, generated concept images, SwiftUI previews, and simulator screenshots first.
- For OpenAI-backed app work, use the OpenAI credential gate before implementing or testing live API behavior.
- Quality bar: V1 may be small, but the approved core loop must be real, usable, visually coherent, locally persistent when required, and verified by the cheapest credible proof.
- Before claiming completion, run the freshest verification that proves the claim, or state exactly what remains unverified.

## Minimal Stage Loop

For each stage:

1. Name the stage and app scale.
2. Name the smallest needed context to read.
3. Name the expected artifact or action.
4. Route to another skill only if its trigger is met.
5. Verify using the cheapest credible check.
6. Update the relevant summary or suggest handoff/new thread when context is getting heavy.

## Stage Summary

| Stage | Output | Default depth |
| --- | --- | --- |
| Product owner mode | launch intent and decision checkpoints | Required when starting from an idea or changing product seriousness. |
| App scale | `tiny`, `small`, or `medium` classification | Required before major planning. |
| App brief | `APP_BRIEF.md` | Short product goal and V1 boundary. |
| PRD | `PRD.md` | Features, non-goals, success criteria. |
| UX spec | `UX_SPEC.md` | Screens, states, flows, edge cases. |
| Feature spec | `docs/specs/spec{n}_<slug>.md` | Only for feature-level work. |
| UI reference | `UI_REFERENCE.md` | Only when visual direction matters. |
| Implementation plan | `IMPLEMENTATION_PLAN.md` | Build order and boundaries. |
| Test plan | `TEST_PLAN.md` | Required tests and explicit skips. |
| Build/test/polish | Code, screenshots, logs, or review notes | Risk-driven. |
| Handoff | temp handoff document or thread advice | When context is large or phase ends. |

## Done Criteria

Before ending a workflow turn, report:

- current stage and scale
- artifacts created or updated
- skills invoked or intentionally not invoked
- verification run, skipped, or blocked
- next recommended stage
- whether a new thread, branch, or handoff is recommended
- any unresolved risk, skipped step, or important uncertainty
