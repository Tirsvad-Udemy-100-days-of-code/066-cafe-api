"""The port through which the business rules read cafes."""

from typing import Protocol

from cafe_api.domain.entities.cafe import Cafe


class CafeRepository(Protocol):
    """Read access to the stored cafes."""

    def list_all(self) -> list[Cafe]:
        """Return every stored cafe.

        @return All cafes, an empty list when none is stored.
        """
        ...

    def find_by_location(self, location: str) -> list[Cafe]:
        """Return the cafes at a location.

        @param location The location to match, compared case-insensitively
            and exactly.
        @return The matching cafes, an empty list when none match.
        """
        ...
