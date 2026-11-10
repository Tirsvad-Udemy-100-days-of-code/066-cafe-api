[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Dag 66: Cafe API-wiki

Noter til dag 66 af Udemy-kurset 100 Days of Code: at bygge sit eget REST API med Flask. Lektionen gør en database over computervenlige caféer til en tjeneste, andre programmer kan kalde. Denne wiki forklarer hvert trin og hvad vi lærte af det. Repositoriet indeholder ingen applikationskode; koden hører til kurset.

## REST kort fortalt

- **REST** (REpresentational State Transfer) er en stil til at designe netværksapplikationer.
- **Klient og server:** som en gæst og restaurantens personale spørger klienten, og serveren svarer.
- **HTTP og HTTPS:** sproget i forespørgslerne; HTTPS krypterer trafikken.
- **Forespørgsel og svar:** klienten sender en forespørgsel, serveren regner eller læser i en database og svarer med en ressource.
- **API-design:** API'et er menukortet over hvad en klient kan bede om; REST giver menukortet en standardform.

## HTTP-verber og CRUD

| Verbum | CRUD | Bruges til |
| --- | --- | --- |
| GET | Læs | Hent en ressource |
| POST | Opret | Tilføj en ny ressource |
| PUT | Opdater | Erstat en hel ressource |
| PATCH | Opdater | Ret en del af en ressource |
| DELETE | Slet | Fjern en ressource |

**PUT eller PATCH?** En cykel ankommer med et itu dæk. PUT er at sende hele cyklen retur og få en ny; PATCH er kun at sende dækket. PATCH er mere effektivt, når kun ét felt ændres.

## Lektionens trin

| Trin | Side |
| --- | --- |
| 1 | [Startprojektet](Step-1-Starting-Project-da) |
| 2 | [En tilfældig café](Step-2-Random-Cafe-da) |
| 3 | [Alle caféerne](Step-3-All-Cafes-da) |
| 4 | [Find en café](Step-4-Search-da) |
| 5 | [Postman](Step-5-Postman-da) |
| 6 | [En ny café](Step-6-Add-Cafe-da) |
| 7 | [En cafés kaffepris](Step-7-Update-Price-da) |
| 8 | [En café, der er lukket](Step-8-Delete-Cafe-da) |
| 9 | [Dokumentér API'et](Step-9-API-Documentation-da) |
