# G1 Repository foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Go/No-Go criterion 2 and the Objective 5 traceability row now follow Success Criterion 6 of BC-001 (Flask and Flask-SQLAlchemy since G4); Task 3 is unchanged because it is done and closed<br>Accepted on a Go review, RC-023; supervised, not independent | [1f27a84] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Spelled out KPI and API on first use; Task 1 changed only by that wording, it is done and closed<br>Accepted on a Go review, RC-025; supervised, not independent | [9086ee4] |

---

## Purpose

Decide whether the repository is ready to receive lecture documentation: it has the Python project configuration, the ignore rules, the Doxygen configuration, a README skeleton with the environment instructions, and a repeatable security scan.

## Deliverable

A pull request that adds `.gitignore`, `pyproject.toml`, `Doxyfile`, a README skeleton with venv, run and test instructions, the folders `src/` and `tests/`, and the project documents under `docs/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 2 | `pyproject.toml` requires Python 3.13 or newer and lists only the runtime dependencies that Success Criterion 6 of BC-001 allows (none when this gateway was decided, Flask and Flask-SQLAlchemy since G4) | True | Otherwise |
| 3 | `.env` is ignored and absent from the index | `git ls-files .env` is empty | `.env` tracked |
| 4 | README passes `framework/scripts/check-readme.sh` | Exit 0 | Non-zero |
| 5 | opengrep reports no High or Critical finding | 0 findings | Any finding |

Criterion 1 (repository description and topics) was removed on 2026-11-11 at S01's request. The other numbers are not changed, because review records cite them.

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / key performance indicator (KPI) / user story | Reference |
| --- | --- |
| Objective 1: publish a repository with a README and licence | [BC-001] |
| Objective 4: venv, run and test instructions | [BC-001] |
| Objective 5: minimal runtime dependencies, opengrep scan | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the one-week constraint of the Business Case (2026-11-10 to 2026-11-17).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a clear description and topics (for example python, flask, rest-api, udemy, 100-days-of-code) on the git host through its application programming interface (API), using the token in the personal `.env` that the project never reads or commits. Serves S03, who browses by description and topics. | No | |
| 2 | Add Python .gitignore | Add the standard Python ignore rules, plus `.venv/`, `.env` and doxygen output, so that the environment and the personal tokens never enter the repository. | No | |
| 3 | Add pyproject.toml | Configure the project for Python 3.13 or newer with pytest settings and an empty runtime dependency list, so S03 has nothing to install or trust. | No | |
| 4 | Add Doxyfile | Add a Doxygen configuration for `src/` so Doxygen comments in later code produce documentation. | No | |
| 5 | Add README skeleton and environment instructions | Create the README from the framework template with the project purpose, how to create and use a local `.venv`, `python -m pip install --upgrade pip`, and how to run the project and its tests. Serves S02. | No | |
| 6 | Add src and tests folder layout | Create the `src/` and `tests/` folders the project uses, each with a short README, so the agreed structure is visible although no code is written. | No | |
| 7 | Run opengrep scan before push | Run `~/.opengrep/cli/latest/opengrep.exe` locally over the repository before each push and record the result, so no finding reaches the git host. | No | |
| 8 | Keep the AI prompt log | Record the session prompts in `docs/ai-prompts/` as the framework process says; ignore the folder if the repository becomes public. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[1f27a84]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/1f27a846fd8270ced60b50e2632c0e547fd684e2
[9086ee4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/9086ee41f673e467b694c5dc168cf6de17d1d50e
