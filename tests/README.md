# tests

The `pytest` tests of the code in `src/`, in the folders of the clean architecture:

| Folder | Proves |
| --- | --- |
| `unit` | The use cases with a fake repository, and that `domain` and `application` import no framework |
| `integration` | The SQLite repository against a real database file |
| `e2e` | The HTTP endpoints through the Flask test client |

Run `python -m pytest` from the repository root. The tests use temporary databases and never read `.env`.
