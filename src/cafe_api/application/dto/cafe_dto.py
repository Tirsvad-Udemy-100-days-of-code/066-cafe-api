"""The data transfer object that carries a cafe out of the application layer."""

from dataclasses import dataclass

from cafe_api.domain.entities.cafe import Cafe


@dataclass(frozen=True, slots=True)
class CafeDto:
    """Plain data of a cafe, safe to hand to the presentation layer."""

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


def to_dto(cafe: Cafe) -> CafeDto:
    """Map a cafe entity to its DTO.

    @param cafe The entity to map.
    @return The DTO with the same values.
    """
    return CafeDto(
        id=cafe.id,
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        seats=cafe.seats,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        has_sockets=cafe.has_sockets,
        can_take_calls=cafe.can_take_calls,
        coffee_price=cafe.coffee_price,
    )
