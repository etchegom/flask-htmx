from flask_app.extensions import db


class PkModel(db.Model):
    """Base model class that includes a primary key column named ``id``."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
