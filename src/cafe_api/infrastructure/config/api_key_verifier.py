"""API key check against a key held in the environment."""

import hmac
import os
from collections.abc import Mapping

from cafe_api import constants


class EnvApiKeyVerifier:
    """Compares a presented key with the one in the environment.

    The key is read at each check and has no default. When the variable is
    unset or empty, every key is rejected. The key is never logged or returned.
    """

    def __init__(self, environ: Mapping[str, str] | None = None) -> None:
        """Create the verifier.

        @param environ The environment to read; defaults to the process
            environment, looked up at each check.
        """
        self._environ = environ

    def is_valid(self, key: str | None) -> bool:
        """Check a key in constant time.

        @param key The key the caller presented, None when there was none.
        @return True only when a key is configured and equals the presented one.
        """
        source = os.environ if self._environ is None else self._environ
        expected = source.get(constants.ENV_API_KEY, "")
        if not expected or not key:
            return False
        return hmac.compare_digest(key.encode("utf-8"), expected.encode("utf-8"))
