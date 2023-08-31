from click import command
from flask_app.extensions import db
from flask_app.models import Todo
from flask_app.models_factories import TodoFactory


@command(name="populate-db")
def populate_db():
    print("Removing all todos and creating 100 new ones.")
    Todo.query.delete()
    TodoFactory.create_batch(100)
    db.session.commit()
