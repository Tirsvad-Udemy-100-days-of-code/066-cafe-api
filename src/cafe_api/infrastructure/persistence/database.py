"""The Flask-SQLAlchemy database object shared by the models."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Declarative base of every table model."""


db = SQLAlchemy(model_class=Base)
