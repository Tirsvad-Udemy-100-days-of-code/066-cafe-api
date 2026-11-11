"""Shared fixtures for the unit tests: a fake cafe repository."""

from dataclasses import asdict, replace

import pytest

from cafe_api.domain.entities.cafe import Cafe
from cafe_api.domain.entities.new_cafe import NewCafe
from cafe_api.domain.errors.cafe_errors import InvalidCafeError

TEST_KEY = "unit-test-key"


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
        self.delete_calls = 0

    def list_all(self) -> list[Cafe]:
        return list(self._cafes)

    def find_by_location(self, location: str) -> list[Cafe]:
        wanted = location.lower()
        return [c for c in self._cafes if c.location.lower() == wanted]

    def add(self, new_cafe: NewCafe) -> Cafe:
        if any(c.name == new_cafe.name for c in self._cafes):
            raise InvalidCafeError("duplicate")
        next_id = max((c.id for c in self._cafes), default=0) + 1
        cafe = Cafe(id=next_id, **asdict(new_cafe))
        self._cafes.append(cafe)
        return cafe

    def get_by_id(self, cafe_id: int) -> Cafe | None:
        return next((c for c in self._cafes if c.id == cafe_id), None)

    def update_coffee_price(self, cafe_id: int, price: str) -> Cafe | None:
        cafe = self.get_by_id(cafe_id)
        if cafe is None:
            return None
        updated = replace(cafe, coffee_price=price)
        self._cafes[self._cafes.index(cafe)] = updated
        return updated

    def delete(self, cafe_id: int) -> bool:
        self.delete_calls += 1
        cafe = self.get_by_id(cafe_id)
        if cafe is None:
            return False
        self._cafes.remove(cafe)
        return True


class FakeApiKeyVerifier:
    """In-memory implementation of the ApiKeyVerifier port."""

    def __init__(self, expected: str | None) -> None:
        self._expected = expected

    def is_valid(self, key: str | None) -> bool:
        return self._expected is not None and key == self._expected


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


@pytest.fixture
def verifier() -> FakeApiKeyVerifier:
    return FakeApiKeyVerifier(TEST_KEY)
