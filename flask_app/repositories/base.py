from typing import Type, TypeVar

from flask_app.extensions import db
from flask_app.models.base import PkModel

T = TypeVar("T", bound="PkModel")


class AbstractRepository:
    model: Type[PkModel]

    __abstract__ = True

    @classmethod
    def get_all(cls) -> list[Type[T]]:
        return cls.model.query.all()

    @classmethod
    def get_by_id(cls, id: int) -> Type[T]:
        return db.session.get(cls.model, id)
