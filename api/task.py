import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

task = Blueprint('task', 'task', url_prefix="/task/v1")

# SELECT ALL TASKS
@task.route('/', methods=["GET"])
def get_all_tasks():
    try:
        tasks = [model_to_dict(task) for task in models.Task.select()]
        return jsonify(data=tasks, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "There was an error getting the resource"})

# CREATE A TASK
@task.route('/', methods=["POST"])
def create_tasks():
    print(request.form, 'request')
    payload = request.form.to_dict()
    payload['user_id'] = 1
    # payload = request.get_json()
    print(payload, 'payload', type(payload), 'type')
    task = models.Task.create(**payload)
    print(task.__dict__, 'looking inside the task model')
    task_dict = model_to_dict(task)
    return jsonify(data=task_dict, status={"code": 201, "message": "Success"})

# SHOW ONE TASK ROUTE
@task.route('/<id>', methods=["GET"])
def get_one_task(id):
    task = models.Task.get_by_id(id)
    return jsonify(data=model_to_dict(task), status={"code": 201, "message": "Success"})

# UPDATING ONE TASK
@task.route('/<id>', methods=["PUT"])
def update_task(id):
    print(request)
    # payload = request.get_json()
    payload = request.form.to_dict()
    print(type(payload))
    # print(payload.form.to_dict())
    print(payload, 'line 40, concents of request')
    query = models.Task.update(**payload).where(models.Task.id == id)
    query.execute()
    updated_task = models.Task.get_by_id(id)
    return jsonify(data=model_to_dict(updated_task), status={"code": 200, "message": "Success"})

# DELETE A TASK
@task.route("/<id>", methods=["Delete"])
def delete_task(id):
    query = models.Task.delete().where(models.Task.id == id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "Resource deleted"})
    deleted_task = models.Task.get_by_id
