"""Runtime configuration read from the environment."""

import os
from collections.abc import Mapping

from cafe_api import constants


def resolve_database_uri(environ: Mapping[str, str] | None = None) -> str:
    """Return the database URI to use.

    @param environ The environment to read; defaults to the process environment.
    @return The value of the database variable, else the default URI.
    """
    source = os.environ if environ is None else environ
    return source.get(constants.ENV_DATABASE_URL, constants.DEFAULT_DATABASE_URI)
