[English](Step-7-Update-Price) · **Dansk** · [Bahasa Malaysia](Step-7-Update-Price-ms)

# 7. En cafés kaffepris

![En cafés kaffepris](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-7.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionens beskrivelse. Det er ikke en optagelse af kursusprojektet.*

| Metode | Rute |
| --- | --- |
| `PATCH` | `/update-price/<cafe_id>` |

## Hvad lektionen gør

- Først ideen om PUT og PATCH: erstat alt, eller ret kun den ødelagte del.
- Tilføj en PATCH-rute `/update-price/<cafe_id>`; den nye pris er en parameter.
- Hent caféen på id i en try/except; findes den ikke, svar med en fejl og HTTP-status 404 i stedet for standardens 200.

## Hvad vi lærte

- Vælg PATCH, når kun ét felt ændres.
- En korrekt HTTP-statuskode (404 ikke fundet) fortæller klienten, hvad der skete, ikke kun beskedteksten.

---

Forrige: [En ny café](Step-6-Add-Cafe-da) · Næste: [En café, der er lukket](Step-8-Delete-Cafe-da)
