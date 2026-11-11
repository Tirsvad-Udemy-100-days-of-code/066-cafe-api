"""Composition root: builds the Flask app and wires every layer."""

from flask import Flask

from cafe_api import constants
from cafe_api.application.use_cases.get_all_cafes import GetAllCafes
from cafe_api.application.use_cases.get_random_cafe import GetRandomCafe
from cafe_api.application.use_cases.search_cafes import SearchCafes
from cafe_api.infrastructure.config.settings import resolve_database_uri
from cafe_api.infrastructure.persistence.database import db
from cafe_api.infrastructure.persistence.seed import seed_if_empty
from cafe_api.infrastructure.repositories.sqlalchemy_cafe_repository import (
    SqlAlchemyCafeRepository,
)
from cafe_api.presentation.controllers.cafe_controller import create_cafe_blueprint
from cafe_api.presentation.shared.error_handlers import register_error_handlers


def create_app(database_uri: str | None = None, seed: bool = True) -> Flask:
    """Create the configured Flask app.

    @param database_uri The SQLAlchemy URI; when None it comes from the
        environment, else the default file database.
    @param seed Whether to insert the example cafes into an empty database.
    @return The app, with tables created and routes registered.
    """
    app = Flask(__name__)
    app.config[constants.CONFIG_KEY_DATABASE_URI] = (
        database_uri or resolve_database_uri()
    )
    db.init_app(app)

    repository = SqlAlchemyCafeRepository(db.session)
    app.register_blueprint(
        create_cafe_blueprint(
            GetRandomCafe(repository),
            GetAllCafes(repository),
            SearchCafes(repository),
        )
    )
    register_error_handlers(app)

    with app.app_context():
        db.create_all()
        if seed:
            seed_if_empty()
    return app
