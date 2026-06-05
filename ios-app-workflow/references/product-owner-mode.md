# Product Owner Mode

Use this when the user starts from an idea, does not code, asks Codex to drive the workflow, or when product seriousness affects scope, testing, polish, or handoff.

## Purpose

Codex should actively move the product forward while keeping the user in control of high-impact decisions. Do not turn this into a long persona prompt.

## Role Switching

Switch professional lens by stage:

| Stage | Lens | Main responsibility |
| --- | --- | --- |
| Discovery / App Brief | product scope designer | Find the smallest real V1 and defer distracting scope. |
| PRD / UX Spec | product spec organizer | Turn decisions into clear features, states, flows, and non-goals. |
| UI Reference | visual direction translator | Convert references and mood into reusable UI rules without overbuilding a design system. |
| Implementation Plan | engineering collaborator | Split work into visible, testable slices with dependency gates. |
| Build | SwiftUI implementer | Use native patterns and keep implementation scoped to the approved slice. |
| Test | risk verifier | Prove the risky behavior with the cheapest credible check. |
| Polish | interface quality reviewer | Fix P0/P1 visual issues against an approved target, then stop before token-heavy subjective churn. |
| Handoff | continuity editor | Preserve state, decisions, verification, and next action for a fresh thread. |

Do not use one lens for every task. For example, do not act like a SwiftUI implementer during V1 scope definition, and do not act like a product strategist during focused UI polish.

## Launch Intent

Classify launch intent separately from app scale:

| Intent | Meaning | Workflow effect |
| --- | --- | --- |
| Exploring | User is testing an idea. | Keep docs light, prefer prototype/spec proof, skip release polish. |
| Personal use | User wants to use it themselves. | Make the core loop real, verify persistence and main flow, keep UI clean. |
| Share with others | User may show it to friends/users. | Add stronger polish, empty/error states, handoff docs, key screenshots. |
| Public launch | User wants TestFlight/App Store or public users. | Add release readiness, privacy/account decisions, broader testing. |

If intent is unknown, infer cautiously from the request and ask one short question only when it changes scope, testing, polish, accounts, or release work.

## Active Product Push

Codex should reduce "what should I ask next?" friction by doing these without waiting:

- identify the current stage and next stage
- separate V1, later, and do-not-do-yet scope
- point out missing decisions that block the next slice
- recommend the smallest real product slice
- route to a supporting skill only when its trigger is met
- end each major phase with the next concrete action

Do not use active push to add features, broaden tests, or invent requirements.

## Product Owner Checkpoints

Ask or pause for user choice when the decision affects:

- V1 scope or non-goals
- data persistence, backend, cloud, auth, payment, or API cost
- UI direction, visual reference, or design language
- testing depth beyond the default risk-driven boundary
- release path, TestFlight, App Store, privacy, or public sharing
- new thread, branch, or handoff after a phase boundary

Proceed without asking for:

- small copy, spacing, layout, or style fixes within an approved direction
- obvious empty/loading/error states
- narrow bug fixes that preserve product behavior
- document summary updates
- cheapest credible verification already allowed by `references/testing.md`

When asking, translate the technical issue into a product decision, give the recommended option, and state the cost of not choosing it.

## Visible Stage Checkpoints

Each implementation slice should have a user-visible or user-understandable proof:

- screen visible in simulator
- core flow can be tried
- saved data survives relaunch
- API path has mock or targeted live smoke
- screenshot confirms a key UI surface
- document decision is reflected in the durable docs

Avoid invisible technical work unless it directly unblocks a visible slice. If invisible work is necessary, explain the next visible result it enables.

## Real Product Quality Bar

For personal, share, or public intent, V1 may be small but should not be a fake demo:

- core product loop is real
- saved state that matters is preserved
- loading, empty, and error states exist for core paths
- key screens follow the approved UI direction
- polish focuses on key screens, not exhaustive whole-app sweeps
- handoff says how to use it, what is verified, what is deferred, and likely V2

For exploring intent, explicitly label prototype-only behavior and do not over-polish.

## Problem Options Rule

When blocked by a high-impact problem, do not silently pick a path. Present:

- 2-3 options
- recommended option
- tradeoff in plain language
- cheapest verification after the choice

For low-impact implementation details, choose the simplest approach consistent with existing project patterns.
