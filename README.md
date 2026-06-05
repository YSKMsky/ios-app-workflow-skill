# iOS App Workflow

A Codex skill for guiding non-coding users through staged iOS app development.

This skill helps Codex decide what to do next when building tiny, small, or medium SwiftUI apps: clarify scope, create bounded docs, route to the right skills, avoid over-testing, handle UI work without defaulting to Figma, and keep context under control.

## What It Does

`ios-app-workflow` acts as an orchestration layer for iOS app projects.

It helps Codex:

- classify app scale as `tiny`, `small`, or `medium`
- decide which workflow stage the project is in
- create short PRD, UX, implementation, and test documents
- route UI work to the right design or SwiftUI skill
- decide when simulator, screenshot, UI test, or manual validation is actually needed
- avoid reading every long document on every task
- suggest when to open a new thread, create a branch, or generate a handoff

## Core Use Case

This skill is designed for a user who does not directly write code but wants Codex to help build an iOS app from idea to working product.

It is especially useful when:

- Codex jumps into code too early
- UI polish consumes too many tokens
- testing becomes too broad or unfocused
- it is unclear which skill should be invoked
- long docs and screenshots cause context bloat
- a project needs a simple workflow, not enterprise-scale process

## Skill Structure

```text
ios-app-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── app-scale.md
    ├── main-workflow.md
    ├── ui-workflow.md
    ├── testing.md
    ├── skill-routing.md
    ├── context-control.md
    └── doc-templates.md
```

## Workflow

The main workflow is:

```text
Idea
→ App Scale
→ App Brief
→ PRD
→ UX Spec
→ UI Reference
→ Implementation Plan
→ Build
→ Test
→ Polish
→ Release or Handoff
```

The UI workflow is handled separately:

```text
UI Input Classifier
→ UI Reference Pack
→ Visual Direction
→ SwiftUI Implementation
→ Screenshot or Diff Debug
→ Polish
```

## App Scale

The skill classifies apps using four dimensions:

- `Scope`: screens, features, models, navigation depth
- `Risk`: API, auth, payments, backend, persistence, data loss
- `UI Complexity`: custom UI, fidelity, animation, device precision
- `Validation Cost`: simulator, screenshots, UI tests, manual-only interactions

This classification controls how much planning, documentation, testing, and verification is appropriate.

## UI Routing

The skill distinguishes between:

- page structure only
- mood board or references
- generated UI concept image
- existing design image to match
- existing SwiftUI screen needing polish
- screenshot mismatch caused by safe area, device frame, black border, or viewport differences

It can route to skills such as:

- `ui-ux-pro-max`
- `impeccable`
- `Product Design:get-context`
- `Product Design:ideate`
- `imagegen`
- `swiftui-ui-patterns`
- `swiftui-view-refactor`
- `ios-debugger-agent`
- `ios-simulator-browser`

It also defines when not to use web/frontend skills for native SwiftUI production work.

## Testing Strategy

Testing is risk-driven, not fixed.

Examples:

| Change | Verification |
| --- | --- |
| Docs only | Review diff, skip build and simulator |
| Small copy or spacing | Skip full simulator flow unless visible risk is high |
| Navigation or modal | Run targeted simulator path |
| Local persistence | Test save, relaunch, and data access |
| OpenAI API flow | Use credential gate, mock or targeted live smoke |
| Final UI polish | Screenshot key screens only |

The goal is to verify real risk without wasting tokens on unnecessary tests.

## Context Control

Every durable workflow document should include:

```text
Context Summary
Key Decisions
Open Questions
Details
```

Codex should read summaries first, then only the relevant detail section for the current task.

The skill also recommends new threads, branches, or handoff documents when context becomes too large or a major phase is complete.

## Installation

Place the `ios-app-workflow` folder in your Codex skills directory:

```bash
~/.codex/skills/ios-app-workflow
```

Then invoke it explicitly:

```text
Use $ios-app-workflow to classify this iOS app, choose the current stage, route to the right skills, and keep docs and context bounded.
```

## Status

First version focused on:

- staged iOS app workflow
- UI routing without Figma dependency
- risk-driven testing
- context and handoff control
- skill routing boundaries for iOS, UI, OpenAI, debugging, and frontend prototype work

