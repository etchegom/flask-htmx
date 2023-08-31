from flask import Blueprint

from flask_restx import Api

from .todo import todo_list_ns, todo_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Restful API",
    version="1.0",
    description="Main app restful API",
)

api.add_namespace(todo_list_ns)
api.add_namespace(todo_ns)
