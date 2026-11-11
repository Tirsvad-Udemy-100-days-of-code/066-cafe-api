"""The table model of a cafe."""

from sqlalchemy.orm import Mapped, mapped_column

from cafe_api import constants
from cafe_api.infrastructure.persistence.database import Base


class CafeModel(Base):
    """Row of the cafe table."""

    __tablename__ = constants.TABLE_NAME_CAFE

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    map_url: Mapped[str]
    img_url: Mapped[str]
    location: Mapped[str]
    seats: Mapped[str]
    has_toilet: Mapped[bool]
    has_wifi: Mapped[bool]
    has_sockets: Mapped[bool]
    can_take_calls: Mapped[bool]
    coffee_price: Mapped[str | None]
