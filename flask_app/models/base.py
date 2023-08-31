from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, func

from flask_app.extensions import db


class PkModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


class TimeStampedPkModel(PkModel):
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
