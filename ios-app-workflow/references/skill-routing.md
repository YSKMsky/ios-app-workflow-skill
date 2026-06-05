# Skill Routing

Route by trigger. Do not invoke skills just because they sound related.

Use this shape when adding a routing decision:

```text
Trigger:
Call:
Read before call:
Why:
Do not call when:
Verification:
```

## Product And Planning

| Trigger | Call | Do not call when |
| --- | --- | --- |
| User wants to clarify idea or worth | `office-hours` | Scope is already approved and implementation is requested. |
| Creative feature/design clarification before code | `superpowers:brainstorming` | Only summarizing existing docs. |
| PRD from existing conversation | `to-prd` | User still needs interview-style clarification. |
| Multi-step implementation plan from spec | `superpowers:writing-plans` | No approved spec or requirements yet. |
| Existing staged iOS project files | `ios-product-flow` | This new skill already provides enough lightweight orchestration. |

## iOS And SwiftUI

| Trigger | Call | Do not call when |
| --- | --- | --- |
| Build/run/debug in Simulator, logs, screenshots | `build-ios-apps:ios-debugger-agent` | Docs-only or no runtime proof needed. |
| Browser-visible simulator or SwiftUI previews | `build-ios-apps:ios-simulator-browser` | Normal build/log debugging is enough. |
| SwiftUI navigation, state, layout, controls | `build-ios-apps:swiftui-ui-patterns` | The issue is visual taste only on an already-built screen. |
| Large SwiftUI view or unclear Observation ownership | `build-ios-apps:swiftui-view-refactor` | The screen is small or only needs visual polish. |
| App Intents, Shortcuts, Siri, Spotlight, widgets | `build-ios-apps:ios-app-intents` | V1 app does not expose system surfaces. |
| SwiftUI jank or slow rendering | `build-ios-apps:swiftui-performance-audit` | No performance symptom exists. |
| Focused latency trace | `build-ios-apps:ios-ettrace-performance` | Code review or simple timing is enough. |
| Leaks, retain cycles, memory growth | `build-ios-apps:ios-memgraph-leaks` | No leak or memory-growth evidence exists. |

## UI And Visual Direction

| Trigger | Call | Do not call when |
| --- | --- | --- |
| Need design system search or SwiftUI UI guidance | `ui-ux-pro-max` | A concrete visual target already exists and only implementation remains. |
| Need image-based UI concepts | `Product Design:get-context` then `Product Design:ideate`, or `imagegen` | User only needs small native UI fix. |
| Existing rendered UI needs critique/polish | `impeccable critique/polish/layout/colorize/typeset` | There is no rendered interface or visual target. |
| Web landing page or portfolio taste | `design-taste-frontend` | Native mobile product UI or multi-step app workflow. |
| Web prototype from accepted concept | `build-web-apps:frontend-app-builder` | Final SwiftUI production implementation. |
| Test/debug rendered web prototype | `build-web-apps:frontend-testing-debugging` | Native iOS simulator validation. |

## OpenAI And Backend

| Trigger | Call | Do not call when |
| --- | --- | --- |
| Building/running/testing OpenAI API-backed app behavior | `openai-developers:openai-platform-api-key` first | Docs-only or static UI work. |
| Current OpenAI docs, model choice, API guidance | `openai-docs` | A concrete runtime API error already exists. |
| OpenAI API request failed | `openai-developers:openai-api-troubleshooting` | No request has been made yet. |
| Agents SDK app or agent service | `openai-developers:agents-sdk` | Normal iOS app calling OpenAI API directly. |
| Supabase Auth/DB/Storage/RLS/Edge Functions | `supabase:supabase` | V1 only reserves future cloud interface and stores locally. |

## Debugging And Verification

| Trigger | Call | Do not call when |
| --- | --- | --- |
| Any bug, test failure, unexpected behavior | `superpowers:systematic-debugging` | The task is planned work without failure. |
| Hard bug needing reproducible loop | `diagnose` | Simple compile error with clear fix. |
| New feature/bugfix where tests should drive code | `superpowers:test-driven-development` | Throwaway prototype or user explicitly skips TDD. |
| Before claiming complete/fixed/passing | `superpowers:verification-before-completion` | Only giving a plan or asking a question. |

## Handoff, GitHub, And Shipping

| Trigger | Call | Do not call when |
| --- | --- | --- |
| Context is long or new thread is recommended | `handoff` | Existing docs already capture everything needed. |
| User wants commit/push/PR | `github:yeet` | User only asked for local edits. |
| GitHub Actions PR checks fail | `github:gh-fix-ci` | Local test failure not connected to PR checks. |

## Overuse Guards

- Do not call UI polish skills for page structure only.
- Do not call web prototype skills for final SwiftUI implementation.
- Do not call simulator skills for docs-only work.
- Do not call Supabase for reserved future cloud support.
- Do not call performance or memory tools without symptoms.
- Do not call OpenAI troubleshooting before an actual API failure.
