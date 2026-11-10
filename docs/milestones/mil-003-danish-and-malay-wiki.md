# G3 Danish and Bahasa Malaysia wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [55768bf] |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-006; autonomous, not independent | [55768bf] |

---

## Purpose

Decide whether the wiki exists in all three languages with the same page set, so that S02 and S03 can read it in English, Danish or Bahasa Malaysia.

## Deliverable

The Danish pages (`*-da.md`) and the Bahasa Malaysia pages (`*-ms.md`) in `docs/wiki/`, the language section of the sidebar, and README links to the wiki in all three languages.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each English page has a `-da` and a `-ms` page | 11 of 11 each | Any missing |
| 2 | Each page starts with the language line | All | Any without |
| 3 | The sidebar has a Languages section with three entries | Yes | No |
| 4 | The wiki reviews `Go` against QC-WIKI-001 | Go | Other |
| 5 | Screenshots appear on every translated step page | 9 of 9 per language | Fewer |
| 6 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The English text is authoritative and is translated page by page |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3: wiki in three languages | [BC-001] |
| Concern CN-006 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — after MIL-002 and one day before the Business Case end date (2026-11-17).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Translate wiki to Danish | Translate Home and the nine step pages to Danish as `*-da.md`; code, commands, file names and IDs stay in English. | No | |
| 2 | Translate wiki to Bahasa Malaysia | Translate Home and the nine step pages to Bahasa Malaysia as `*-ms.md`; the same rule for code and names. | No | |
| 3 | Add Languages section to the sidebar | Add the Languages section last in `_Sidebar.md` with `English: [Home](Home)`, `Dansk: [Hjem](Home-da)` and `Bahasa Melayu: [Utama](Home-ms)`. | No | |
| 4 | Link wiki languages from README | Add links to the wiki in the three languages to the README. | No | |
| 5 | Review the wiki against QC-WIKI-001 | Review all three languages and record the `RC-*`; the language criteria stay pending for S01 where a stand-in cannot decide them. | No | |
| 6 | Run opengrep scan before push | Run opengrep over the repository before pushing the branch. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[55768bf]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/55768bf1606cc189d8c6c00cacb762dc5fd04f55
