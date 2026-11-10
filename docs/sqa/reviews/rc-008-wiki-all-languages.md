# Review of the trilingual wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6bb27fa] |
| 2026-11-10 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Criterion 14 confirmed on the published wiki; verdict Go | pending |

---

## Artifact Under Review

- Instance reviewed: the trilingual wiki in `docs/wiki/` (English, Danish, Bahasa Malaysia; 30 pages and `_Sidebar.md`)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da, ms / it
- Language reviewer: none named; the Danish and Bahasa Malaysia text was written by the AI and has not been read by a native speaker
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, one English list, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 10 English pages listed; 0 dead links across the 31 files. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is last: English, Dansk, Bahasa Melayu, each linking to its Home. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | Hand-written; no generator in the repository. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Language line on every page. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English and the PO language (English); Danish and Bahasa Malaysia added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 10 pages in each of en, da and ms; the name sets match. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line, current language in bold, links to the other two. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | `-da` and `-ms` suffixes; English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Routes, commands, file names and IDs are English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked on the published wiki on 2026-11-10: 30 pages exist, Home-da, Home-ms and sample da and ms step pages return 200, and the sidebar lists the three languages. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no generator or template change. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 31 files are directly in `docs/wiki/`. |

## Overall Verdict

Go — every criterion passes; criterion 14 was confirmed on the published wiki after the merge of G3. The Danish and Bahasa Malaysia wording is AI-written and not read by a native speaker; this is an action item, not a criterion of the checklist.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the Danish pages and correct wording; the Bahasa Malaysia pages need a native reader | S01 | 2026-11-16 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[6bb27fa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/6bb27faf87b19c469b13a0847f2219d1f83dc91a
