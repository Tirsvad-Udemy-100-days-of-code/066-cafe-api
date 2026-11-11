"""Use case: pick one cafe at random."""

import random
from collections.abc import Callable, Sequence

from cafe_api import constants
from cafe_api.application.dto.cafe_dto import CafeDto, to_dto
from cafe_api.domain.entities.cafe import Cafe
from cafe_api.domain.errors.cafe_errors import CafeNotFoundError
from cafe_api.domain.repositories.cafe_repository import CafeRepository


class GetRandomCafe:
    """Return a randomly chosen cafe."""

    def __init__(
        self,
        repository: CafeRepository,
        choose: Callable[[Sequence[Cafe]], Cafe] = random.choice,
    ) -> None:
        """Create the use case.

        @param repository The port to read cafes from.
        @param choose The function that picks one cafe; injected so tests
            are deterministic.
        """
        self._repository = repository
        self._choose = choose

    def execute(self) -> CafeDto:
        """Pick a cafe.

        @return The chosen cafe.
        @throws CafeNotFoundError when no cafe is stored.
        """
        cafes = self._repository.list_all()
        if not cafes:
            raise CafeNotFoundError(constants.MSG_NO_CAFES)
        return to_dto(self._choose(cafes))
