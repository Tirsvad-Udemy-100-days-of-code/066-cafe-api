**English** · [Dansk](Step-9-API-Documentation-da) · [Bahasa Malaysia](Step-9-API-Documentation-ms)

# 9. Document the API

![Document the API](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-9.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

## What the lecture does

- Other people cannot see the server code, so the API must be documented: routes, parameters and what comes back.
- Give every Postman request a name and a description, keep them in one collection and use Publish Docs.
- Link the published documentation from the project's `index.html` with an anchor tag.

## This repository's API

This repository holds its own implementation of the API. Start it with `python -m cafe_api`; it listens on `http://127.0.0.1:5000`.

| Verb | Route | What it does | Success | Errors |
| --- | --- | --- | --- | --- |
| `GET` | `/random` | One random cafe | 200 `{"cafe": {...}}` | 404 when there is no cafe |
| `GET` | `/all` | Every cafe | 200 `{"cafes": [...]}` |  |
| `GET` | `/search?loc=...` | The cafes at a location, ignoring case | 200 `{"cafes": [...]}` | 400 without `loc`, 404 when none match |
| `POST` | `/add` | Create a cafe from a JSON body | 201 `{"cafe": {...}}` | 400 for a missing, blank or wrongly typed field, or a name that already exists |
| `PATCH` | `/update-price/<cafe_id>?new_price=...` | Change the coffee price | 200 `{"cafe": {...}}` | 400 without `new_price`, 404 for an unknown id |
| `DELETE` | `/report-closed/<cafe_id>` | Remove a closed cafe; needs the header `X-API-Key` | 200 `{"message": "..."}` | 403 for a wrong or missing key, 404 for an unknown id |

- Every error is JSON: `{"error": "..."}`.
- The API key is read from the environment variable `CAFE_API_KEY` when a request arrives. There is no default key: when the variable is not set, every delete answers 403.
- The lecture sends the key as the query parameter `api-key`. Here it travels in the header `X-API-Key`, so the key does not end up in URLs and logs.
- The `POST /add` body is a JSON object with the text fields `name`, `map_url`, `img_url`, `location`, `seats`, the true/false fields `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, and an optional `coffee_price`.

Try them (on Windows PowerShell use `curl.exe`, or send the requests from Postman):

```bash
curl http://127.0.0.1:5000/random
curl "http://127.0.0.1:5000/search?loc=Peckham"
curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"name": "Example Cafe", "map_url": "https://example.com/map", "img_url": "https://example.com/img.jpg", "location": "Peckham", "seats": "10-20", "has_toilet": true, "has_wifi": true, "has_sockets": false, "can_take_calls": false, "coffee_price": "2.80"}'
curl -X PATCH "http://127.0.0.1:5000/update-price/1?new_price=3.20"
curl -X DELETE http://127.0.0.1:5000/report-closed/1 -H "X-API-Key: <your-key>"
```

## What we gained

- Documentation is part of an API product.
- Postman generates it from the saved requests, so the tests and the documentation stay in step.

---

Previous: [A cafe that is closed](Step-8-Delete-Cafe) · [Home](Home)
