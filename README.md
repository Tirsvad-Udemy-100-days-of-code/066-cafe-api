<!-- README of the Day 66 repository, from framework/templates/README-template.md. -->

# 🚀 066-cafe-api

Notes and screenshots for Day 66 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": building a REST API with Flask. For fellow course participants and anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Lecture steps](#-lecture-steps)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The Day 66 lecture builds a REST API for a database of laptop-friendly cafes: a random cafe, all cafes, a search by location, adding a cafe, updating a coffee price, deleting a closed cafe, and publishing the API documentation with Postman.

This repository documents what the lecture teaches. It holds **no application code**; the code belongs to the course. The lecture steps with screenshots are below, and the wiki explains what each step teaches, in English, Danish and Bahasa Malaysia.

| Part | Purpose |
| --- | --- |
| `docs/` | Project documents, the wiki source (`docs/wiki/`) and screenshots |
| `src/` | Reserved for source code (empty) |
| `tests/` | Reserved for `pytest` tests (empty) |
| `framework/` | The SQA and QC framework the project follows |

## 🎓 Lecture steps

The images are illustrations with example data, drawn for this repository from the lecture description; they are not captures of the course project. Each step has a wiki page that explains what we gained ([English][wiki-home], [Dansk][wiki-home-da], [Bahasa Malaysia][wiki-home-ms]).

### 1. The starting project

Set up the virtual environment, look at `main.py` and the `cafes.db` database. [Read more][wiki-1]

![The starting project](./docs/images/step-1.png)

### 2. A random cafe

`GET /random` returns one cafe as JSON, built with `jsonify()`. [Read more][wiki-2]

![A random cafe](./docs/images/step-2.png)

### 3. All the cafes

`GET /all` returns every cafe as a JSON list. [Read more][wiki-3]

![All the cafes](./docs/images/step-3.png)

### 4. Find a cafe

`GET /search?loc=...` filters cafes by location with `where()`. [Read more][wiki-4]

![Find a cafe](./docs/images/step-4.png)

### 5. Postman

Test requests with key-value parameters and save them in a collection. [Read more][wiki-5]

![Postman](./docs/images/step-5.png)

### 6. A new cafe

`POST /add` creates a cafe from the request body. [Read more][wiki-6]

![A new cafe](./docs/images/step-6.png)

### 7. A cafe's coffee price

`PATCH /update-price/<cafe_id>` changes one field and returns 404 when the id is unknown. [Read more][wiki-7]

![A cafe's coffee price](./docs/images/step-7.png)

### 8. A cafe that is closed

`DELETE /report-closed/<cafe_id>` needs an `api-key`; wrong key gives 403. [Read more][wiki-8]

![A cafe that is closed](./docs/images/step-8.png)

### 9. Document the API

Publish the Postman collection as API documentation. [Read more][wiki-9]

![Document the API](./docs/images/step-9.png)

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
[wiki-home]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Home
[wiki-home-da]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Home-da
[wiki-home-ms]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Home-ms
[wiki-1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-1-Starting-Project
[wiki-2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-2-Random-Cafe
[wiki-3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-3-All-Cafes
[wiki-4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-4-Search
[wiki-5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-5-Postman
[wiki-6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-6-Add-Cafe
[wiki-7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-7-Update-Price
[wiki-8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-8-Delete-Cafe
[wiki-9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/wiki/Step-9-API-Documentation
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
