from flask_security import AsaList, RoleMixin, UserMixin
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import backref, relationship

from .base import PkModel, TimeStampedPkModel


class RolesUsers(PkModel):
    __tablename__ = "roles_users"

    user_id = Column("user_id", Integer(), ForeignKey("user.id"))
    role_id = Column("role_id", Integer(), ForeignKey("role.id"))


class Role(TimeStampedPkModel, RoleMixin):
    __tablename__ = "role"

    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(255))
    permissions = Column(MutableList.as_mutable(AsaList()), nullable=True)


class User(TimeStampedPkModel, UserMixin):
    __tablename__ = "user"

    email = Column(String(255), unique=True, nullable=False)

    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    active = Column(Boolean(), nullable=False, default=False)
    confirmed_at = Column(DateTime())

    fs_uniquifier = Column(String(64), unique=True, nullable=False)

    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(64))
    current_login_ip = Column(String(64))
    login_count = Column(Integer)

    roles = relationship(
        "Role",
        secondary="roles_users",
        backref=backref("users", lazy="dynamic", cascade_backrefs=False),
    )
