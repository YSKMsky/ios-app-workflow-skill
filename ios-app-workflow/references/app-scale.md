# App Scale Classifier

Use this before choosing document depth, UI validation depth, testing depth, or thread strategy.

## Contents

- Dimensions
- Scale Rules
- English Learning App Acceptance Case

## Dimensions

Classify across four dimensions:

| Dimension | Look for |
| --- | --- |
| Scope | Screen count, feature count, data models, navigation depth. |
| Risk | API calls, auth, payments, backend, persistence, data loss, privacy. |
| UI Complexity | Custom UI, visual fidelity, animations, responsive/device precision, reader/editor surfaces. |
| Validation Cost | Simulator need, screenshots, UI tests, manual-only interactions, API mocks. |

## Scale Rules

### tiny

Use for:

- 1-2 screens
- no backend or external API
- no durable user data, or trivial local settings only
- standard SwiftUI controls
- low visual precision

Docs:

- `APP_BRIEF.md`
- short `TEST_PLAN.md` or test notes

Testing:

- build or compile check
- simulator only when runtime behavior changed
- screenshots only for visible UI risk
- no UI tests by default

### small

Use for:

- 3-5 screens
- local persistence or simple API usage
- moderate navigation and state
- consistent visual language needed
- limited custom components

Docs:

- 5 workflow docs, each short
- optional `UI_REFERENCE.md` for important visual work

Testing:

- targeted build
- simulator for navigation, persistence, or runtime paths
- screenshots for key screens only
- UI tests only for fragile repeated core journeys

### medium

Use for:

- 5+ important surfaces, or fewer surfaces with meaningful state/API risk
- OpenAI/API integration
- backend architecture or reserved cloud boundary
- local persistence with saved user content
- reader/editor/note/highlight surfaces
- high UI taste or design fidelity requirements

Docs:

- 5 workflow docs
- `UI_REFERENCE.md` for UI-heavy work
- explicit V1/V2/V3 boundaries

Testing:

- build plus targeted simulator flows
- persistence relaunch scenario when local saved data matters
- screenshots for key screens and UI polish stages
- mocked or targeted runtime checks for API flows
- avoid exhaustive UI tests unless a core journey is fragile

## English Learning App Acceptance Case

Classify the V1 English learning app as `medium` when it includes:

- OpenAI API generated article, questions, expressions, and feedback
- read/write learning loop
- local saved articles, expressions, answers, AI feedback, notes, highlights, and underlines
- no V1 login, payment, or cloud persistence
- cloud interface reserved for later
- high UI taste requirements

Testing impact:

- skip cloud sync, auth, and payment tests in V1
- test local save and relaunch behavior
- test API behavior with mocks or a targeted live smoke only after credential gate
- use screenshots only for key screens or polish, not every minor copy change
