"""Integration tests of the repository write methods against a SQLite file."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from flask import Flask

from cafe_api.domain.entities.new_cafe import NewCafe
from cafe_api.domain.errors.cafe_errors import InvalidCafeError
from cafe_api.infrastructure.persistence.database import db
from cafe_api.infrastructure.repositories.sqlalchemy_cafe_repository import (
    SqlAlchemyCafeRepository,
)
from cafe_api.presentation.app_factory import create_app


def _new_cafe(name: str = "Integration Cafe") -> NewCafe:
    return NewCafe(
        name=name,
        map_url="https://example.com/map",
        img_url="https://example.com/img.jpg",
        location="Bank",
        seats="0-10",
        has_toilet=True,
        has_wifi=False,
        has_sockets=True,
        can_take_calls=False,
        coffee_price=None,
    )


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "write.db"


@pytest.fixture
def app(db_path: Path) -> Flask:
    return create_app(f"sqlite:///{db_path}", seed=True)


@pytest.fixture
def repository(app: Flask) -> Iterator[SqlAlchemyCafeRepository]:
    with app.app_context():
        yield SqlAlchemyCafeRepository(db.session)


def test_add_stores_cafe_and_get_by_id_returns_it(
    repository: SqlAlchemyCafeRepository,
) -> None:
    stored = repository.add(_new_cafe())

    assert stored.id > 0
    assert repository.get_by_id(stored.id) == stored
    assert stored.coffee_price is None


def test_add_persists_beyond_the_session(
    app: Flask, repository: SqlAlchemyCafeRepository
) -> None:
    stored = repository.add(_new_cafe())
    db.session.remove()

    assert repository.get_by_id(stored.id) is not None


def test_add_raises_invalid_cafe_when_name_exists_and_session_stays_usable(
    repository: SqlAlchemyCafeRepository,
) -> None:
    repository.add(_new_cafe())
    before = len(repository.list_all())

    with pytest.raises(InvalidCafeError):
        repository.add(_new_cafe())

    assert len(repository.list_all()) == before


def test_get_by_id_returns_none_when_id_is_unknown(
    repository: SqlAlchemyCafeRepository,
) -> None:
    assert repository.get_by_id(99999) is None


def test_update_coffee_price_changes_and_persists_price(
    repository: SqlAlchemyCafeRepository,
) -> None:
    cafe_id = repository.list_all()[0].id

    updated = repository.update_coffee_price(cafe_id, "9.99")
    db.session.remove()

    assert updated is not None
    assert updated.coffee_price == "9.99"
    reloaded = repository.get_by_id(cafe_id)
    assert reloaded is not None
    assert reloaded.coffee_price == "9.99"


def test_update_coffee_price_returns_none_when_id_is_unknown(
    repository: SqlAlchemyCafeRepository,
) -> None:
    assert repository.update_coffee_price(99999, "1.00") is None


def test_delete_removes_cafe_and_second_delete_returns_false(
    repository: SqlAlchemyCafeRepository,
) -> None:
    cafe_id = repository.list_all()[0].id

    assert repository.delete(cafe_id) is True
    db.session.remove()
    assert repository.get_by_id(cafe_id) is None
    assert repository.delete(cafe_id) is False


def test_delete_returns_false_when_id_is_unknown(
    repository: SqlAlchemyCafeRepository,
) -> None:
    assert repository.delete(99999) is False
