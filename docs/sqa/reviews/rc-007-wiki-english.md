# Review of the English wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f4f0ed2] |

---

## Artifact Under Review

- Instance reviewed: the English wiki in `docs/wiki/` (Home, nine step pages, `_Sidebar.md`)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en / it (wiki pages have no Metadata rows)
- Language reviewer: none (S01 reads English and knows the domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, then one list of the English pages, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 10 English pages listed; a script found 0 dead links in `docs/wiki/`. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is last. Only English exists at G2; Dansk and Bahasa Melayu entries are added at MIL-003. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | The sidebar is written by hand, not produced by a generator kept in the repository. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page starts with a language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English is the PO language (registry). |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Only English exists at G2, so the page sets are identical; da and ms come with MIL-003. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line; at G2 it shows English only, links are added when the languages exist (MIL-003). |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | English pages have no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Routes, commands and file names are in English. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | Can only be checked on the published wiki after the merge. Re-check and update this record after the merge. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no generator or template change. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All pages are directly in `docs/wiki/`. |

## Overall Verdict

Go-with-conditions — every checkable criterion passes; criterion 14 (check on the published wiki) is Pending until the page is published after the merge. The record is updated to Go after that check.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the sidebar, pages and images on the published wiki, then update criterion 14 | S01 | 2026-11-14 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[f4f0ed2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/f4f0ed21099b43bcfed12afed38be5478bbd347c
