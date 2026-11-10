# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [55768bf] |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-002; autonomous, not independent | [55768bf] |

---

## Purpose

This analysis identifies who has influence over, or interest in, the Day 66 documentation project and what each needs, so that the README and wiki serve them. It uses the Power/Interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsystem | HIGH | HIGH | Manage Closely | A faithful, illustrated record of what the lecture taught |
| S02 | Udemy coursists | Fellow course participants | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable material with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact, and merges.
- **Keep Informed (S02):** cannot change the project but is its main audience; their needs shape the README and the wiki.
- **Monitor (S03):** casual visitors; a good description and topics are sufficient.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is documented with a screenshot and what was gained | Functionality |
| CN-002 | S02 | README instructions to run the project and its tests work as written | Usability |
| CN-003 | S02 | Material uses the assignment's names for routes and functions | Functionality |
| CN-004 | S03 | The repository has a clear description, topics and README | Usability |
| CN-005 | S03 | No runtime dependencies to install or trust | Supportability |
| CN-006 | S01 | The wiki exists in English, Danish and Bahasa Malaysia | Functionality |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat | Per milestone | Plan and review summary | MIL-001, MIL-002, MIL-003 |
| CR-002 | Pull request | Per milestone | Reviewable change | MIL-001, MIL-002, MIL-003 |
| CR-003 | README and wiki | On merge | Published documentation | MIL-002, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants rich explanation, S03 wants a short README | S01, S03 | The README stays brief with step summaries and links; depth is in the wiki |
| S02 wants runnable code, the scope has no code | S02, S01 | The README states plainly that the repository documents the lecture and holds no application code, and points to the course resources |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 2 of [BC-001] |
| S01 | CN-006 | Objective 3 of [BC-001] |
| S02 | CN-002 | Objective 4 of [BC-001] |
| S02 | CN-003 | Objective 2 of [BC-001] |
| S03 | CN-004 | Objective 1 of [BC-001] |
| S03 | CN-005 | Objective 5 of [BC-001] |

## Sign-Off

Pending S01.

---

[BC-001]: ./business-case.md
[55768bf]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/55768bf1606cc189d8c6c00cacb762dc5fd04f55
