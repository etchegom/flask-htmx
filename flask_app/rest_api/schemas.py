from flask_app.extensions import ma
from flask_app.models import Todo


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True
        include_fk = True
