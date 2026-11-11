"""The port through which the use cases check an API key."""

from typing import Protocol


class ApiKeyVerifier(Protocol):
    """Decides whether a presented API key is valid."""

    def is_valid(self, key: str | None) -> bool:
        """Check a key.

        @param key The key the caller presented, None when there was none.
        @return True only when the key matches the configured one.
        """
        ...
