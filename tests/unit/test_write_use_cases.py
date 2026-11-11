"""Unit tests of the write use cases with fake ports."""

import pytest
from conftest import TEST_KEY, FakeApiKeyVerifier, FakeCafeRepository

from cafe_api.application.dto.new_cafe_dto import NewCafeDto
from cafe_api.application.use_cases.add_cafe import AddCafe
from cafe_api.application.use_cases.delete_cafe import DeleteCafe
from cafe_api.application.use_cases.update_coffee_price import UpdateCoffeePrice
from cafe_api.domain.errors.cafe_errors import (
    AccessDeniedError,
    CafeNotFoundError,
    InvalidCafeError,
)


def _new_cafe(name: str = "Delta", coffee_price: str | None = "3.00") -> NewCafeDto:
    return NewCafeDto(
        name=name,
        map_url="https://example.com/map",
        img_url="https://example.com/img.jpg",
        location="Bank",
        seats="0-10",
        has_toilet=False,
        has_wifi=True,
        has_sockets=True,
        can_take_calls=False,
        coffee_price=coffee_price,
    )


def test_add_returns_stored_cafe_with_new_id(repository: FakeCafeRepository) -> None:
    dto = AddCafe(repository).execute(_new_cafe())

    assert dto.id == 4
    assert dto.name == "Delta"
    assert repository.get_by_id(4) is not None


def test_add_accepts_missing_price(repository: FakeCafeRepository) -> None:
    dto = AddCafe(repository).execute(_new_cafe(coffee_price=None))

    assert dto.coffee_price is None


def test_add_stores_blank_price_as_no_price(repository: FakeCafeRepository) -> None:
    assert (
        AddCafe(repository).execute(_new_cafe(coffee_price="  ")).coffee_price is None
    )


@pytest.mark.parametrize("name", ["", "   "])
def test_add_raises_invalid_cafe_when_name_is_blank(
    repository: FakeCafeRepository, name: str
) -> None:
    with pytest.raises(InvalidCafeError, match="name"):
        AddCafe(repository).execute(_new_cafe(name=name))

    assert len(repository.list_all()) == 3


def test_add_raises_invalid_cafe_when_name_is_taken(
    repository: FakeCafeRepository,
) -> None:
    with pytest.raises(InvalidCafeError):
        AddCafe(repository).execute(_new_cafe(name="Alpha"))


def test_update_price_returns_updated_cafe(repository: FakeCafeRepository) -> None:
    dto = UpdateCoffeePrice(repository).execute(1, " 4.20 ")

    assert dto.coffee_price == "4.20"
    stored = repository.get_by_id(1)
    assert stored is not None
    assert stored.coffee_price == "4.20"


def test_update_price_raises_not_found_when_id_is_unknown(
    repository: FakeCafeRepository,
) -> None:
    with pytest.raises(CafeNotFoundError):
        UpdateCoffeePrice(repository).execute(99, "4.20")


@pytest.mark.parametrize("price", ["", "   "])
def test_update_price_raises_invalid_cafe_when_price_is_blank(
    repository: FakeCafeRepository, price: str
) -> None:
    with pytest.raises(InvalidCafeError):
        UpdateCoffeePrice(repository).execute(1, price)


def test_delete_removes_cafe_when_key_is_right(
    repository: FakeCafeRepository, verifier: FakeApiKeyVerifier
) -> None:
    DeleteCafe(repository, verifier).execute(TEST_KEY, 1)

    assert repository.get_by_id(1) is None


@pytest.mark.parametrize("key", ["wrong-key", "", None])
def test_delete_raises_access_denied_when_key_is_wrong_or_missing(
    repository: FakeCafeRepository, verifier: FakeApiKeyVerifier, key: str | None
) -> None:
    with pytest.raises(AccessDeniedError):
        DeleteCafe(repository, verifier).execute(key, 1)

    assert repository.get_by_id(1) is not None


def test_delete_raises_access_denied_when_no_key_is_configured(
    repository: FakeCafeRepository,
) -> None:
    unconfigured = FakeApiKeyVerifier(None)

    with pytest.raises(AccessDeniedError):
        DeleteCafe(repository, unconfigured).execute(TEST_KEY, 1)


def test_delete_raises_not_found_when_id_is_unknown_and_key_is_right(
    repository: FakeCafeRepository, verifier: FakeApiKeyVerifier
) -> None:
    with pytest.raises(CafeNotFoundError):
        DeleteCafe(repository, verifier).execute(TEST_KEY, 99)


def test_delete_checks_key_before_looking_up_the_cafe(
    repository: FakeCafeRepository, verifier: FakeApiKeyVerifier
) -> None:
    with pytest.raises(AccessDeniedError):
        DeleteCafe(repository, verifier).execute("wrong-key", 99)

    assert repository.delete_calls == 0
