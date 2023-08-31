from flask_app.models import Todo

from .base import AbstractRepository


class TodoRepository(AbstractRepository):
    model = Todo

    @classmethod
    def search_by_title(cls, search_term: str) -> list[Todo]:
        return cls.model.query.filter(cls.model.title.like(f"%{search_term}%")).all()
