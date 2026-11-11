"""Errors raised by the cafe business rules."""


class CafeError(Exception):
    """Base class of every cafe business error."""


class CafeNotFoundError(CafeError):
    """Raised when no cafe matches the request."""


class InvalidSearchError(CafeError):
    """Raised when a search request is not valid."""
