from click import command
from flask_app.extensions import db
from flask_app.todos.factories import TodoFactory
from flask_app.todos.models import Todo


@command(name="populate-db")
def populate_db():
    print("Removing all todos and creating 100 new ones.")
    db.session.query(Todo).delete()
    TodoFactory.create_batch(100)
