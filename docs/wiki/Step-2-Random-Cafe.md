**English**

# 2. A random cafe

![A random cafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-2.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/random` |

## What the lecture does

- Add a `/random` route that accepts GET requests and picks a random cafe from the database.
- An API returns JSON instead of an HTML template, so the SQLAlchemy object must be serialised.
- `jsonify()` builds the JSON; you can write each field by hand to shape the answer, or convert the row to a dictionary and jsonify that.

## What we gained

- Serialisation: turning a database object into JSON.
- Hand-built JSON gives full control (hide the id, group the booleans); a dictionary is faster when you want every field.

---

Previous: [The starting project](Step-1-Starting-Project) · Next: [All the cafes](Step-3-All-Cafes)
