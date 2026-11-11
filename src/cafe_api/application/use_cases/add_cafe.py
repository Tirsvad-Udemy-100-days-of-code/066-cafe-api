"""Use case: add a cafe."""

from cafe_api.application.dto.cafe_dto import CafeDto, to_dto
from cafe_api.application.dto.new_cafe_dto import NewCafeDto
from cafe_api.domain.entities.new_cafe import NewCafe
from cafe_api.domain.repositories.cafe_repository import CafeRepository


class AddCafe:
    """Store a new cafe."""

    def __init__(self, repository: CafeRepository) -> None:
        """Create the use case.

        @param repository The port to store cafes in.
        """
        self._repository = repository

    def execute(self, data: NewCafeDto) -> CafeDto:
        """Add the cafe.

        Surrounding blanks are removed from the text fields; a blank price
        is stored as no price.

        @param data The cafe to add.
        @return The stored cafe with its new id.
        @throws InvalidCafeError when a required text field is blank or the
            name is already taken.
        """
        price = data.coffee_price.strip() if data.coffee_price is not None else None
        new_cafe = NewCafe(
            name=data.name.strip(),
            map_url=data.map_url.strip(),
            img_url=data.img_url.strip(),
            location=data.location.strip(),
            seats=data.seats.strip(),
            has_toilet=data.has_toilet,
            has_wifi=data.has_wifi,
            has_sockets=data.has_sockets,
            can_take_calls=data.can_take_calls,
            coffee_price=price or None,
        )
        return to_dto(self._repository.add(new_cafe))
