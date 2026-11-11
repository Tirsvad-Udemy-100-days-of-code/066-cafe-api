"""The Cafe entity."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Cafe:
    """A cafe with the facts a remote worker looks for.

    The entity is immutable and holds no framework type.
    """

    id: int
    name: str
    map_url: str
    img_url: str
    location: str
    seats: str
    has_toilet: bool
    has_wifi: bool
    has_sockets: bool
    can_take_calls: bool
    coffee_price: str | None
