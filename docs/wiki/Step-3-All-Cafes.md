**English** · [Dansk](Step-3-All-Cafes-da) · [Bahasa Malaysia](Step-3-All-Cafes-ms)

# 3. All the cafes

![All the cafes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-3.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/all` |

## What the lecture does

- Add a `/all` route that returns every cafe as JSON.
- Select all rows with `select()`, run it with `execute()` and turn the result into a list with `scalars()`.
- Convert each cafe to a dictionary and return the list.

## What we gained

- A collection route is how a website could list every cafe.
- Reusing one conversion for every row avoids writing the same code per route.

---

Previous: [A random cafe](Step-2-Random-Cafe) · Next: [Find a cafe](Step-4-Search)
