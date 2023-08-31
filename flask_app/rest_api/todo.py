from flask_app.repositories import TodoRepository
from flask_restx import Namespace, Resource

from .schemas import TodoSchema

todo_ns = Namespace("todo", description="Todo operations")
todo_list_schema = TodoSchema(many=True)


@todo_ns.route("/")
class TodoList(Resource):
    @todo_ns.doc("List all the todo tasks")
    def get(self):
        return todo_list_schema.dump(TodoRepository.get_all()), 200
