"""The port through which the business rules read and write cafes."""

from typing import Protocol

from cafe_api.domain.entities.cafe import Cafe
from cafe_api.domain.entities.new_cafe import NewCafe


class CafeRepository(Protocol):
    """Access to the stored cafes."""

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

    def add(self, new_cafe: NewCafe) -> Cafe:
        """Store a new cafe.

        @param new_cafe The cafe to store.
        @return The stored cafe with its new id.
        @throws InvalidCafeError when a cafe with the same name exists.
        """
        ...

    def get_by_id(self, cafe_id: int) -> Cafe | None:
        """Return one cafe.

        @param cafe_id The id to look for.
        @return The cafe, or None when the id is unknown.
        """
        ...

    def update_coffee_price(self, cafe_id: int, price: str) -> Cafe | None:
        """Change the coffee price of a cafe.

        @param cafe_id The id of the cafe to change.
        @param price The new price text.
        @return The updated cafe, or None when the id is unknown.
        """
        ...

    def delete(self, cafe_id: int) -> bool:
        """Remove a cafe.

        @param cafe_id The id of the cafe to remove.
        @return True when a cafe was removed, False when the id is unknown.
        """
        ...
