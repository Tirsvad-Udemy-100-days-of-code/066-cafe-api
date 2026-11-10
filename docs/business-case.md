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
| 2026-11-10 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-001; autonomous, not independent | pending |

---

## Executive Summary

This project documents the learning outcome of Day 66 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp", the lecture "Build Your Own REST API Service" (a Flask cafe API). The deliverable is documentation only: a README and a trilingual wiki (English, Danish, Bahasa Malaysia) that walk through each lecture step with a screenshot and explain what was learned. No application code is written. The repository is published on the Tirsystem Gitea host so that fellow course participants and GitHub viewers can read it.

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
5. Keep the repository free of runtime dependencies and scan it with opengrep before each push.

## Scope

### In Scope

- Repository setup: description, topics, Python `.gitignore`, `pyproject.toml` (Python 3.13 or newer, pytest configuration, no runtime dependencies), `Doxyfile`, and the folders `docs/`, `src/` and `tests/` as the layout the project uses.
- README from the framework template with the lecture steps, screenshots, venv instructions and run and test instructions.
- Wiki pages in English, Danish and Bahasa Malaysia, one page per lecture step.
- A screenshot for each lecture step in the README and the wiki.
- A local opengrep scan before each push; the AI prompt log under `docs/ai-prompts/`.

### Out of Scope

- Any Python source code, tests or `constants.py` (the Product Owner asked for README and wiki only). The coding rules (pytest, Doxygen comments, `constants.py`) apply the day code is added.
- Hosting or running the API, a Postman collection or published Postman documentation.
- Secrets: `.env` holds personal tokens and is never read into the project, tested or committed.

## Expected Benefits

### Tangible Benefits

- One README and a three-language wiki that cover all nine lecture steps.
- A repository that other participants can read without installing anything.

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
| 6 | Runtime dependencies | 0 | Empty `dependencies` list in `pyproject.toml` |
| 7 | Reviews | 100 percent of artifacts have an `RC-*` verdict | Files in `docs/sqa/reviews/` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Screenshots of lecture steps cannot be produced without running the lecture code | Objective 2 not met | Use only screenshots that S01 supplies or that come from publicly reachable pages; record the source of each; ask S01 before any placeholder is used |
| The lecture material is copyrighted by the course author | Legal exposure | Summarise in own words, never reproduce solution code or the starting archive |
| Danish or Bahasa Malaysia text is machine quality | Misleading translation | English is authoritative; S01 reviews the languages S01 reads; Bahasa Malaysia is flagged as not reviewed by a native speaker |
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
- Documentation only; no programming.
- One branch and one pull request per milestone.
- Duration: 2026-11-10 to 2026-11-17 (one week).

## Cost–Benefit Assessment

A qualitative assessment is justified: the project is a personal learning record with no revenue.

| Costs | Benefits |
| --- | --- |
| About 8 hours of S01 review and screenshot work, plus AI drafting effort | Consolidated learning, a shareable reference for S02 and S03, reach in three languages |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owner, developer and reviewer; wants a record of the learning |
| S02 | Reads the README, compares solutions and runs the instructions |
| S03 | Browses the repository for ideas; needs description, topics and README |

## Recommendation

Proceed — the scope is small, documentation-only and fits the one-week constraint.

---

[SA-001]: ./stakeholder-analysis.md
