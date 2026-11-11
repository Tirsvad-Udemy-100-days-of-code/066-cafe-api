"""Mapping of business errors to JSON error responses."""

from http import HTTPStatus

from flask import Flask, Response, jsonify

from cafe_api.domain.errors.cafe_errors import (
    AccessDeniedError,
    CafeNotFoundError,
    InvalidCafeError,
    InvalidSearchError,
)
from cafe_api.presentation.contracts.cafe_contract import error_body


def _json_error(error: Exception, status: HTTPStatus) -> tuple[Response, int]:
    return jsonify(error_body(str(error))), status.value


def handle_not_found(error: CafeNotFoundError) -> tuple[Response, int]:
    """Answer 404 with the error message as JSON."""
    return _json_error(error, HTTPStatus.NOT_FOUND)


def handle_invalid_search(error: InvalidSearchError) -> tuple[Response, int]:
    """Answer 400 with the error message as JSON."""
    return _json_error(error, HTTPStatus.BAD_REQUEST)


def handle_invalid_cafe(error: InvalidCafeError) -> tuple[Response, int]:
    """Answer 400 with the error message as JSON."""
    return _json_error(error, HTTPStatus.BAD_REQUEST)


def handle_access_denied(error: AccessDeniedError) -> tuple[Response, int]:
    """Answer 403 with the error message as JSON."""
    return _json_error(error, HTTPStatus.FORBIDDEN)


def register_error_handlers(app: Flask) -> None:
    """Register the JSON error handlers on the app.

    CafeNotFoundError answers 404, InvalidSearchError and InvalidCafeError
    answer 400, and AccessDeniedError answers 403.

    @param app The Flask app to extend.
    """
    app.register_error_handler(CafeNotFoundError, handle_not_found)
    app.register_error_handler(InvalidSearchError, handle_invalid_search)
    app.register_error_handler(InvalidCafeError, handle_invalid_cafe)
    app.register_error_handler(AccessDeniedError, handle_access_denied)
