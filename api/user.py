# USER CONTROLLER

import models

import os
import sys
import secrets

# from PIL import Image ignore this unless we want to add profile pictures

# flask methods
from flask import Blueprint, request, jsonify, url_for, send_file

# other modules that we will use
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

# first argument, is the blueprint name
# second arg - is its import name
# 3 arg = this is what every route in the blueprint

user = Blueprint("users", "user", url_prefix="/user")

# @user.route('/login', methods=['POST'])

# register route
@user.route("/register", methods=["POST"])
def register_user():
    print(request)

    payload = request.get_json()  # set the form to variable, change it to dict
    print(payload)
    payload["email"].lower()
    try:
        models.User.get(models.User.email == payload["email"])

        return jsonify(
            data={},
            status={"code": 401, "message": "A user with that email already exists!"},
        )

    except models.DoesNotExist:

        payload["password"] = generate_password_hash(payload["password"])
        user = models.User.create(**payload)

        login_user(user)

        user_dict = model_to_dict(user)
        del user_dict["password"]
        return jsonify(data={}, status={"code": 200, "message": "Success"})


@user.route("/login", methods=["GET", "POST"])
def login():
    print(request)
    payload = request.get_json()  # set the form to variable, change it to dict
    print(payload)
    try:
        user = models.User.get(models.User.email == payload["email"])
        user_dict = model_to_dict(user)
        if check_password_hash(user_dict["password"], payload["password"]):
            del user_dict["password"]
            login_user(user)
            print(user_dict["username"], " this is user")
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
        else:
            return jsonify(
                data={},
                status={"code": 401, "message": "username or password is incorrect"},
            )
    except models.DoesNotExist:
        return jsonify(
            data={},
            status={"code": 401, "message": "Username or Password is incorrect"},
        )


# Show route
@user.route("/<id>", methods=["GET"])
def show_a_profile(id):
    user = models.User.get_by_id(id)
    return jsonify(data=model_to_dict(user), status={"code": 200, "message": "Success"})


# Edit route
@user.route("/<id>", methods=["PUT"])
def edit_profile(id):
    payload = request.get_json()
    query = models.User.update(**payload).where(models.User.id == id)
    query.execute()
    updateUser = models.User.get_by_id(id)
    return jsonify(
        data=model_to_dict(updateUser), status={"code": 200, "message": "Success"}
    )


# Delete route
@user.route("/<id>", methods=["DELETE"])
def delete_user(id):
    query = models.User.delete().where(models.User.id == id)
    query.execute()

    return jsonify(data="Delete successful", status={"code": 200, "message": "Success"})
