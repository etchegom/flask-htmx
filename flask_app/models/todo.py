from sqlalchemy import Boolean, Column, String

from .base import PkModel


class Todo(PkModel):
    __tablename__ = "todos"

    title = Column(String)
    completed = Column(Boolean, default=False, nullable=False)

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"<Todo #{self.id}>"
