from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
from flask_htmx import HTMX

from todo import all_todos

app = Flask(__name__)

htmx = HTMX(app)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
assets.register("css", css)
css.build()


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


if __name__ == "__main__":
    app.run(debug=True)
