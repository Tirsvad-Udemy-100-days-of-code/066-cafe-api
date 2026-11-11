[English](Step-4-Search) · **Dansk** · [Bahasa Malaysia](Step-4-Search-ms)

# 4. Find en café

![Find en café](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-4.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionens beskrivelse. Det er ikke en optagelse af kursusprojektet.*

| Metode | Rute |
| --- | --- |
| `GET` | `/search?loc=...` |

## Hvad lektionen gør

- Tilføj en `/search`-rute; kalderen sender et område som forespørgselsparameter efter et spørgsmålstegn, fx `?loc=Peckham`.
- Filtrér forespørgslen med `where()` på områdekolonnen.
- Hvis intet passer, svar med en tydelig JSON-fejlbesked.

## Hvad vi lærte

- Forespørgselsparametre lader kalderen indsnævre resultatet uden at ændre ruten.
- Et hjælpsomt fejlsvar er en del af API-designet.

---

Forrige: [Alle caféerne](Step-3-All-Cafes-da) · Næste: [Postman](Step-5-Postman-da)
