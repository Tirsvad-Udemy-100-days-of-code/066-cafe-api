"""Errors raised by the cafe business rules."""


class CafeError(Exception):
    """Base class of every cafe business error."""


class CafeNotFoundError(CafeError):
    """Raised when no cafe matches the request."""


class InvalidSearchError(CafeError):
    """Raised when a search request is not valid."""


class InvalidCafeError(CafeError):
    """Raised when the data of a cafe is not valid."""


class AccessDeniedError(CafeError):
    """Raised when a request lacks a valid API key."""
