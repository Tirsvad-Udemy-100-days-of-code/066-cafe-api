"""Use case: find the cafes at a location."""

from cafe_api import constants
from cafe_api.application.dto.cafe_dto import CafeDto, to_dto
from cafe_api.domain.errors.cafe_errors import CafeNotFoundError, InvalidSearchError
from cafe_api.domain.repositories.cafe_repository import CafeRepository


class SearchCafes:
    """Return the cafes at a given location."""

    def __init__(self, repository: CafeRepository) -> None:
        """Create the use case.

        @param repository The port to read cafes from.
        """
        self._repository = repository

    def execute(self, location: str) -> list[CafeDto]:
        """Search by location.

        @param location The location to look for; surrounding blanks are ignored.
        @return The matching cafes, never empty.
        @throws InvalidSearchError when the location is blank.
        @throws CafeNotFoundError when no cafe matches.
        """
        wanted = location.strip()
        if not wanted:
            raise InvalidSearchError(constants.MSG_BLANK_LOCATION)
        cafes = self._repository.find_by_location(wanted)
        if not cafes:
            raise CafeNotFoundError(constants.MSG_NO_CAFE_AT_LOCATION)
        return [to_dto(cafe) for cafe in cafes]
