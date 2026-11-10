**English** · [Dansk](Step-7-Update-Price-da) · [Bahasa Malaysia](Step-7-Update-Price-ms)

# 7. A cafe's coffee price

![A cafe's coffee price](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-7.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `PATCH` | `/update-price/<cafe_id>` |

## What the lecture does

- First the PUT versus PATCH idea: replace everything, or change only the broken part.
- Add a PATCH route `/update-price/<cafe_id>`; the new price is a parameter.
- Get the cafe by id inside a try/except; if it does not exist, answer with an error and the HTTP status 404 instead of the default 200.

## What we gained

- Choose PATCH when only one field changes.
- A correct HTTP status code (404 not found) tells clients what happened, not only the message text.

---

Previous: [A new cafe](Step-6-Add-Cafe) · Next: [A cafe that is closed](Step-8-Delete-Cafe)
