from flask_app.extensions import db

from .base import PkModel


class Todo(PkModel):
    __tablename__ = "todos"

    title = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"<Todo #{self.id}>"
