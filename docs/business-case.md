# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-001; autonomous, not independent | [55768bf] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Scope change: add the Flask cafe API (code) to the documentation project<br>New objectives 6 and 7, new Success Criteria 8 and 9<br>Runtime dependencies limited to Flask and Flask-SQLAlchemy<br>Accepted on a Go review, RC-009; supervised, not independent | pending |

---

## Executive Summary

This project documents the learning outcome of Day 66 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp", the lecture "Build Your Own REST API Service" (a Flask cafe API). The deliverables are a README and a trilingual wiki (English, Danish, Bahasa Malaysia) that walk through each lecture step with a screenshot and explain what was learned, and a working implementation of the lecture's cafe API in Python with Flask, with tests, so that the documented steps can be run. The repository is published on the Tirsystem Gitea host so that fellow course participants and GitHub viewers can read it.

## Methodological and Standards Foundation

- Process: the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, one pull request per milestone).
- Quality model: ISO/IEC 25010:2023 characteristics tag every QC criterion.
- Documentation: Markdown, reviewed against `QC-WIKI-001` for the wiki and checked with `framework/scripts/check-readme.sh` for the README.
- Repository hygiene: a Python `.gitignore`, `pyproject.toml`, a Doxyfile and a static-analysis scan with opengrep before every push.

## Problem Statement

A course participant learns the Day 66 REST API concepts (REST, HTTP verbs, routing, JSON serialisation, Postman, API keys, documentation) but keeps no structured record of them. Participants who want to compare solutions find scattered code and no explanation of the lecture steps in context, and none in Danish or Bahasa Malaysia.

## Business Opportunity

A clear, illustrated walk-through of the lecture steps lets S01 consolidate the learning, lets S02 compare against a readable reference, and lets S03 find a well-described repository. A trilingual wiki widens the audience at low cost.

## Objectives

1. Publish a repository with a description, topics, README and licence on the Tirsystem Gitea host.
2. Document each Day 66 lecture step (starting project, random cafe, all cafes, search, Postman, add a cafe, update the price, delete a cafe, API documentation) in the README with one screenshot per step.
3. Publish a wiki in English, Danish and Bahasa Malaysia with the same page set, each page explaining what was gained in that step.
4. Document how to create and use a local `.venv` and run `python -m pip install --upgrade pip`, and how to run the project and its tests.
5. Keep the runtime dependencies to the minimum the API needs (Flask and Flask-SQLAlchemy) and scan the repository with opengrep before each push.
6. Implement the cafe API from the lecture: random cafe, all cafes, search by location, add a cafe, update a price, delete a cafe with an API key; written from the lecture description, with tests.
7. Keep the implementation clean in structure (layers per `clean-architecture`), constants in `constants.py`, Doxygen comments, and `pytest` tests that pass.

## Scope

### In Scope

- Repository setup: description, topics, Python `.gitignore`, `pyproject.toml` (Python 3.13 or newer, pytest configuration, runtime dependencies Flask and Flask-SQLAlchemy from G4), `Doxyfile`, and the folders `docs/`, `src/` and `tests/` as the layout the project uses.
- README from the framework template with the lecture steps, screenshots, venv instructions and run and test instructions.
- Wiki pages in English, Danish and Bahasa Malaysia, one page per lecture step.
- A screenshot for each lecture step in the README and the wiki.
- A local opengrep scan before each push; the AI prompt log under `docs/ai-prompts/`.
- The Flask cafe API (gateways G4 and G5): a `Cafe` model on SQLite with example seed data, the endpoints `GET /random`, `GET /all`, `GET /search`, `POST /add`, `PATCH /update-price/<id>` and `DELETE /report-closed/<id>` (guarded by an API key read from the environment), `pytest` tests, and README instructions to run it.
- API documentation of the endpoints in the README and the wiki (lecture step 9), in the three wiki languages.

### Out of Scope

- The course's starting archive, its `cafes.db` and its solution code: the API is written from the lecture description and seeded with example data.
- Hosting the API in production, a front end, user accounts, and a Postman collection or published Postman documentation.
- Secrets: `.env` holds personal tokens and is never read into the project, tested or committed. The API key is read from an environment variable at run time; tests set their own test value and no real key is stored in the repository.

## Expected Benefits

### Tangible Benefits

- One README and a three-language wiki that cover all nine lecture steps.
- A cafe API that other participants can run and test locally after setting up the `.venv`.

### Intangible Benefits

- Consolidated understanding of REST and Flask API design for S01.
- A reusable pattern for documenting the remaining bootcamp days.

## Strategic Alignment

The repository belongs to the Tirsvad Udemy 100 Days of Code collection, one repository per day. It follows the same framework, wiki and review conventions as the other repositories of the Tirsystem host.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps documented | 9 of 9 steps in the README and in each wiki language | Count of step sections |
| 2 | Screenshots | 1 per lecture step in the README and the wiki | Count of images referenced |
| 3 | Wiki languages | 3 (en, da, ms) with identical page sets | Page list comparison |
| 4 | Repository metadata | Description set and at least 5 topics | Gitea API response |
| 5 | Security scan | 0 findings of High or Critical severity | opengrep output before each push |
| 6 | Runtime dependencies | 2 (Flask, Flask-SQLAlchemy), none other | `dependencies` list in `pyproject.toml` |
| 7 | Reviews | 100 percent of artifacts have an `RC-*` verdict | Files in `docs/sqa/reviews/` |
| 8 | Endpoints implemented | 6 of 6, each with a passing `pytest` test | `pytest` output |
| 9 | Code review | `Go` against `qc-programming-python` for each code gateway | `RC-*` files |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Screenshots of lecture steps cannot be produced without running the lecture code | Objective 2 not met | Use only screenshots that S01 supplies or that come from publicly reachable pages; record the source of each; ask S01 before any placeholder is used |
| The lecture material is copyrighted by the course author | Legal exposure | Summarise in own words, never reproduce solution code or the starting archive |
| Danish or Bahasa Malaysia text is machine quality | Misleading translation | English is authoritative; S01 reviews the languages S01 reads; Bahasa Malaysia is flagged as not reviewed by a native speaker |
| The new code resembles the copyrighted lecture code too closely | Legal exposure | Write the code from the lecture description and the wiki with own structure, names and seed data; never copy the course archive or `cafes.db` |
| The delete endpoint's API key is hardcoded or committed | Key leak | Read it from an environment variable, no default value in code, tests use a test value |
| The scope grows past the one-week constraint | G5 slips | Two small code gateways; S01 decides to drop or move G5 |
| A token leaks into the repository | Account compromise | `.env` is in `.gitignore`, is never opened by project tooling, and an opengrep scan runs before each push |
| Gitea wiki publishing is not enabled | Wiki not visible | Keep the wiki in `docs/wiki/`, enable the wiki in the repository settings, verify after merge |

## Assumptions

- S01 is Product Owner, developer and reviewer; the AI acts as stand-in reviewer in autonomous mode.
- The PO language is English and the PO domain is IT.
- The Gitea repository exists and `.env` holds tokens for the personal use of S01.
- Wiki pages are published by the `publish-wiki-pages.yml` workflow after merge.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`; no runtime dependencies unless needed.
- Folder structure `src/`, `tests/`, `docs/`.
- Python code follows the framework rules (`constants.py`, Doxygen comments, `pytest` tests, layers per `clean-architecture`); nothing is written under `src/` or `tests/` before its gateway is `Accepted` with a `Go` review.
- One branch and one pull request per milestone.
- Duration: 2026-11-10 to 2026-11-17 (one week).

## Cost–Benefit Assessment

A qualitative assessment is justified: the project is a personal learning record with no revenue.

| Costs | Benefits |
| --- | --- |
| About 8 hours of S01 review and screenshot work, plus about 6 hours for the code gateways, plus AI drafting effort | Consolidated learning, a shareable reference for S02 and S03, reach in three languages |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owner, developer and reviewer; wants a record of the learning |
| S02 | Reads the README, compares solutions and runs the instructions |
| S03 | Browses the repository for ideas; needs description, topics and README |

## Recommendation

Proceed — the scope is small and fits the one-week constraint: the documentation is done (G1 to G3) and two small code gateways (G4, G5) are added.

---

[SA-001]: ./stakeholder-analysis.md
[55768bf]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/55768bf1606cc189d8c6c00cacb762dc5fd04f55
