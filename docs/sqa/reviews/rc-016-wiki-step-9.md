# Review of the Step 9 wiki pages

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-005], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [a0008b8] |

---

## Artifact Under Review

- Instance reviewed: the wiki pages `Step-9-API-Documentation`, `-da` and `-ms` in `docs/wiki/`, changed by [MIL-005]
- Checklist used: [QC-WIKI-001]
- Scope: delta re-review of criteria 3, 8, 10, 11, 13 and 14; reason: a new section "This repository's API" in the three Step 9 pages; earlier record [RC-008]
- Language and domain: en, da, ms / it
- Language reviewer: none named; the Danish and Bahasa Malaysia text was written by the AI and has not been read by a native speaker
- Mode: supervised; the reviewer is the AI as stand-in for S01; not independent of the author

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | Not affected by this change; see [RC-008] |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Not affected by this change; see [RC-008] |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Re-checked: Step 9 links only to pages that exist (`Step-8-Delete-Cafe`, `-da`, `-ms`); no sidebar change |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | Not affected by this change; see [RC-008] |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Not affected by this change; see [RC-008] |
| 6 | The sidebar does not repeat the page list per language | Pass | Not affected by this change; see [RC-008] |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | Not affected by this change; see [RC-008] |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Re-checked: the three Step 9 pages start with the language line |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | Not affected by this change; see [RC-008] |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Re-checked: 10 pages in each of en, da and ms (31 files with `_Sidebar.md`); Step 9 exists in all three |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Re-checked: current language in bold, links to the other two, on all three Step 9 pages |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Not affected by this change; see [RC-008] |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Re-checked: the `bash` block with the five `curl` commands is byte-identical in the three languages (same checksum); routes, header and field names stay English |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The new Step 9 text can be checked on the published wiki only after the merge; the publish workflow runs then |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | Not affected by this change; see [RC-008] |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | Not affected by this change; see [RC-008] |

## Overall Verdict

Go-with-conditions — every re-checked criterion passes except 14, which is Pending until the pages are published after the merge, so the MIL-005 criterion "the wiki still reviews Go" is open until then. The Danish and Bahasa Malaysia wording is AI-written and not read by a native speaker.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, check the three Step 9 pages on the published wiki and close criterion 14 | S01 | 2026-11-16 |
| Read the new Danish section and correct wording; the Bahasa Malaysia section needs a native reader | S01 | 2026-11-16 |

---

[MIL-005]: ../../milestones/mil-005-write-api.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[RC-008]: ./rc-008-wiki-all-languages.md
[a0008b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/a0008b8374b2b0f6c45664de70b15d1327ea894b
