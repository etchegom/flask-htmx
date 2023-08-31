from flask_app.repositories import TodoRepository
from flask_restx import Namespace, Resource

todo_ns = Namespace("todo", description="Todo operations")


@todo_ns.route("/")
class TodoList(Resource):
    # @todo_ns.doc('list_todos')
    # @todo_ns.marshal_list_with(todo)
    def get(self):
        return TodoRepository.get_all()
