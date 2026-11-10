[English](Step-2-Random-Cafe) · **Dansk** · [Bahasa Malaysia](Step-2-Random-Cafe-ms)

# 2. En tilfældig café

![En tilfældig café](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-2.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionens beskrivelse. Det er ikke en optagelse af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/random` |

## Hvad lektionen gør

- Tilføj en `/random`-rute, der tager imod GET og vælger en tilfældig café fra databasen.
- Et API returnerer JSON i stedet for en HTML-skabelon, så SQLAlchemy-objektet skal serialiseres.
- `jsonify()` bygger JSON; du kan skrive hvert felt selv for at forme svaret, eller omdanne rækken til en ordbog og jsonify den.

## Hvad vi lærte

- Serialisering: at omdanne et databaseobjekt til JSON.
- Håndbygget JSON giver fuld kontrol (skjul id, gruppér booleans); en ordbog er hurtigere, når du vil have alle felter.

---

Forrige: [Startprojektet](Step-1-Starting-Project-da) · Næste: [Alle caféerne](Step-3-All-Cafes-da)
