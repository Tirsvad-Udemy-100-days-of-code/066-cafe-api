"""Unit tests of the read use cases with a fake repository."""

from collections.abc import Sequence

import pytest

from cafe_api.application.use_cases.get_all_cafes import GetAllCafes
from cafe_api.application.use_cases.get_random_cafe import GetRandomCafe
from cafe_api.application.use_cases.search_cafes import SearchCafes
from cafe_api.domain.entities.cafe import Cafe
from cafe_api.domain.errors.cafe_errors import CafeNotFoundError, InvalidSearchError
from cafe_api.domain.repositories.cafe_repository import CafeRepository


def _pick_last(cafes: Sequence[Cafe]) -> Cafe:
    return cafes[-1]


def test_random_returns_chosen_cafe_when_cafes_exist(
    repository: CafeRepository,
) -> None:
    dto = GetRandomCafe(repository, choose=_pick_last).execute()

    assert dto.name == "Gamma"


def test_random_raises_not_found_when_repository_is_empty(
    empty_repository: CafeRepository,
) -> None:
    with pytest.raises(CafeNotFoundError):
        GetRandomCafe(empty_repository).execute()


def test_all_returns_every_cafe_as_dto(repository: CafeRepository) -> None:
    names = [dto.name for dto in GetAllCafes(repository).execute()]

    assert names == ["Alpha", "Beta", "Gamma"]


def test_all_returns_empty_list_when_repository_is_empty(
    empty_repository: CafeRepository,
) -> None:
    assert GetAllCafes(empty_repository).execute() == []


def test_search_returns_only_matching_location(repository: CafeRepository) -> None:
    names = [dto.name for dto in SearchCafes(repository).execute("Peckham")]

    assert names == ["Alpha", "Beta"]


def test_search_is_case_insensitive_and_ignores_surrounding_blanks(
    repository: CafeRepository,
) -> None:
    names = [dto.name for dto in SearchCafes(repository).execute("  pECKham ")]

    assert names == ["Alpha", "Beta"]


def test_search_raises_not_found_when_nothing_matches(
    repository: CafeRepository,
) -> None:
    with pytest.raises(CafeNotFoundError):
        SearchCafes(repository).execute("Atlantis")


@pytest.mark.parametrize("location", ["", "   "])
def test_search_raises_invalid_search_when_location_is_blank(
    repository: CafeRepository, location: str
) -> None:
    with pytest.raises(InvalidSearchError):
        SearchCafes(repository).execute(location)
