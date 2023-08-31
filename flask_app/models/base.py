from datetime import datetime

from flask_app.extensions import db
from sqlalchemy import Column, DateTime, Integer, func


class PkModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


class TimeStampedModel(PkModel):
    __abstract__ = True

    created = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
    modified = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=datetime.utcnow,
    )
