import models 

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

api = Blueprint('task', 'task', url_prefix="/task/v1")

@api.route('/', methods=['GET'])
deg get_alltasks():
