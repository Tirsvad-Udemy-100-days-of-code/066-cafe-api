# Traceability Matrix: Cafe API

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the baseline milestone, with the review records of all documents (autonomous, not independent) | [2f325a3] |

---

## Purpose

Tracks backward and forward links between the artifact instances of Cafe API so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-029], [RC-024], [RC-020], [RC-018], [RC-017], [RC-009], [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-027], [RC-022], [RC-010], [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-030], [RC-026], [RC-021], [RC-011], [RC-003] |
| [MIL-001] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-025], [RC-023], [RC-019], [RC-004] |
| [MIL-002] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-005] |
| [MIL-003] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-006] |
| [MIL-004] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-012], [RC-014] |
| [MIL-005] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-013], [RC-015] |
| [MIL-006] | Milestone | en | education | [BC-001], [PP-001], [MIL-005] | - | [RC-031] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-002], [MIL-003] | - | [RC-032], [RC-028], [RC-016], [RC-008], [RC-007] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (Go/No-Go criteria 1 and 2) | - | - | Covered |
| CN-002 | [MIL-001] (Go/No-Go criterion 4) | - | - | Covered |
| CN-003 | [MIL-004] (Go/No-Go criterion 2) | - | - | Covered |
| CN-004 | [MIL-001] (Go/No-Go criterion 4) | - | - | Covered |
| CN-005 | [MIL-001] (criterion 2), [MIL-004] (criteria 6 and 7) | - | - | Covered |
| CN-006 | [MIL-003] (Go/No-Go criteria 1 to 3) | - | - | Covered |
| CN-007 | [MIL-004] (criteria 1 to 3), [MIL-005] (criteria 1 to 4) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it. The domain of BC-001, PP-001 and MIL-006 is `education` since MIL-006; the other documents keep the domain `it` they were accepted with (see the Open Issues of PP-001). The wiki row shows the domain of the project (a wiki is not an artifact with a `Domain` row). MIL-006 adds this matrix and changes no source, test, image or wiki file. The framework has no quality checklist for this matrix, so it has no review record of its own. The review records RC-001 to RC-032 are not rows themselves; RC-014 and RC-015 review the code of the milestones MIL-004 and MIL-005.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-repository-foundation.md
[MIL-002]: ../milestones/mil-002-english-lecture-documentation.md
[MIL-003]: ../milestones/mil-003-danish-and-malay-wiki.md
[MIL-004]: ../milestones/mil-004-read-api.md
[MIL-005]: ../milestones/mil-005-write-api.md
[MIL-006]: ../milestones/mil-006-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-wiki-english.md
[RC-008]: ./reviews/rc-008-wiki-all-languages.md
[RC-009]: ./reviews/rc-009-business-case-v2.md
[RC-010]: ./reviews/rc-010-stakeholder-analysis-v2.md
[RC-011]: ./reviews/rc-011-project-plan-v2.md
[RC-012]: ./reviews/rc-012-mil-004.md
[RC-013]: ./reviews/rc-013-mil-005.md
[RC-014]: ./reviews/rc-014-g4-code.md
[RC-015]: ./reviews/rc-015-g5-code.md
[RC-016]: ./reviews/rc-016-wiki-step-9.md
[RC-017]: ./reviews/rc-017-business-case-v3.md
[RC-018]: ./reviews/rc-018-business-case-v4.md
[RC-019]: ./reviews/rc-019-mil-001-v2.md
[RC-020]: ./reviews/rc-020-business-case-v5.md
[RC-021]: ./reviews/rc-021-project-plan-v3.md
[RC-022]: ./reviews/rc-022-stakeholder-analysis-v3.md
[RC-023]: ./reviews/rc-023-mil-001-v3.md
[RC-024]: ./reviews/rc-024-business-case-v6.md
[RC-025]: ./reviews/rc-025-mil-001-v4.md
[RC-026]: ./reviews/rc-026-project-plan-v4.md
[RC-027]: ./reviews/rc-027-stakeholder-analysis-v4.md
[RC-028]: ./reviews/rc-028-wiki-danish-method.md
[RC-029]: ./reviews/rc-029-business-case-baseline.md
[RC-030]: ./reviews/rc-030-project-plan-baseline.md
[RC-031]: ./reviews/rc-031-milestone-006.md
[RC-032]: ./reviews/rc-032-wiki-baseline.md
[2f325a3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/2f325a39b931a60920bb82434ad99e74cb1f7951
