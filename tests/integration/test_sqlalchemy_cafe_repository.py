"""Integration tests of the SQLAlchemy repository against a SQLite file."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from flask import Flask

from cafe_api.infrastructure.persistence.database import db
from cafe_api.infrastructure.persistence.seed import seed_if_empty
from cafe_api.infrastructure.repositories.sqlalchemy_cafe_repository import (
    SqlAlchemyCafeRepository,
)
from cafe_api.presentation.app_factory import create_app


@pytest.fixture
def app(tmp_path: Path) -> Flask:
    return create_app(f"sqlite:///{tmp_path / 'repo.db'}", seed=True)


@pytest.fixture
def repository(app: Flask) -> Iterator[SqlAlchemyCafeRepository]:
    with app.app_context():
        yield SqlAlchemyCafeRepository(db.session)


def test_list_all_returns_seeded_cafes(repository: SqlAlchemyCafeRepository) -> None:
    cafes = repository.list_all()

    assert len(cafes) >= 6
    assert all(cafe.id > 0 for cafe in cafes)


def test_find_by_location_matches_case_insensitively(
    repository: SqlAlchemyCafeRepository,
) -> None:
    lower = repository.find_by_location("peckham")
    upper = repository.find_by_location("PECKHAM")

    assert len(lower) >= 2
    assert lower == upper
    assert {cafe.location for cafe in lower} == {"Peckham"}


def test_find_by_location_returns_empty_list_when_no_match(
    repository: SqlAlchemyCafeRepository,
) -> None:
    assert repository.find_by_location("Atlantis") == []


def test_seed_if_empty_does_not_insert_twice(
    app: Flask, repository: SqlAlchemyCafeRepository
) -> None:
    before = len(repository.list_all())

    assert seed_if_empty() is False
    assert len(repository.list_all()) == before
