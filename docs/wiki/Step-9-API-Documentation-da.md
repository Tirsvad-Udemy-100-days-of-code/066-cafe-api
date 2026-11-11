[English](Step-9-API-Documentation) · **Dansk** · [Bahasa Malaysia](Step-9-API-Documentation-ms)

# 9. Dokumentér API'et

![Dokumentér API'et](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-9.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionens beskrivelse. Det er ikke en optagelse af kursusprojektet.*

## Hvad lektionen gør

- Andre kan ikke se serverkoden, så API'et skal dokumenteres: ruter, parametre og hvad der kommer retur.
- Giv hver Postman-forespørgsel et navn og en beskrivelse, behold dem i én samling og brug Publish Docs.
- Link til den udgivne dokumentation fra projektets `index.html` med et anker-tag.

## API'et i dette repositorium

Dette repositorium har sin egen implementation af API'et. Start den med `python -m cafe_api`; den lytter på `http://127.0.0.1:5000`.

| Verbum | Rute | Hvad den gør | Succes | Fejl |
| --- | --- | --- | --- | --- |
| `GET` | `/random` | Én tilfældig café | 200 `{"cafe": {...}}` | 404 hvis der ingen café er |
| `GET` | `/all` | Alle caféer | 200 `{"cafes": [...]}` |  |
| `GET` | `/search?loc=...` | Caféerne på en lokation, uanset store og små bogstaver | 200 `{"cafes": [...]}` | 400 uden `loc`, 404 hvis ingen passer |
| `POST` | `/add` | Opret en café fra en JSON-krop | 201 `{"cafe": {...}}` | 400 ved et manglende, tomt eller forkert felt, eller et navn der allerede findes |
| `PATCH` | `/update-price/<cafe_id>?new_price=...` | Ret kaffeprisen | 200 `{"cafe": {...}}` | 400 uden `new_price`, 404 ved ukendt id |
| `DELETE` | `/report-closed/<cafe_id>` | Fjern en lukket café; kræver headeren `X-API-Key` | 200 `{"message": "..."}` | 403 ved forkert eller manglende nøgle, 404 ved ukendt id |

- Hver fejl er JSON: `{"error": "..."}`.
- API-nøglen læses fra miljøvariablen `CAFE_API_KEY`, når en forespørgsel kommer. Der er ingen standardnøgle: er variablen ikke sat, svarer hver sletning 403.
- Lektionen sender nøglen som forespørgselsparameteren `api-key`. Her sendes den i headeren `X-API-Key`, så nøglen ikke havner i URL'er og logs.
- Kroppen til `POST /add` er et JSON-objekt med tekstfelterne `name`, `map_url`, `img_url`, `location`, `seats`, sand/falsk-felterne `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls` og en valgfri `coffee_price`.

Prøv dem (i Windows PowerShell brug `curl.exe`, eller send forespørgslerne fra Postman):

```bash
curl http://127.0.0.1:5000/random
curl "http://127.0.0.1:5000/search?loc=Peckham"
curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"name": "Example Cafe", "map_url": "https://example.com/map", "img_url": "https://example.com/img.jpg", "location": "Peckham", "seats": "10-20", "has_toilet": true, "has_wifi": true, "has_sockets": false, "can_take_calls": false, "coffee_price": "2.80"}'
curl -X PATCH "http://127.0.0.1:5000/update-price/1?new_price=3.20"
curl -X DELETE http://127.0.0.1:5000/report-closed/1 -H "X-API-Key: <your-key>"
```

## Hvad vi lærte

- Dokumentation er en del af et API-produkt.
- Postman genererer den fra de gemte forespørgsler, så test og dokumentation følges ad.

---

Forrige: [En café, der er lukket](Step-8-Delete-Cafe-da) · [Hjem](Home-da)
