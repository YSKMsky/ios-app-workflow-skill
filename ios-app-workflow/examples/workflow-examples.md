# Workflow Examples

Use these as compact models. Do not copy them verbatim when the user's project differs.

## From Idea To V1

User says:

```text
I want to build an iOS English learning app from zero. I do not code. It should generate articles, questions, useful expressions, feedback, and saved review.
```

Agent should:

1. Stage: app-level discovery.
2. Read: `references/app-scale.md`, `references/product-owner-mode.md`, then `references/main-workflow.md`.
3. Classify: likely `medium` if OpenAI API, local persistence, multiple saved content types, and polished UI matter.
4. Launch intent: infer `personal use` or ask one short question if share/public quality changes testing and polish depth.
5. Recommend V1: one real read/write learning loop with local saved articles, expressions, answers, feedback, and reader notes.
6. Defer: cards, listening, login, payment, cloud sync, and broad release work.
7. Output: short `APP_BRIEF.md`, `PRD.md`, `UX_SPEC.md`, `IMPLEMENTATION_PLAN.md`, and `TEST_PLAN.md`.
8. Verification boundary: simulator for main flow and persistence, targeted key screenshots, no login/payment/cloud tests.

Do not:

- start coding before V1 scope and saved/discarded data are clear
- build listening/cards because they are product ideas
- call Supabase only because future cloud support is mentioned

## Page Structure Only, No Figma

User says:

```text
I only have screen hierarchy for Read, Review, Card, Listening, and Settings. I want a quiet, clear, refined UI.
```

Agent should:

1. Read `references/ui-workflow.md`.
2. Classify input as page structure plus mood direction.
3. Create or update `UI_REFERENCE.md` with page structure, mood, do-not-want, key screens, and reusable visual rules.
4. If user wants concepts, route to Product Design `get-context` then `ideate`, or `imagegen`.
5. Use `swiftui-ui-patterns` only when implementing native screens.

Do not call `impeccable polish` yet, because there is no rendered UI or selected visual target.

## Single UI Polish Pass

User says:

```text
This existing Reader screen feels cluttered. Make it calmer and more premium.
```

Agent should:

1. Treat as feature-level work.
2. Read `references/feature-spec-mode.md`, `references/ui-workflow.md`, and relevant `UI_REFERENCE.md`.
3. If a screenshot exists, use `impeccable critique` or focused polish routing.
4. Make a small pass on layout, typography, spacing, or color, based on the diagnosed issue.
5. Verify with one targeted screenshot if the screen is agent-operable.

Do not reopen all app-level docs or run a full simulator screenshot sweep.

## Design Image Versus App Screenshot

User says:

```text
The app screenshot does not match this design image. Fix it.
```

Agent should:

1. Read `references/ui-workflow.md`.
2. Confirm target design, app screen, device, and whether each image includes device frame or only screen content.
3. Normalize comparison for safe area, black border, scale, orientation, appearance mode, scroll position, and status/nav bars.
4. Create a Design Delta: P0 structural, P1 obvious visual mismatch, P2 subjective polish.
5. Edit in focused passes and verify with a targeted screenshot.

Do not judge UI mismatch from raw image dimensions alone.
