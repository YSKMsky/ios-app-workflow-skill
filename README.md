# iOS App Workflow Skill

Codex skill for guiding non-coding users through staged SwiftUI iOS app development with scoped docs, UI routing, risk-driven testing, and context control.

## What This Is

`ios-app-workflow` is an orchestration skill for building tiny, small, and medium iOS apps with Codex.

It is designed for product owners who do not write code directly, but want Codex to help move an iOS app from idea to usable V1 without jumping into code too early, overloading the context window, over-polishing UI, or running unnecessary tests.

## When To Use It

Use this skill when Codex needs to guide a SwiftUI iOS app through:

- idea clarification and V1 scope
- app scale classification
- short product, UX, implementation, and test docs
- UI direction without defaulting to Figma
- feature-level specs
- skill routing for iOS, UI, OpenAI, debugging, and handoff
- risk-driven testing and explicit test skips
- context boundaries, thread handoff, and branch advice

Do not use it for isolated Xcode errors, performance profiling, memory leaks, or one-off SwiftUI fixes when a narrower iOS skill applies.

## Core Principles

- **Product owner control**: Codex can recommend and execute, but should not silently decide high-impact scope, architecture, UI direction, cost, account, or release choices.
- **Progressive disclosure**: `SKILL.md` stays lean. Detailed rules live in references and examples that are loaded only when needed.
- **Risk-driven testing**: verification should match the risk of the change, not run every possible test by default.
- **UI as a separate track**: create a visual target before polish, and avoid Figma-heavy workflows unless truly needed.
- **No workflow railroading**: feature-level work should not reopen the full app workflow.
- **Real V1 quality**: V1 may be small, but the approved core loop should be real, usable, visually coherent, persistent when required, and verified by the cheapest credible proof.

## Skill Structure

```text
ios-app-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── config.json
├── examples/
│   └── workflow-examples.md
├── references/
│   ├── app-scale.md
│   ├── context-control.md
│   ├── doc-templates.md
│   ├── feature-spec-mode.md
│   ├── gotchas.md
│   ├── main-workflow.md
│   ├── output-modes.md
│   ├── product-owner-mode.md
│   ├── skill-routing.md
│   ├── testing.md
│   └── ui-workflow.md
└── scripts/
    └── validate-skill.py
```

## Main Workflow

The app-level workflow is:

```text
Product Owner Mode
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

For smaller tasks, the skill uses Feature Spec Mode instead of reopening the full app workflow.

## Feature-Level Work

Feature Spec Mode is used for:

- one feature
- one screen
- one UI polish pass
- one bugfix
- one testing, routing, or context-control change

It creates a bounded feature spec under `docs/specs/` and only syncs main docs when a durable app-level decision changes.

Low-risk, reversible tasks can use a fast path: Codex states the recommended path, explains why it is safe, names the cheapest verification, and proceeds unless a product-owner checkpoint is triggered.

## UI Workflow

The UI workflow supports:

- page structure only
- mood boards and visual references
- generated UI concept images
- existing design image matching
- app screenshot versus design target debugging
- focused polish on rendered SwiftUI screens

The skill intentionally avoids calling polish tools before there is a concrete rendered interface or visual target.

## Testing Strategy

Testing is risk-driven:

| Change | Default verification |
| --- | --- |
| Docs or planning only | Diff/read review |
| Copy or small spacing | Build only if code changed; screenshot only when visible risk is high |
| Navigation, tab, sheet, modal | Targeted simulator path |
| State or data flow | Unit test or targeted runtime scenario |
| Local persistence | Save, relaunch, and data-access scenario |
| OpenAI/API integration | Credential gate, mock or targeted live smoke, error-state check |
| Final UI polish | Key screenshots only |

Skipped tests should be explicit and justified.

## Gotchas

The high-signal rules live in `references/gotchas.md`.

Examples:

- Do not use the full app workflow for a single feature or polish pass.
- Do not read every durable doc for every task.
- Do not compare screenshots by raw image dimensions before checking device frame and safe area.
- Do not call Supabase just because future cloud support is reserved.
- Do not run simulator or screenshots for docs-only changes.
- Do not call `impeccable` before there is a rendered interface or concrete visual target.

## Configuration

`config.json` stores stable user preferences so Codex does not repeatedly ask the same questions:

- default language: Traditional Chinese
- user coding level: non-coding
- default platform: iOS SwiftUI
- Figma default: false
- default validation style: risk-driven
- preferred UI direction: quiet, clear, refined, not SaaS-like

## Validation

Run the validation script before committing or publishing changes:

```bash
ios-app-workflow/scripts/validate-skill.py
```

It checks:

- `SKILL.md` YAML frontmatter
- trigger-oriented description
- negative trigger boundary
- referenced files in `references/` and `examples/`
- `config.json`
- forbidden files such as `.DS_Store` and skill-package `README.md`
- `SKILL.md` length

## Installation

Copy the `ios-app-workflow` folder into your Codex skills directory:

```bash
~/.codex/skills/ios-app-workflow
```

Then invoke it explicitly:

```text
Use $ios-app-workflow to guide this SwiftUI iOS app from idea to V1, keep docs short, route skills carefully, and choose risk-driven verification.
```

## Repository Description

Suggested GitHub description:

```text
Codex skill for guiding non-coding users through staged SwiftUI iOS app development with scoped docs, UI routing, risk-driven testing, and context control.
```
