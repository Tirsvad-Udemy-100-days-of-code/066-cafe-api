# G5 Write endpoints and API documentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-013; supervised, not independent | [37f38a7] |

---

## Purpose

Decide whether the API can change data as the lecture describes (add a cafe, update a coffee price, delete a closed cafe with an API key) without leaking a secret, and whether the endpoints are documented in the README and in all three wiki languages.

## Deliverable

A pull request that adds `POST /add`, `PATCH /update-price/<id>` and `DELETE /report-closed/<id>` with their use cases, the API key check read from an environment variable, `pytest` tests, and the endpoint documentation in the README and in the wiki step 9 pages in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes, with tests for success and failure of each write endpoint | All pass | Any failure or missing test |
| 2 | `POST /add` creates a cafe that `GET /all` then returns | Yes | No |
| 3 | `PATCH /update-price/<id>` changes the price and returns 404 for an unknown id | Yes | No |
| 4 | `DELETE /report-closed/<id>` returns 403 with a wrong or missing key, 404 for an unknown id, and deletes with the right key | Yes | No |
| 5 | The API key is read from an environment variable, has no default in code, and no key value is in the repository | True | Otherwise |
| 6 | Every endpoint is documented in the README and in `Step-9-API-Documentation` in en, da and ms | 3 of 3 languages | Fewer |
| 7 | The wiki still reviews `Go` against QC-WIKI-001 | Go | Other |
| 8 | The code is reviewed `Go` against `qc-programming-python` | Go | Other |
| 9 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The write endpoints reuse the model, repository, layers and test set-up of G4 |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6: implement the write endpoints | [BC-001] |
| Objective 3: the wiki in three languages stays current | [BC-001] |
| Objective 7: structure, constants, comments, tests | [BC-001] |
| Concern CN-007 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — one day before the Business Case end date (2026-11-17).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the add-cafe use case and endpoint | Add the use case and `POST /add` that creates a cafe from the request body and returns a JSON success message, with validation of missing fields. | No | Wiki step 6 |
| 2 | Implement the update-price use case and endpoint | Add the use case and `PATCH /update-price/<id>` that changes the coffee price given as a query parameter, with a 404 JSON error for an unknown id. | No | Wiki step 7 |
| 3 | Implement the delete use case and API key check | Add the use case and `DELETE /report-closed/<id>` guarded by an API key read from an environment variable with no default; 403 for a wrong or missing key, 404 for an unknown id. | No | Wiki step 8 |
| 4 | Write pytest tests for the write side | Test each endpoint for success and failure with the Flask test client; tests set their own test key and never use a real one. | No | |
| 5 | Add Doxygen comments to the new code | Comment the new public classes and functions in the Doxygen style. | No | |
| 6 | Document the API in the README | Add the endpoint list with request and response examples and how to set the API key, so S02 can try each call. | No | Wiki step 9 |
| 7 | Update the wiki step 9 pages in three languages | Bring `Step-9-API-Documentation` in English, Danish and Bahasa Malaysia in line with the implemented endpoints; English is authoritative. | No | Wiki step 9 |
| 8 | Review code and run opengrep before push | Review the code against `qc-programming-python`, record the `RC-*`, run opengrep locally and record the result, and keep the AI prompt log. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[37f38a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/37f38a77d878ac293fe09ee1f5e02a9a4afdce90
