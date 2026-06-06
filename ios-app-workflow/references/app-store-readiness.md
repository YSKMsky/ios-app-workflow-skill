# App Store Readiness

Use this as a release-risk checklist, not as an App Store encyclopedia.

## Load Only When

Read this file only when:

- launch intent is public launch
- user mentions TestFlight, App Store, App Review, privacy policy, subscription, payment, login, account deletion, UGC, kids, health, finance, gambling, third-party AI, analytics, tracking, metadata, screenshots, or review notes
- a feature decision could affect release eligibility

Do not load this file for early personal prototypes unless the user asks about release risk.

## Rule

Do not reject or remove a feature solely because it may affect review.

Instead:

1. classify the release risk
2. explain the product decision in plain language
3. suggest the safest implementation path
4. mark required release work
5. continue local or personal implementation if launch intent is not public

## Risk Levels

### P0 Blocker

Use for likely prohibited, illegal, unavailable-entitlement, or submission-blocking issues.

Examples:

- app crashes or cannot complete the reviewed core flow
- placeholder content or incomplete binary
- broken required login
- required backend unavailable for review
- feature requires unavailable license, right, or entitlement

### P1 Release Requirement

Use for work likely needed before TestFlight or App Review.

Examples:

- privacy policy needed
- permission wording needed
- account deletion needed when account creation exists
- test account or review notes needed
- third-party AI or data sharing disclosure needed
- App Store metadata and screenshots must match actual behavior

### P2 Advisory

Use for non-blocking release polish.

Examples:

- HIG or taste issue
- onboarding clarity
- metadata improvement
- screenshot polish

## APP_STORE_READINESS.md Template

```markdown
# APP_STORE_READINESS

## Context Summary
- Launch target:
- App Store risk level:
- Required before TestFlight:
- Required before App Review:

## Key Decisions
-

## Open Questions
-

## Details
### Distribution Path
- Personal device:
- TestFlight:
- App Store:

### Privacy / Data Map
| Data | Stored where | Shared with | User consent needed | Delete path |
| --- | --- | --- | --- | --- |

### Third-Party Services / AI
| Service | Purpose | Data sent | User-facing disclosure |
| --- | --- | --- |

### Account / Login / Deletion

### Monetization / IAP / Subscription

### UGC / Content / Safety

### Metadata / Screenshots / Review Notes

### Build / SDK / Device Testing

### Explicit Non-Goals For This Release
```
