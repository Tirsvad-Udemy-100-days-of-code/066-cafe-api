"""The NewCafe entity: a cafe that has no id yet."""

from dataclasses import dataclass

from cafe_api import constants
from cafe_api.domain.errors.cafe_errors import InvalidCafeError


@dataclass(frozen=True, slots=True)
class NewCafe:
    """The facts of a cafe before the store gives it an id.

    The text fields must not be blank. The entity is immutable.

    @throws InvalidCafeError on creation when a text field is blank.
    """

    name: str
    map_url: str
    img_url: str
    location: str
    seats: str
    has_toilet: bool
    has_wifi: bool
    has_sockets: bool
    can_take_calls: bool
    coffee_price: str | None

    def __post_init__(self) -> None:
        """Check the business rule that required text is not blank."""
        for field in constants.FIELDS_REQUIRED_TEXT:
            if not getattr(self, field).strip():
                raise InvalidCafeError(constants.MSG_FIELD_BLANK.format(field=field))
