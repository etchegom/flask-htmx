from flask import Flask, render_template, request
from flask_assets import Bundle, Environment

from todo import all_todos
from extensions import db, migrate, debug_toolbar, htmx
from admin import admin


def create_app(config_object: str = "settings") -> Flask:
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
    pass


@app.route("/", methods=["GET", "POST"])
def homepage():
    if htmx:
        search_term = request.form.get("search")
        filtered_todos = (
            all_todos
            if not len(search_term)
            else [t for t in all_todos if search_term in t["title"]]
        )
        return render_template("todo.html", todos=filtered_todos)

    return render_template("index.html", todos=all_todos)
