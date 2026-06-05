# UI Workflow

Use this when UI direction, reference images, generated concepts, SwiftUI implementation, screenshots, or visual polish are involved.

## Contents

- UI Input Classifier
- Low-Cost UI Reference Pack
- Recommended UI Paths
- Page structure only
- Mood board or visual references
- Generated concept image selected
- Existing design image, agent must modify app to match
- App screenshot differs from design target
- Existing SwiftUI surface needs polish
- Web Frontend Skills Boundary
- Manual-Only Interaction Rule

## UI Input Classifier

Classify the user's current input:

1. Page structure only
2. Mood words only
3. Web/app references or mood board
4. Generated UI concept image
5. Existing design image to match
6. Existing SwiftUI screen needing polish
7. App screenshot differs from design target

Do not call a polish skill until there is something concrete to polish.

## Low-Cost UI Reference Pack

Create or update `UI_REFERENCE.md` for important UI work. Keep it short.

Required sections:

- Page Structure
- Mood / Visual Direction
- References
- Do Not Want
- Key Screens
- Reusable Visual Rules

Use this instead of a full design system for `small` and most `medium` apps.

## Recommended UI Paths

### Page structure only

Use when the user has screens and hierarchy but no visual direction.

Process:

1. Clarify key screens and primary workflow.
2. Use `ui-ux-pro-max` when useful to search a lightweight design system or SwiftUI stack guidance.
3. Create `UI_REFERENCE.md`.
4. Generate 1-3 visual concepts only if the user wants to see options.
5. Do not call `impeccable polish` yet.

### Mood board or visual references

Use when the user has references from the web or apps.

Process:

1. Inspect actual images or URLs when available.
2. Extract visual rules, not just adjectives.
3. Update `UI_REFERENCE.md`.
4. Use Product Design `get-context` then `ideate`, or `imagegen`, when the next step is visual concept exploration.

### Generated concept image selected

Use when the user selected an AI-generated UI image as the direction.

Process:

1. Treat the image as visual target, not production code.
2. Extract tokens: color, type scale, density, radius, spacing, component style.
3. Implement in SwiftUI using `swiftui-ui-patterns`.
4. Use `impeccable` only after a rendered SwiftUI surface exists.

Do not:

- treat `Product Design:image-to-code` output as final SwiftUI code
- rebuild native app UI as a web app unless the goal is a throwaway prototype

### Existing design image, agent must modify app to match

Use this when a design image exists and the native app screen must be adjusted against it.

Process:

1. Confirm target:
   - source design image
   - target app screen
   - device and viewport
   - whether the reference includes device frame, black border, or only screen content
2. Normalize before judging:
   - identify safe area
   - identify device frame and black border
   - compare content area to content area
   - do not judge mismatch only from different image dimensions
3. Create a Design Delta:
   - P0: missing structure, wrong content, blocked flow
   - P1: obvious layout, spacing, typography, color, density, or hierarchy mismatch
   - P2: subtle polish
4. Pick the skill:
   - `swiftui-ui-patterns` if the screen is not built yet
   - `impeccable polish/layout/colorize/typeset` if a rendered interface exists
   - `ios-debugger-agent` or `ios-simulator-browser` for native screenshot proof
   - `frontend-testing-debugging` only for web prototypes
5. Edit in small passes:
   - one pass for layout
   - one pass for typography
   - one pass for color and material
   - one pass for spacing and density
6. Verify with a targeted screenshot when the interaction is agent-operable.
7. Stop when P0/P1 are resolved and only subjective P2 remains.

### App screenshot differs from design target

First ask whether the mismatch is real UI or capture mismatch.

Check:

- device frame included vs not included
- black border included vs not included
- safe area included vs not included
- status/nav bars
- screenshot scale
- simulator device model
- scroll position
- dynamic type or appearance mode

Only edit UI after capture mismatch is ruled out.

### Existing SwiftUI surface needs polish

Use:

- `impeccable critique` for diagnosis
- `impeccable polish` for final pass
- `impeccable layout`, `colorize`, or `typeset` for focused fixes

Use `ios-debugger-agent` when the polish must be verified in Simulator.

Do not:

- rerun broad concept ideation when the direction is already selected
- run full app screenshot sweeps for one small visible change

## Web Frontend Skills Boundary

These skills may help with concepts or prototypes, but they are not native SwiftUI production skills.

| Skill | Use in iOS workflow | Do not use for |
| --- | --- | --- |
| `ui-ux-pro-max` | Design system search, SwiftUI stack guidance, UI heuristics. | Automatic implementation or final polish by itself. |
| `design-taste-frontend` | Reference-only for landing pages, portfolios, and anti-slop web redesign rules. | Native mobile product UI or multi-step app screens. |
| `frontend-app-builder` | Optional high-cost web prototype from accepted visual concept. | Final SwiftUI implementation. |
| `frontend-testing-debugging` | Testing/debugging a web prototype. | Native iOS simulator validation. |

## Manual-Only Interaction Rule

If Codex cannot operate an interaction reliably, do not force screenshot or UI test validation.

Examples:

- selecting text inside a reader
- highlight/underline gesture that simulator automation cannot perform
- complex swipe/drag controls not exposed through accessible elements

Use:

- implementation-level checks
- state inspection
- manual checklist
- user-provided screenshot/video feedback
