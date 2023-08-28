from flask import Blueprint, render_template, request
from flask_admin.contrib.sqla import ModelView

from .data import all_todos

from flask_app.extensions import admin, db, htmx
from .models import Todo

admin.add_view(ModelView(Todo, db.session))


blueprint = Blueprint("todos", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def todos_view():
    if htmx:
        search_term = request.form.get("search")
        filtered_todos = (
            all_todos
            if not len(search_term)
            else [t for t in all_todos if search_term in t["title"]]
        )
        return render_template("todos.html", todos=filtered_todos)

    return render_template("index.html", todos=all_todos)
