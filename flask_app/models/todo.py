from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .base import PkModel


class Todo(PkModel):
    __tablename__ = "todo"

    title = Column(String)
    completed = Column(Boolean, default=False, nullable=False)
    assignee_id = Column(Integer, ForeignKey("user.id"))

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"<Todo #{self.id}>"
