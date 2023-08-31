from flask import Blueprint, render_template, request
from flask_admin.contrib.sqla import ModelView

from flask_app.extensions import admin, db, htmx
from flask_app.models import Todo
from flask_app.repositories import TodoRepository

admin.add_view(ModelView(Todo, db.session))


blueprint = Blueprint("frontend", __name__, static_folder="../static")


@blueprint.route("/todo", methods=["GET", "POST"])
def todos_view():
    if htmx:
        search_term = request.form.get("search")
        if len(search_term):
            return render_template(
                "todos.html",
                todos=TodoRepository.search_by_title(search_term=search_term),
            )

    return render_template("index.html", todos=TodoRepository.get_all())
