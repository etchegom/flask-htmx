from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_app.extensions import db
from flask_app.models import Role, Todo, User

admin = Admin(name="Backoffice", template_mode="bootstrap3")


class TodoModelView(ModelView):
    page_size = 50


class UserModelView(ModelView):
    can_delete = False
    column_exclude_list = ["password"]


def create_admin_app(app: Flask):
    admin.init_app(app)
    # admin.init_app(app, index_view=MyAdminIndexView())

    admin.add_view(ModelView(User, db.session, category="Team"))
    admin.add_view(ModelView(Role, db.session, category="Team"))

    admin.add_view(TodoModelView(Todo, db.session))
