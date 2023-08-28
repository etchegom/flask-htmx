from extensions import db
from models import Todo
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin


admin = Admin(name="Backoffice", template_mode="bootstrap3")
admin.add_view(ModelView(Todo, db.session))
