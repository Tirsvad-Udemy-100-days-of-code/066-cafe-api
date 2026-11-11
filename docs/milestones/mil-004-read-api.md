# G4 Flask app and read endpoints

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-012; supervised, not independent | pending |

---

## Purpose

Decide whether the Flask cafe API runs locally and answers the three read requests of the lecture (a random cafe, all cafes, a search by location), with the structure, constants, comments and tests the project rules require.

## Deliverable

A pull request that adds the layered package under `src/` (domain, application, infrastructure, presentation), the `Cafe` model on SQLite with example seed data, `constants.py`, the endpoints `GET /random`, `GET /all` and `GET /search?loc=...`, `pytest` tests under `tests/`, the Flask and Flask-SQLAlchemy dependencies in `pyproject.toml`, and README run and test instructions that match the code.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes, with at least one test per endpoint and one for an empty search result | All pass | Any failure or missing test |
| 2 | `GET /random`, `GET /all` and `GET /search?loc=...` return JSON with the cafe fields named in the wiki | Yes | No |
| 3 | `GET /search` for an unknown location returns a JSON error with status 404 | Yes | No |
| 4 | The domain and application layers import neither Flask nor SQLAlchemy | True (checked by a test) | Otherwise |
| 5 | The code is reviewed `Go` against `qc-programming-python` | Go | Other |
| 6 | `pyproject.toml` lists exactly Flask and Flask-SQLAlchemy as runtime dependencies | True | Otherwise |
| 7 | No secret, no `cafes.db` of the course and no course code is in the repository | True | Otherwise |
| 8 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The English wiki step pages 1 to 5 describe the behaviour this gateway implements; the Danish and Bahasa Malaysia pages of MIL-003 are not needed |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5: minimal runtime dependencies, scan | [BC-001] |
| Objective 6: implement the read endpoints | [BC-001] |
| Objective 7: structure, constants, comments, tests | [BC-001] |
| Concern CN-007 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — inside the one-week constraint of the Business Case (2026-11-10 to 2026-11-17).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add runtime dependencies and package layout | Add Flask and Flask-SQLAlchemy to `pyproject.toml` and create the layer folders under `src/` (domain, application, infrastructure, presentation) as the `clean-architecture` skill shows, so that the business rules do not import the framework. Serves S02, who installs into a local `.venv`. | No | |
| 2 | Add constants.py | Hold every fixed value (route paths, field names, default database file, error messages) in `constants.py`, as the Python coding rules require, so no magic string is repeated. | No | |
| 3 | Implement the Cafe entity and repository port | Define the `Cafe` entity with the fields the wiki names (name, map link, image link, location, seats, toilet, wifi, sockets, calls, coffee price) and a repository interface in the domain layer. | No | |
| 4 | Implement the SQLite repository and seed data | Implement the repository with Flask-SQLAlchemy in the infrastructure layer and a seed step with example cafes written for this repository, never the course's `cafes.db`. | No | |
| 5 | Implement the read use cases | Add the use cases random cafe, all cafes and search by location in the application layer, independent of Flask. | No | Wiki steps 2 to 4 |
| 6 | Add the Flask read endpoints | Add `GET /random`, `GET /all` and `GET /search?loc=...` in the presentation layer (MVC for an API), returning JSON and a 404 JSON error when no cafe matches. | No | Wiki steps 2 to 4 |
| 7 | Write pytest tests for the read side | Test the use cases with a fake repository and the endpoints with the Flask test client, including the empty search and a test that the inner layers import no framework. | No | |
| 8 | Add Doxygen comments | Comment every public class and function in the Doxygen style the Python rules set, so the `Doxyfile` produces documentation. | No | |
| 9 | Update README run and test instructions | Replace the "no application code" statements with the commands to install, seed, run and test, matching the code. Serves S02. | No | |
| 10 | Review code and run opengrep before push | Review the code against `qc-programming-python`, record the `RC-*`, run opengrep locally and record the result, and keep the AI prompt log. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
