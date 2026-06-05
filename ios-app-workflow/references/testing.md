# Risk-Driven Testing

Use the cheapest credible verification for the change. Do not run expensive tests by reflex.

## Decision Table

| Change type | Required verification | Explicit skips |
| --- | --- | --- |
| Docs, skill, prompt, planning only | diff/read review | build, simulator, screenshot, UI test |
| Copy only | build only if code changed | simulator, screenshot unless visible risk is high |
| Small spacing/color tweak | targeted screenshot if key UI or high taste surface | full simulator flow, UI tests |
| SwiftUI layout change | build plus targeted screenshot when practical | full app screenshot sweep |
| Navigation, tab, sheet, modal | simulator targeted path | unrelated screens, broad UI test |
| State/data flow | unit test or targeted runtime scenario | screenshot unless UI changed |
| Local persistence | save, relaunch, data accessible scenario | cloud sync, auth, payment tests |
| OpenAI/API integration | credential gate, mock or targeted live smoke, error-state check | broad simulator sweep unless UI changed |
| Backend/cloud/Auth/RLS | backend-specific skill and tests | local-only assumptions |
| Performance symptom | code-first audit, then profile if evidence needed | ETTrace by default |
| Memory/leak symptom | memgraph only when leak or growth evidence exists | memory tooling by default |
| Final UI polish | key screenshots only | exhaustive UI test unless core journey is fragile |

## Simulator Use

Use simulator when:

- navigation or modal behavior changed
- runtime state is important
- local persistence must be proven
- API flow must be observed
- visual fidelity must be checked on device-sized surface

Skip simulator when:

- only docs changed
- only planning changed
- no executable code changed
- change is isolated and covered by a faster test

## Screenshot Use

Use screenshots when:

- visual layout, density, type, color, safe area, or design matching matters
- final polish is being evaluated
- a key screen changed

Skip screenshots when:

- no visible UI changed
- interaction cannot be performed by the agent
- comparing full image dimensions would be misleading due to device frame or safe area mismatch

Before comparing screenshots:

- normalize device frame and content area
- match device model and orientation
- match appearance mode
- match scroll position

## UI Tests

Use UI tests sparingly.

Good candidates:

- fragile core journeys repeated often
- release-critical flows
- regression for a bug that can be automated reliably

Skip by default for:

- early UI exploration
- subjective polish
- one-off layout changes
- manual-only reader gestures

## V1 English Learning App Testing Boundary

For the V1 read/write learning loop:

Required:

- app opens to Read page after relaunch
- saved article, expression, answer, feedback, note, highlight, and underline remain accessible
- generated article/questions/expressions/feedback path has mock or targeted live smoke
- reader, questions, expression detail, and saved review surfaces have key visual checks

Skipped:

- cloud sync tests
- login tests
- payment tests
- card feature tests
- listening feature tests
- exhaustive UI automation for text selection/highlight if agent cannot operate it
