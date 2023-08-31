from flask import Flask
from flask_security import SQLAlchemySessionUserDatastore

from flask_app import commands, frontend, rest_api
from flask_app.admin.views import create_admin_app
from flask_app.extensions import api, assets, db, debug_toolbar, htmx, ma, migrate, security
from flask_app.models.auth import Role, User


def create_app(config_object: str = "flask_app.settings") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    create_admin_app(app)

    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)
    htmx.init_app(app)
    assets.init_app(app)
    api.init_app(app)
    ma.init_app(app)

    user_datastore = SQLAlchemySessionUserDatastore(
        session=db.session, user_model=User, role_model=Role
    )
    security.init_app(app, user_datastore)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(frontend.views.blueprint, url_prefix="/frontend")
    app.register_blueprint(rest_api.views.blueprint, url_prefix="/api")


def register_commands(app: Flask) -> None:
    app.cli.add_command(commands.populate_db)
