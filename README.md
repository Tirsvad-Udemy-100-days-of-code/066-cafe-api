<!-- README of the Day 66 repository, from framework/templates/README-template.md. -->

# 🚀 066-cafe-api

Notes and screenshots for Day 66 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": building a REST API with Flask. For fellow course participants and anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The Day 66 lecture builds a REST API for a database of laptop-friendly cafes: a random cafe, all cafes, a search by location, adding a cafe, updating a coffee price, deleting a closed cafe, and publishing the API documentation with Postman.

This repository documents what the lecture teaches. It holds **no application code**; the code belongs to the course. The lecture steps with screenshots are added in the next milestone, and the wiki explains what each step teaches, in English, Danish and Bahasa Malaysia.

| Part | Purpose |
| --- | --- |
| `docs/` | Project documents, the wiki source (`docs/wiki/`) and screenshots |
| `src/` | Reserved for source code (empty) |
| `tests/` | Reserved for `pytest` tests (empty) |
| `framework/` | The SQA and QC framework the project follows |

## 📋 Requirements

- Python 3.13 or newer (`python --version`), needed for the virtual environment and `pytest`.
- `git`, to clone the repository.
- Optional: [Doxygen][doxygen], to build the source documentation from the `Doxyfile`.

There are no runtime dependencies.

## 🛠️ Setup

Create and use a local virtual environment named `.venv` in the repository root, then upgrade `pip`.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pytest
```

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pytest
```

Leave the environment with `deactivate`. The `.venv` folder is ignored by git.

## ▶️ Run

There is nothing to run: the repository documents the lecture. Read the [wiki][wiki] or the lecture steps in this README. To build the (currently empty) source documentation:

```bash
doxygen Doxyfile
```

## 🧪 Tests

With the environment active:

```bash
python -m pytest
```

There is no code yet, so pytest reports "no tests ran" (exit code 5).

## 📄 License

See [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][wiki]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api
[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/issues
[doxygen]: https://www.doxygen.nl/
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
