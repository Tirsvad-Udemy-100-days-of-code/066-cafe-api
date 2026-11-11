"""Fixed values of the cafe API, defined once.

This module imports nothing from the project, so every layer may use it.
"""

# Routes and request parameters.
ROUTE_RANDOM = "/random"
ROUTE_ALL = "/all"
ROUTE_SEARCH = "/search"
QUERY_PARAM_LOCATION = "loc"
BLUEPRINT_NAME = "cafes"

# Configuration.
ENV_DATABASE_URL = "CAFE_API_DATABASE_URL"
DEFAULT_DATABASE_URI = "sqlite:///cafes.db"
CONFIG_KEY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
TABLE_NAME_CAFE = "cafe"

# JSON keys of the response envelopes.
JSON_KEY_ERROR = "error"
JSON_KEY_CAFE = "cafe"
JSON_KEY_CAFES = "cafes"

# Error messages shown to the client.
MSG_NO_CAFES = "No cafe is available."
MSG_NO_CAFE_AT_LOCATION = "No cafe was found at that location."
MSG_BLANK_LOCATION = f"The query parameter '{QUERY_PARAM_LOCATION}' is required."
