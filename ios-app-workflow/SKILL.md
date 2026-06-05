---
name: ios-app-workflow
description: Guide Codex through staged iOS app work for non-coding users building tiny, small, or medium SwiftUI apps. Use when starting, planning, continuing, designing, polishing, testing, debugging, or handing off an iOS app project, especially when Codex must classify app scale, keep PRD/UX/test docs short, route to the right iOS/UI/OpenAI/debug skills, decide what tests to skip, avoid Figma-heavy workflows, or control context, branch, and thread boundaries.
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
3. If app scale is unknown, read `references/app-scale.md` and classify `tiny`, `small`, or `medium`.
4. Read only the reference files needed for the current request. Do not load every reference by default.
5. State the current stage, scale, required output, likely skill routing, and verification boundary before acting.

## Reference Loading Map

Read these files only when their condition applies:

| Reference | Read when |
| --- | --- |
| `references/app-scale.md` | App size, document depth, testing depth, or V1 scope is unclear. |
| `references/main-workflow.md` | Starting or continuing the staged app workflow. |
| `references/ui-workflow.md` | UI direction, mood board, reference images, design image matching, screenshot mismatch, or polish is involved. |
| `references/testing.md` | Choosing verification commands, simulator use, screenshots, UI tests, or explicit skips. |
| `references/skill-routing.md` | Deciding which skill/plugin to invoke, or avoiding over-invocation. |
| `references/context-control.md` | Docs are long, context is large, phase is ending, or thread/branch/handoff may be needed. |
| `references/doc-templates.md` | Creating or updating workflow docs. |

## Operating Rules

- Prefer one clear gate at a time. Ask one question when a blocked decision would change scope, data risk, UI direction, or testing depth.
- Do not start large implementation before the current phase has enough brief/spec/plan context, unless the user explicitly asks to skip planning.
- Keep docs short. Each durable doc must have `Context Summary`, `Key Decisions`, `Open Questions`, and `Details`.
- Read summaries before details. Do not read full PRD, UX spec, implementation plan, and test plan "just in case".
- Use risk-driven testing. Skipping a test is allowed when the skip is explicit and justified by change type.
- Treat UI as a separate track. Do not call polish skills before there is a visual target or rendered interface to polish.
- Figma is not the default. Use page structure, UI references, mood boards, generated concept images, SwiftUI previews, and simulator screenshots first.
- For OpenAI-backed app work, use the OpenAI credential gate before implementing or testing live API behavior.
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
| App scale | `tiny`, `small`, or `medium` classification | Required before major planning. |
| App brief | `APP_BRIEF.md` | Short product goal and V1 boundary. |
| PRD | `PRD.md` | Features, non-goals, success criteria. |
| UX spec | `UX_SPEC.md` | Screens, states, flows, edge cases. |
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
