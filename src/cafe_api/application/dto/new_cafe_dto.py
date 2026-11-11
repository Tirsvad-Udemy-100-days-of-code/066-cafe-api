"""The data transfer object that carries a new cafe into the application layer."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NewCafeDto:
    """Plain data of a cafe to create, as the presentation layer received it."""

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
