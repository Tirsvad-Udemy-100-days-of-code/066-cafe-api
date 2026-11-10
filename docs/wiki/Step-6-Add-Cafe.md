**English**

# 6. A new cafe

![A new cafe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-6.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `POST` | `/add` |

## What the lecture does

- Add a POST route that creates a cafe from the values sent in the request body.
- In Postman the body tab's key-value pairs play the role of `<input name=...>` in an HTML form, so no form is needed to test.
- Commit the new row to the database and answer with a success message.

## What we gained

- POST creates resources; the data travels in the body, not in the URL.
- You can build and test the server side before any front end exists.

---

Previous: [Postman](Step-5-Postman) · Next: [A cafe's coffee price](Step-7-Update-Price)
