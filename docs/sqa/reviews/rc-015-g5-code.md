# Review of G5 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-005], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the G5 code of [MIL-005] (`src/cafe_api/` and `tests/`, branch `g5-write-api`)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code, a technical type)
- Language reviewer: none
- Mode: supervised; the reviewer is the AI as stand-in for S01; the code was written by the `python-developer` agent, so the review is not independent of the author

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff `N` rules pass; new modules are `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE` |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`AddCafe`, `UpdateCoffeePrice`, `DeleteCafe`, `EnvApiKeyVerifier`, `AccessDeniedError`) |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` clean on the whole tree; no suppressions |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` reports no issues in 43 source files; the one `Any` (raw JSON in `parse_new_cafe`) is commented |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except:`; the repository rolls back and re-raises; an `IntegrityError` is converted to `InvalidCafeError` with the cause kept |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened by our code; commits go through the Flask-SQLAlchemy session |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have docstrings with `@param`/`@return`/`@throws` |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print`; the API key is never logged or returned (the 403 message is fixed text) |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The project has no Design Class Diagram; MIL-005 tasks are plain technical tasks citing wiki steps 6 to 9. Recorded here as the deviation |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 82 tests (59 new) with positive, negative and error cases for each endpoint; each test sets its own key with `monkeypatch`; no network, no `.env` |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Strict mode clean |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional. Same as [RC-014]: bounded ranges, no exact pins or lock file |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Routes, header, env var name, messages and field tuples are in `constants.py`; the cafe field list is not repeated in the new parser beyond the constants |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `test_layer_imports.py` still passes with the new domain and application modules; the key check is a port (`ApiKeyVerifier`) implemented in infrastructure and wired in the composition root |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One use case per operation; `ApiKeyVerifier` is a narrow protocol received by `DeleteCafe`; `CafeRepository` grew by four methods that all use cases need; no type tests |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | New code sits in `domain`, `application` (`ports`, `dto`, `use_cases`), `infrastructure` and `presentation` (`controllers`, `contracts`, `shared`); tests in `unit`, `integration`, `e2e` |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All new names are English `snake_case`, no space |

## Overall Verdict

Go — every Mandatory criterion passes or is N-A with a reason (7, 10); the Optional criterion 13 fails as in [RC-014]. Verified here, not only reported: `pytest` 82 passed, `ruff`, `mypy --strict`, and a live run of `python -m cafe_api` with `curl`: `POST /add` 201 and 400 (duplicate name, non-boolean flag), `PATCH /update-price` 200, 404 and 400, `DELETE /report-closed` 403 without a key and with a wrong key (also for an unknown id), 404 with the right key for an unknown id, 200 with the right key. Lesson from [RC-014]: the pull request's OpenGrep check blocks on `useless-inner-function`, which my local scan does not run, so the new controller and handlers use classes and module-level functions, and an AST check finds no function defined inside another function in `src/`. The local scan reports only the non-blocking WARNING `sql-injection-db-cursor-execute` (a false positive, three controller calls to our own `execute`). The pull request's OpenGrep result is the reference and is not known yet. Go/No-Go criteria 1 to 5 and 8 of MIL-005 are met on these checks; criterion 6 and 7 are covered by [RC-016]; criterion 9 depends on the pull request check.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Review the code yourself before the merge; this review is not independent | S01 | 2026-11-15 |
| Confirm the OpenGrep check of the G5 pull request has no ERROR finding | S01 | 2026-11-16 |
| Decide whether to add a lock file or exact pins (optional criterion 13) | S01 | 2026-11-16 |

---

[MIL-005]: ../../milestones/mil-005-write-api.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[RC-014]: ./rc-014-g4-code.md
