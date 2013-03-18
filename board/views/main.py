# -*- coding: utf-8 -*-
"""
  board.views.board
  ==================================

  Handles task board page 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: GPLv2, see LICENSE for more details.
"""
import platform
import socket
import json

from flask import Blueprint, request
from flask import render_template, current_app
from flask import jsonify, make_response

from board.task import Task, task_model


board = Blueprint('board', __name__)


def register(app):
   app.register_blueprint(board)


@board.route('/')
def show_index():
   return render_template('index.html')


@board.route('/tasks', methods=['GET'])
def tasks():
   current_app.logger.info("[GET] /tasks")

   tasks = [(t.as_dict()) for t in task_model().itervalues()]

   #return jsonify(tasks=tasks)
   #return make_response(json.dumps(tasks, indent=None if request.is_xhr else 2), mimetype='application/json')
   return current_app.response_class(json.dumps(tasks, indent=None if request.is_xhr else 2), mimetype='application/json')


@board.route('/tasks/<int:id>', methods=['GET'])
def task(id):
   current_app.logger.info("[GET] /tasks/{0}".format(id))

   tasks = task_model();
   task = tasks.get(id)
   #return jsonify(task=task)
   return current_app.response_class(json.dumps(task.as_dict(), indent=None if request.is_xhr else 2), mimetype='application/json')


@board.route('/tasks', methods=['PUT'])
def add_task():
   return ""


@board.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
   print request.args
   current_app.logger.info("[DELETE] /tasks")
   return ""


