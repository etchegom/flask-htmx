from flask import request

from flask_app.repositories import TodoRepository
from flask_restx import Namespace, Resource, fields

from .schemas import TodoSchema

todo_list_ns = Namespace("todo", description="Todo operations")
todo_ns = Namespace("todo", description="Todo operations")

todo_schema = TodoSchema()
todo_list_schema = TodoSchema(many=True)


todo_payload = todo_list_ns.model("Todo", {"title": fields.String("Title")})


@todo_list_ns.route("/")
class TodoList(Resource):
    @todo_list_ns.doc("List all the todo tasks")
    def get(self):
        return todo_list_schema.dump(TodoRepository.get_all()), 200

    @todo_list_ns.expect(todo_payload)
    @todo_list_ns.doc("Create a todo task")
    def post(self):
        payload = request.get_json()
        todo = TodoRepository.create(instance=todo_schema.load(payload))
        return todo_schema.dump(todo), 201


@todo_ns.route("/<int:id>")
class Todo(Resource):
    def get(self, id: int):
        todo = TodoRepository.get_by_id(id)
        if todo:
            return todo_schema.dump(todo), 200
        return 404
