**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Day 66: Cafe API wiki

Notes on Day 66 of the Udemy course 100 Days of Code: building your own REST API with Flask. The lecture turns a database of laptop-friendly cafes into a service that other programs can call. This wiki explains each step and what we gained from it. The repository holds no application code; the code belongs to the course.

## REST in short

- **REST** (REpresentational State Transfer) is a style for designing networked applications.
- **Client and server:** like a guest and the restaurant staff, the client asks and the server answers.
- **HTTP and HTTPS:** the language of the requests; HTTPS encrypts the traffic.
- **Request and response:** the client sends a request, the server may compute or query a database, and replies with a resource.
- **API design:** the API is the menu of what a client may ask for; REST gives the menu a standard shape.

## HTTP verbs and CRUD

| Verb | CRUD | Used for |
| --- | --- | --- |
| GET | Read | Fetch a resource |
| POST | Create | Add a new resource |
| PUT | Update | Replace a whole resource |
| PATCH | Update | Change part of a resource |
| DELETE | Delete | Remove a resource |

**PUT or PATCH?** A bicycle arrives with a broken tyre. PUT is sending back the whole bicycle for a new one; PATCH is sending only the tyre. PATCH is more efficient when one field changes.

## The lecture steps

| Step | Page |
| --- | --- |
| 1 | [The starting project](Step-1-Starting-Project) |
| 2 | [A random cafe](Step-2-Random-Cafe) |
| 3 | [All the cafes](Step-3-All-Cafes) |
| 4 | [Find a cafe](Step-4-Search) |
| 5 | [Postman](Step-5-Postman) |
| 6 | [A new cafe](Step-6-Add-Cafe) |
| 7 | [A cafe's coffee price](Step-7-Update-Price) |
| 8 | [A cafe that is closed](Step-8-Delete-Cafe) |
| 9 | [Document the API](Step-9-API-Documentation) |
