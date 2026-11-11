"""JSON-ready response bodies of the cafe API."""

from dataclasses import asdict
from typing import Any

from cafe_api import constants
from cafe_api.application.dto.cafe_dto import CafeDto
from cafe_api.application.dto.new_cafe_dto import NewCafeDto
from cafe_api.domain.errors.cafe_errors import InvalidCafeError


def cafe_to_json(cafe: CafeDto) -> dict[str, Any]:
    """Turn a cafe DTO into a JSON-ready dict.

    The keys are the fields of the DTO, so the field list is stated once.

    @param cafe The DTO to convert.
    @return A dict of plain values.
    """
    return asdict(cafe)


def cafe_body(cafe: CafeDto) -> dict[str, Any]:
    """Build the body for a single cafe."""
    return {constants.JSON_KEY_CAFE: cafe_to_json(cafe)}


def cafes_body(cafes: list[CafeDto]) -> dict[str, Any]:
    """Build the body for a list of cafes."""
    return {constants.JSON_KEY_CAFES: [cafe_to_json(cafe) for cafe in cafes]}


def error_body(message: str) -> dict[str, str]:
    """Build the body for an error.

    @param message The text to show the client.
    """
    return {constants.JSON_KEY_ERROR: message}


def message_body(message: str) -> dict[str, str]:
    """Build the body for a plain success message.

    @param message The text to show the client.
    """
    return {constants.JSON_KEY_MESSAGE: message}


def _require(body: dict[str, Any], field: str) -> Any:
    # Any: the value is the unchecked JSON input that the caller type-checks.
    if field not in body:
        raise InvalidCafeError(constants.MSG_FIELD_REQUIRED.format(field=field))
    return body[field]


def parse_new_cafe(body: object) -> NewCafeDto:
    """Read and type-check the JSON body of POST /add.

    Blank text is left to the use case, which owns that rule.

    @param body The parsed JSON, or None when the request had no JSON body.
    @return The cafe to add.
    @throws InvalidCafeError naming the field that is missing or of the wrong type.
    """
    if not isinstance(body, dict):
        raise InvalidCafeError(constants.MSG_BODY_NOT_OBJECT)
    values: dict[str, Any] = {}
    for field in constants.FIELDS_REQUIRED_TEXT:
        value = _require(body, field)
        if not isinstance(value, str):
            raise InvalidCafeError(constants.MSG_FIELD_NOT_TEXT.format(field=field))
        values[field] = value
    for field in constants.FIELDS_REQUIRED_FLAG:
        value = _require(body, field)
        if not isinstance(value, bool):
            raise InvalidCafeError(constants.MSG_FIELD_NOT_FLAG.format(field=field))
        values[field] = value
    price = body.get(constants.FIELD_COFFEE_PRICE)
    if price is not None and not isinstance(price, str):
        raise InvalidCafeError(
            constants.MSG_FIELD_NOT_TEXT_OR_NULL.format(
                field=constants.FIELD_COFFEE_PRICE
            )
        )
    values[constants.FIELD_COFFEE_PRICE] = price
    return NewCafeDto(**values)
