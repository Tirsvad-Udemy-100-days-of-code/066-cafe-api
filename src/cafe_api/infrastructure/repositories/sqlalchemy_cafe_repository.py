"""SQLAlchemy implementation of the cafe repository port."""

from collections.abc import Iterator
from contextlib import contextmanager

from flask_sqlalchemy.session import Session
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session

from cafe_api import constants
from cafe_api.domain.entities.cafe import Cafe
from cafe_api.domain.entities.new_cafe import NewCafe
from cafe_api.domain.errors.cafe_errors import InvalidCafeError
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
    """Reads and writes cafes in a SQL database through a SQLAlchemy session."""

    def __init__(self, session: scoped_session[Session]) -> None:
        """Create the repository.

        @param session The session to query with.
        """
        self._session = session

    @contextmanager
    def _transaction(self) -> Iterator[None]:
        """Commit the session on success, roll it back and re-raise on error."""
        try:
            yield
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise

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

    def add(self, new_cafe: NewCafe) -> Cafe:
        """Store a new cafe and commit.

        @param new_cafe The cafe to store.
        @return The stored cafe with its new id.
        @throws InvalidCafeError when the name is already taken.
        """
        model = CafeModel(
            name=new_cafe.name,
            map_url=new_cafe.map_url,
            img_url=new_cafe.img_url,
            location=new_cafe.location,
            seats=new_cafe.seats,
            has_toilet=new_cafe.has_toilet,
            has_wifi=new_cafe.has_wifi,
            has_sockets=new_cafe.has_sockets,
            can_take_calls=new_cafe.can_take_calls,
            coffee_price=new_cafe.coffee_price,
        )
        try:
            with self._transaction():
                self._session.add(model)
        except IntegrityError as error:
            raise InvalidCafeError(constants.MSG_DUPLICATE_NAME) from error
        return _to_entity(model)

    def get_by_id(self, cafe_id: int) -> Cafe | None:
        """Return one cafe.

        @param cafe_id The id to look for.
        @return The cafe, or None when the id is unknown.
        """
        model = self._session.get(CafeModel, cafe_id)
        return None if model is None else _to_entity(model)

    def update_coffee_price(self, cafe_id: int, price: str) -> Cafe | None:
        """Change the coffee price of a cafe and commit.

        @param cafe_id The id of the cafe to change.
        @param price The new price text.
        @return The updated cafe, or None when the id is unknown.
        """
        model = self._session.get(CafeModel, cafe_id)
        if model is None:
            return None
        with self._transaction():
            model.coffee_price = price
        return _to_entity(model)

    def delete(self, cafe_id: int) -> bool:
        """Remove a cafe and commit.

        @param cafe_id The id of the cafe to remove.
        @return True when a cafe was removed, False when the id is unknown.
        """
        model = self._session.get(CafeModel, cafe_id)
        if model is None:
            return False
        with self._transaction():
            self._session.delete(model)
        return True
