from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from uuid import uuid4

app = Flask(__name__)
api = Api(app)

TASKS = {}


def abort_if_task_does_not_exist(task_id):
    if task_id not in TASKS:
        abort(404, message=f"Task {task_id} doesn't exist")


parser = reqparse.RequestParser()
parser.add_argument('task')


class Task(Resource):
    def get(self, task_id):
        abort_if_task_does_not_exist(task_id)
        return TASKS[task_id]

    def delete(self, task_id):
        abort_if_task_does_not_exist(task_id)
        del TASKS[task_id]
        return '', 204

    def put(self, task_id):
        args = parser.parse_args()
        TASKS[task_id] = {'task': args['task'], 'id': task_id}
        return TASKS[task_id], 200


class TaskList(Resource):
    def get(self):
        return list(TASKS.values())

    def post(self):
        args = parser.parse_args()
        task_id = uuid4().hex
        TASKS[task_id] = {'task': args['task'], 'id': task_id}
        return TASKS[task_id], 201


api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<task_id>')


if __name__ == '__main__':
    app.run(debug=True)
