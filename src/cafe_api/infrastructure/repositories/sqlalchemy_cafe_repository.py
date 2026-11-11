"""SQLAlchemy implementation of the cafe repository port."""

from flask_sqlalchemy.session import Session
from sqlalchemy import func, select
from sqlalchemy.orm import scoped_session

from cafe_api.domain.entities.cafe import Cafe
from cafe_api.infrastructure.persistence.cafe_model import CafeModel


def _to_entity(model: CafeModel) -> Cafe:
    return Cafe(
        id=model.id,
        name=model.name,
        map_url=model.map_url,
        img_url=model.img_url,
        location=model.location,
        seats=model.seats,
        has_toilet=model.has_toilet,
        has_wifi=model.has_wifi,
        has_sockets=model.has_sockets,
        can_take_calls=model.can_take_calls,
        coffee_price=model.coffee_price,
    )


class SqlAlchemyCafeRepository:
    """Reads cafes from a SQL database through a SQLAlchemy session."""

    def __init__(self, session: scoped_session[Session]) -> None:
        """Create the repository.

        @param session The session to query with.
        """
        self._session = session

    def list_all(self) -> list[Cafe]:
        """Return every stored cafe, ordered by id."""
        rows = self._session.scalars(select(CafeModel).order_by(CafeModel.id))
        return [_to_entity(row) for row in rows]

    def find_by_location(self, location: str) -> list[Cafe]:
        """Return the cafes whose location equals the given one, ignoring case.

        @param location The location to match.
        @return The matching cafes ordered by id, possibly empty.
        """
        query = (
            select(CafeModel)
            .where(func.lower(CafeModel.location) == location.lower())
            .order_by(CafeModel.id)
        )
        return [_to_entity(row) for row in self._session.scalars(query)]
