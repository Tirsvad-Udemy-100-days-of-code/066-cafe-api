# Review of G4 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [37f38a7] |

---

## Artifact Under Review

- Instance reviewed: the G4 code of [MIL-004] (`src/cafe_api/` and `tests/`, branch `g4-read-api`)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code, a technical type)
- Language reviewer: none
- Mode: supervised; the code was written by the `python-developer` agent and reviewed by the AI as stand-in for S01, so the review is not independent of the author

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff `N` rules pass; modules `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE` |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`find_by_location`, `GetRandomCafe`, `MSG_NO_CAFE_AT_LOCATION`); no single-letter names |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` clean on 41 files; no suppressions |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` reports no issues in 34 source files |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | grep finds no bare `except:`; errors are specific (`CafeNotFoundError`, `InvalidSearchError`) and mapped to HTTP codes in one place |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; `id` is a dataclass field name only, no builtin is shadowed as a variable |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no file, lock or connection itself; the SQLAlchemy session is owned by Flask-SQLAlchemy |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a docstring with a brief first sentence and `@param`/`@return`/`@throws`; private helpers are short |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print`; no logging is needed yet and no secret is read or written |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The project has no Design Class Diagram; MIL-004 tasks are plain technical tasks citing wiki steps 2 to 4, and the layer layout follows the `clean-architecture` skill. Recorded here as the deviation |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 23 pytest tests (unit, integration, e2e) named for behaviour, using temporary SQLite files; no network, no order dependence, no `.env` |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Strict mode clean; no `Any` |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional. Dependencies are declared with bounded ranges (`Flask>=3.1,<4`), not exact pins, and there is no lock file. Dev tools are in the `dev` extra |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Routes, messages and JSON keys are in `constants.py`; the response keys derive from `CafeDto`. The `Cafe`, `CafeDto` and `CafeModel` field lists look alike but change for different reasons (domain, boundary, storage), so they stay separate |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `tests/unit/test_layer_imports.py` parses `domain/` and `application/` and fails on Flask, SQLAlchemy, infrastructure or presentation imports; the controller takes use cases and imports no infrastructure |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One responsibility per use case; repository is a narrow `Protocol`; use cases receive it by constructor; the composition root builds the adapter |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/cafe_api`; `unit`, `integration`, `e2e` under `tests/`; MVC layout `controllers`, `contracts`, `shared`; imports point inward |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All file and folder names are English `snake_case` with no space |

## Overall Verdict

Go — every Mandatory criterion passes or is N-A with a reason (7, 10). The Optional criterion 13 fails (no exact pins) and does not block. Verified here, not only reported: `pytest` 23 passed, `ruff`, `mypy --strict`, a live run of `python -m cafe_api` with `curl` on `/random`, `/all`, `/search` (200, 404, 400). opengrep (`--no-git-ignore`, so the untracked files were scanned) reports one WARNING and no High or Critical: a Django SQL rule matched `search_cafes.execute(location)` in the controller; it is a false positive, because `execute` is our use case and the query goes through SQLAlchemy's parameterised `where`. Go/No-Go criteria 1 to 8 of MIL-004 are met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether to add a lock file or exact pins (optional criterion 13) | S01 | 2026-11-16 |
| Review the code yourself before the merge; this review is not independent | S01 | 2026-11-13 |

---

[MIL-004]: ../../milestones/mil-004-read-api.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[37f38a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/37f38a77d878ac293fe09ee1f5e02a9a4afdce90
