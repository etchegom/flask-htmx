from click import command
from flask_app.todos.factories import TodoFactory


@command(name="populate-db")
def populate_db():
    print("Populating the database...")
    TodoFactory.create_batch(10)
