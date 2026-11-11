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
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Follow the Business Case scope change: runnable API, two runtime dependencies, milestones MIL-004 and MIL-005<br>Accepted on a Go review, RC-010; supervised, not independent | [37f38a7] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Concern CN-004 (same ID) and the S03 rows no longer name a description and topics; the S03 dependency concern now says two runtime dependencies, as CN-005<br>Accepted on a Go review, RC-022; supervised, not independent | pending |

---

## Purpose

This analysis identifies who has influence over, or interest in, the Day 66 documentation project and what each needs, so that the README and wiki serve them. It uses the Power/Interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsystem | HIGH | HIGH | Manage Closely | A faithful, illustrated record of what the lecture taught |
| S02 | Udemy coursists | Fellow course participants | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable material with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear README, and only the two runtime dependencies Flask and Flask-SQLAlchemy |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact, and merges.
- **Keep Informed (S02):** cannot change the project but is its main audience; their needs shape the README and the wiki.
- **Monitor (S03):** casual visitors; a clear README is sufficient.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is documented with a screenshot and what was gained | Functionality |
| CN-002 | S02 | README instructions to run the project and its tests work as written | Usability |
| CN-003 | S02 | Material uses the assignment's names for routes and functions | Functionality |
| CN-004 | S03 | The repository has a clear README | Usability |
| CN-005 | S03 | Only the two runtime dependencies Flask and Flask-SQLAlchemy, and no secret in the repository | Supportability |
| CN-006 | S01 | The wiki exists in English, Danish and Bahasa Malaysia | Functionality |
| CN-007 | S02 | The cafe API runs locally and its tests pass, using the assignment's route names | Functionality |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat | Per milestone | Plan and review summary | MIL-001, MIL-002, MIL-003, MIL-004, MIL-005 |
| CR-002 | Pull request | Per milestone | Reviewable change | MIL-001, MIL-002, MIL-003, MIL-004, MIL-005 |
| CR-003 | README and wiki | On merge | Published documentation | MIL-002, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants rich explanation, S03 wants a short README | S01, S03 | The README stays brief with step summaries and links; depth is in the wiki |
| S02 wants runnable code, S03 wants nothing to install | S02, S03, S01 | The runtime dependencies are only Flask and Flask-SQLAlchemy, installed into a local `.venv`; the README says how |

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
| S02 | CN-007 | Objectives 6 and 7 of [BC-001] |

## Sign-Off

Pending S01.

---

[BC-001]: ./business-case.md
[37f38a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/37f38a77d878ac293fe09ee1f5e02a9a4afdce90
