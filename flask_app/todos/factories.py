import factory
from flask_app.extensions import db

from .models import Todo


class TodoFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Todo
        sqlalchemy_session = db.session

    title = factory.Faker("sentence")
    completed = factory.Faker("boolean", chance_of_getting_true=25)
