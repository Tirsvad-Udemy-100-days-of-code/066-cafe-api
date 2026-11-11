"""Shared fixtures for the unit tests: a fake cafe repository."""

import pytest

from cafe_api.domain.entities.cafe import Cafe


def make_cafe(cafe_id: int, name: str, location: str) -> Cafe:
    """Build a cafe with fixed values apart from id, name and location."""
    return Cafe(
        id=cafe_id,
        name=name,
        map_url="https://example.com/map",
        img_url="https://example.com/img.jpg",
        location=location,
        seats="10-20",
        has_toilet=True,
        has_wifi=True,
        has_sockets=False,
        can_take_calls=True,
        coffee_price="2.50",
    )


class FakeCafeRepository:
    """In-memory implementation of the CafeRepository port."""

    def __init__(self, cafes: list[Cafe]) -> None:
        self._cafes = cafes

    def list_all(self) -> list[Cafe]:
        return list(self._cafes)

    def find_by_location(self, location: str) -> list[Cafe]:
        wanted = location.lower()
        return [c for c in self._cafes if c.location.lower() == wanted]


@pytest.fixture
def sample_cafes() -> list[Cafe]:
    return [
        make_cafe(1, "Alpha", "Peckham"),
        make_cafe(2, "Beta", "Peckham"),
        make_cafe(3, "Gamma", "Soho"),
    ]


@pytest.fixture
def repository(sample_cafes: list[Cafe]) -> FakeCafeRepository:
    return FakeCafeRepository(sample_cafes)


@pytest.fixture
def empty_repository() -> FakeCafeRepository:
    return FakeCafeRepository([])
