from flask import Flask
from flask_assets import Bundle, Environment

from flask_app.todos.views import blueprint as todos_bp
from flask_app.extensions import admin, db, debug_toolbar, htmx, migrate


def create_app(config_object: str = "flask_app.settings") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    # TODO: move to somewhere else
    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css")
    assets.register("css", css)
    css.build()

    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    debug_toolbar.init_app(app)
    htmx.init_app(app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(todos_bp, url_prefix='/todo')
