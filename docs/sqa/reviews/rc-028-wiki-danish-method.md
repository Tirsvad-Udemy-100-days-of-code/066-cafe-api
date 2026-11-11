# Review of the Danish wiki wording (HTTP method)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-028 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [a117b07] |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Criterion 14 confirmed on the published wiki; verdict Go | [49f4e8e] |

---

## Artifact Under Review

- Instance reviewed: the Danish wiki pages `Home-da` and `Step-2` to `Step-9` (`-da`) in `docs/wiki/`
- Checklist used: [QC-WIKI-001]
- Scope: delta re-review of criteria 11 and 14; reason: the word "Verbum" in the route tables and "HTTP-verber" in two headings and sentences became "Metode" and "HTTP-metoder" (the Danish term for an HTTP method); earlier record [RC-008]
- Language and domain: da / it
- Language reviewer: none named; the Danish text was written by the AI and has not been read by a native speaker. The correction was requested by S01 in chat
- Mode: supervised; the reviewer is the AI as stand-in for S01; not independent of the author

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | Not affected by this change; see [RC-008] |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Not affected by this change; see [RC-008] |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Not affected by this change; see [RC-008] |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | Not affected by this change; see [RC-008] |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Not affected by this change; see [RC-008] |
| 6 | The sidebar does not repeat the page list per language | Pass | Not affected by this change; see [RC-008] |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | Not affected by this change; see [RC-008] |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Not affected by this change; see [RC-008] |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | Not affected by this change; see [RC-008] |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Not affected by this change; see [RC-008] |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Re-checked: only table header words changed; the language line of the changed pages is untouched |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Not affected by this change; see [RC-008] |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Not affected by this change; see [RC-008] |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked on the published wiki on 2026-11-11 after the merge of the change and the run of the publish workflow: the nine Danish pages `Home-da` and `Step-2` to `Step-9` (`-da`) return 200, contain "Metode" or "HTTP-metoder" and no "Verbum" or "HTTP-verber" |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | Not affected by this change; see [RC-008] |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | Not affected by this change; see [RC-008] |

## Overall Verdict

Go — every re-checked criterion passes; criterion 14 was confirmed on the published wiki after the merge. Only wording changed: no page, link, code block or file name. The Danish text as a whole is still AI-written and not read by a native speaker.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the Danish text and correct wording (this record covers only the method term) | S01 | 2026-11-16 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[RC-008]: ./rc-008-wiki-all-languages.md
[a117b07]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/a117b077fc8eff72017fefd8300f9173dc4d7b40
[49f4e8e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/commit/49f4e8ece124ad1e03a5d00b3b593ae689e641be
