"""JSON-ready response bodies of the cafe API."""

from dataclasses import asdict
from typing import Any

from cafe_api import constants
from cafe_api.application.dto.cafe_dto import CafeDto


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
