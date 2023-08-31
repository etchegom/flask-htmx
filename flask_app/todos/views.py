from flask import Blueprint, render_template, request
from flask_admin.contrib.sqla import ModelView

from flask_app.extensions import admin, db, htmx

from .models import Todo

admin.add_view(ModelView(Todo, db.session))


blueprint = Blueprint("todos", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def todos_view():
    if htmx:
        search_term = request.form.get("search")
        if len(search_term):
            return render_template(
                "todos.html", todos=Todo.query.filter(Todo.title.like(f"%{search_term}%")).all()
            )

    return render_template("index.html", todos=Todo.query.all())
