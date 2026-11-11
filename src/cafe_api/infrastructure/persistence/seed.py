"""Example data for a fresh database. All cafes are fictional."""

from sqlalchemy import select

from cafe_api.infrastructure.persistence.cafe_model import CafeModel
from cafe_api.infrastructure.persistence.database import db

_EXAMPLE_URL = "https://example.com"

# name, location, seats, toilet, wifi, sockets, calls, coffee price
_EXAMPLES: list[tuple[str, str, str, bool, bool, bool, bool, str | None]] = [
    ("Copper Kettle Corner", "Peckham", "20-30", True, True, True, False, "2.60"),
    ("Lantern Loft", "Peckham", "10-20", True, True, False, True, "2.90"),
    ("Quiet Harbour Roasters", "Shoreditch", "30-40", True, True, True, True, "3.10"),
    ("Paper Moon Cafe", "Hackney", "0-10", False, True, True, False, None),
    ("Willow Bench Coffee", "Greenwich", "40-50", True, False, False, True, "2.40"),
    ("Bright Window Bakery", "Brixton", "20-30", True, True, True, False, "2.75"),
]


def _build_model(
    row: tuple[str, str, str, bool, bool, bool, bool, str | None],
) -> CafeModel:
    name, location, seats, toilet, wifi, sockets, calls, price = row
    slug = name.lower().replace(" ", "-")
    return CafeModel(
        name=name,
        map_url=f"{_EXAMPLE_URL}/maps/{slug}",
        img_url=f"{_EXAMPLE_URL}/images/{slug}.jpg",
        location=location,
        seats=seats,
        has_toilet=toilet,
        has_wifi=wifi,
        has_sockets=sockets,
        can_take_calls=calls,
        coffee_price=price,
    )


def seed_if_empty() -> bool:
    """Insert the example cafes when the table has no rows.

    Must run inside an application context after the tables exist.

    @return True when rows were inserted, False when the table was not empty.
    """
    if db.session.scalars(select(CafeModel.id).limit(1)).first() is not None:
        return False
    db.session.add_all(_build_model(row) for row in _EXAMPLES)
    db.session.commit()
    return True
