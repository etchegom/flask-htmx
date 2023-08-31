from flask import current_app
from flask_security.utils import hash_password

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


@command(name="create-admin-user")
def create_admin_user():
    # TODO: create role + user
    # app.security.datastore.find_or_create_role(
    #     name="user", permissions={"user-read", "user-write"}
    # )
    if not current_app.security.datastore.find_user(email="admin@me.com"):
        current_app.security.datastore.create_user(
            email="admin@me.com", password=hash_password("password")
        )
