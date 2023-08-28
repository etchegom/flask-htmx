from app import db


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    completed = db.Column(db.Boolean())

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"<id {self.id}>"
