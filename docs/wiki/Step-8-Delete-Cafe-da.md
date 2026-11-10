[English](Step-8-Delete-Cafe) · **Dansk** · [Bahasa Malaysia](Step-8-Delete-Cafe-ms)

# 8. En café, der er lukket

![En café, der er lukket](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/066-cafe-api/raw/branch/main/docs/images/step-8.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionens beskrivelse. Det er ikke en optagelse af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `DELETE` | `/report-closed/<cafe_id>` |

## Hvad lektionen gør

- Tilføj en DELETE-rute `/report-closed/<cafe_id>`.
- Beskyt den med en `api-key`-parameter: en forkert nøgle giver 403 Forbidden, en manglende café giver 404.
- Slet rækken og gem først, når nøglen er rigtig, og caféen findes.

## Hvad vi lærte

- Simpel autorisation: ikke alle må slette data.
- Rækkefølgen af kontroller har betydning: autorisér, slå op, og ret så.

---

Forrige: [En cafés kaffepris](Step-7-Update-Price-da) · Næste: [Dokumentér API'et](Step-9-API-Documentation-da)
