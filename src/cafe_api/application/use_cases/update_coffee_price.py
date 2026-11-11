"""Use case: change the coffee price of a cafe."""

from cafe_api import constants
from cafe_api.application.dto.cafe_dto import CafeDto, to_dto
from cafe_api.domain.errors.cafe_errors import CafeNotFoundError, InvalidCafeError
from cafe_api.domain.repositories.cafe_repository import CafeRepository


class UpdateCoffeePrice:
    """Set a new coffee price on a stored cafe."""

    def __init__(self, repository: CafeRepository) -> None:
        """Create the use case.

        @param repository The port to read and change cafes with.
        """
        self._repository = repository

    def execute(self, cafe_id: int, new_price: str) -> CafeDto:
        """Update the price.

        @param cafe_id The id of the cafe to change.
        @param new_price The new price text; surrounding blanks are ignored.
        @return The updated cafe.
        @throws InvalidCafeError when the price is blank.
        @throws CafeNotFoundError when the id is unknown.
        """
        price = new_price.strip()
        if not price:
            raise InvalidCafeError(constants.MSG_BLANK_NEW_PRICE)
        cafe = self._repository.update_coffee_price(cafe_id, price)
        if cafe is None:
            raise CafeNotFoundError(constants.MSG_CAFE_NOT_FOUND)
        return to_dto(cafe)
