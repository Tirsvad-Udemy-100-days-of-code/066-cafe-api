"""Use case: list every cafe."""

from cafe_api.application.dto.cafe_dto import CafeDto, to_dto
from cafe_api.domain.repositories.cafe_repository import CafeRepository


class GetAllCafes:
    """Return all stored cafes."""

    def __init__(self, repository: CafeRepository) -> None:
        """Create the use case.

        @param repository The port to read cafes from.
        """
        self._repository = repository

    def execute(self) -> list[CafeDto]:
        """List the cafes.

        @return Every cafe, an empty list when none is stored.
        """
        return [to_dto(cafe) for cafe in self._repository.list_all()]
