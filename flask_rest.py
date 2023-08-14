import json
from flask import Flask, request, jsonify
from task import Task


app = Flask(__name__)


@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    return Task.tasks


@app.route('/post-tasks', methods=['POST'])
def post_tasks():
    data = json.loads(request.data)
    title = data["title"]
    Task.add_task(Task(), title)
    return Task.tasks


@app.route('/delete-tasks', methods=['DELETE'])
def delete_tasks():
    data = json.loads(request.data)
    task_id = data["task_id"]
    Task.delete_task(Task(), task_id)
    return Task.tasks


@app.route('/get-categories', methods=['GET'])
def get_categories():
    return Task.categories


@app.route('/post-categories', methods=['POST'])
def post_categories():
    data = json.loads(request.data)
    name = data["name"]
    Task.add_category(Task(), name)
    return Task.categories


@app.route('/delete-categories', methods=['DELETE'])
def delete_categories():
    data = json.loads(request.data)
    day_id = data['day_id']
    Task.delete_category(Task(), day_id)
    return Task.categories


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
