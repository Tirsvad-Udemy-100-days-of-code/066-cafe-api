# Review of PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [37f38a7] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: delta re-review of the change in Version History row 2026-11-11 (add G4 and G5), all criteria re-checked against the earlier record [RC-003]
- Language and domain: en / it
- Language reviewer: S01 (confirmed criteria 3, 5 and 9 of QC-LANG-001)
- Mode: supervised; the reviewer is the AI as stand-in for S01, at S01's request in chat ("Accept, review it", 2026-11-11); not independent of the author

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-10, end 2026-11-17, constraint one week; unchanged |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | G1 to G5 each listed once with document, decision date and owner S01 |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | G4 on 2026-11-13 and G5 on 2026-11-16 match MIL-004 and MIL-005 and lie inside the window |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every in-scope item of BC-001, including the API endpoints and the API documentation, to G4 or G5 |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependencies G1 to G2 to G3 and G2 to G4 to G5 are stated and acyclic. G4 is decided on 2026-11-13, before G2's planned date of 2026-11-14, but G2 reached Go on 2026-11-10 (RC-005); the assumption records this. This was a defect in the first draft (G4 depended on G3) and was corrected before the review |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | No-Go rule covers later gateways and the end date; S01 decides the end date |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 only; no invented roles |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions list the source; the early Go of G1 to G3 and the code rules are recorded as assumptions |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Five plan risks with impact and mitigation; two new risks (overrun, resemblance to lecture code) trace to BC-001 risks |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues are current; the user-stories decision is stated as an open issue and the plan assumes none |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverables of G4 and G5 match the Deliverable sections of MIL-004 and MIL-005 |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | G4 and G5 say 'none (technical tasks)' with the reason in Open Issues |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars, table and dependency list agree |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | G4 and G5 marked 'not yet synced' |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One plan; Version History has the new row |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | AI proposal: the content is English throughout. Only S01 may confirm (no stand-in). Confirmed by S01 by accepting the plan in chat, 2026-11-11. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is the one the registry gives for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | AI proposal: only common IT terms are used and no domain dictionary exists yet. Only S01 may confirm. Confirmed by S01 by accepting the plan in chat, 2026-11-11. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | AI proposal: terms are used correctly. A reviewer competent in the domain must confirm: S01. Confirmed by S01 by accepting the plan in chat, 2026-11-11. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Optional. Acronyms such as API, MVC, JSON, SQLite and HTTP are used without being spelled out on first use. |

## Overall Verdict

Go — every Mandatory criterion passes; criteria 3, 5 and 9 of QC-LANG-001 were confirmed by S01 (plan acceptance in chat, 2026-11-11). Only the Optional criterion 10 (acronyms) fails and does not block; it has an action item. Mode: supervised, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Spell out acronyms (API, MVC, JSON, SQLite, HTTP) on first use (optional criterion 10 of QC-LANG-001) | S01 | 2026-11-16 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[37f38a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/37f38a77d878ac293fe09ee1f5e02a9a4afdce90
