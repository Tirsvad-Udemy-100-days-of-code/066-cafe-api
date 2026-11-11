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

# Write endpoints.
ROUTE_ADD = "/add"
ROUTE_UPDATE_PRICE = "/update-price/<int:cafe_id>"
ROUTE_REPORT_CLOSED = "/report-closed/<int:cafe_id>"
BLUEPRINT_NAME_WRITE = "cafes_write"
QUERY_PARAM_NEW_PRICE = "new_price"

# API key. Only the NAME of the environment variable is stored here; the value
# is read at request time and has no default.
ENV_API_KEY = "CAFE_API_KEY"
HEADER_API_KEY = "X-API-Key"

# Request body fields of POST /add.
FIELDS_REQUIRED_TEXT = ("name", "map_url", "img_url", "location", "seats")
FIELDS_REQUIRED_FLAG = ("has_toilet", "has_wifi", "has_sockets", "can_take_calls")
FIELD_COFFEE_PRICE = "coffee_price"

# JSON keys and texts of the write responses.
JSON_KEY_MESSAGE = "message"
MSG_CAFE_DELETED = "The cafe was deleted."
MSG_CAFE_NOT_FOUND = "No cafe with that id was found."
MSG_ACCESS_DENIED = "A valid API key is required."
MSG_BODY_NOT_OBJECT = "The request body must be a JSON object."
MSG_FIELD_REQUIRED = "The field '{field}' is required."
MSG_FIELD_NOT_TEXT = "The field '{field}' must be a string."
MSG_FIELD_NOT_FLAG = "The field '{field}' must be true or false."
MSG_FIELD_NOT_TEXT_OR_NULL = "The field '{field}' must be a string or null."
MSG_FIELD_BLANK = "The field '{field}' must not be blank."
MSG_BLANK_NEW_PRICE = f"The query parameter '{QUERY_PARAM_NEW_PRICE}' is required."
MSG_DUPLICATE_NAME = "A cafe with that name already exists."
