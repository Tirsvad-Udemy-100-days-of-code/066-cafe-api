# src

The source of the Flask cafe API, in the package `cafe_api`, laid out in the layers of the clean architecture:

| Layer | Holds |
| --- | --- |
| `domain` | The `Cafe` entity, the repository interface and the errors; imports no framework |
| `application` | The use cases and the data transfer objects |
| `infrastructure` | The SQLite persistence with Flask-SQLAlchemy, the seed data and the settings |
| `presentation` | The HTTP controllers (MVC for an API), the response contracts and the composition root |

Python 3.13 or newer, constants in `constants.py`, Doxygen comments, tests in `tests/`.
