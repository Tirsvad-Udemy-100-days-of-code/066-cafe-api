**English** · [Dansk](Step-4-Search-da) · [Bahasa Malaysia](Step-4-Search-ms)

# 4. Find a cafe

![Find a cafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-4.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/search?loc=...` |

## What the lecture does

- Add a `/search` route; the caller passes a location as a query parameter after a question mark, for example `?loc=Peckham`.
- Filter the query with `where()` on the location column.
- If nothing matches, answer with a clear JSON error message.

## What we gained

- Query parameters let callers narrow results without changing the route.
- A helpful error answer is part of the API design.

---

Previous: [All the cafes](Step-3-All-Cafes) · Next: [Postman](Step-5-Postman)
