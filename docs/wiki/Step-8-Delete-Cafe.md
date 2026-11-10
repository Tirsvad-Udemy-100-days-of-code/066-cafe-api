**English** · [Dansk](Step-8-Delete-Cafe-da) · [Bahasa Malaysia](Step-8-Delete-Cafe-ms)

# 8. A cafe that is closed

![A cafe that is closed](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-8.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `DELETE` | `/report-closed/<cafe_id>` |

## What the lecture does

- Add a DELETE route `/report-closed/<cafe_id>`.
- Protect it with an `api-key` parameter: a wrong key gets 403 Forbidden, a missing cafe gets 404.
- Delete the row and commit only when the key is right and the cafe exists.

## What we gained

- Simple authorisation: not everyone may delete data.
- The order of checks matters: authorise first, then look up, then change.

---

Previous: [A cafe's coffee price](Step-7-Update-Price) · Next: [Document the API](Step-9-API-Documentation)
