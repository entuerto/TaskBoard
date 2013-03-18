# -*- coding: utf-8 -*-
"""
  taskboard
  ==================================

  Application factory function 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: BSD, see LICENSE for more details.
"""
from datetime import date

from flask import Flask
from board import webconfig
from board.task import Task, task_model
from board.views import register_views


def create_app(config):
   app = Flask(__name__)
   
   app.config.from_object(webconfig)

   if config:
      app.config.from_pyfile(config)

   app.debug = app.config['DEBUG']
   app.secret_key = app.config['SECRET_KEY']
    
   # register views (extensions)
   register_views(app)

   # setup the application security (users and login)
   # setup_security(app)
  
   # app.jinja_env.globals.update(dict(bytes_to_string=utils.bytes_to_string,))

   mock_tasks()

   return app


def mock_tasks():
   tasks = task_model()

   # id=0, text="", priority="Normal", project="", due=date.today(), status="Not started", link=""

   tasks[100] = Task(100, "Analyse dependants", "Normal", "vie2011", date(2013, 03, 01), "Not started", "")
   tasks[101] = Task(101, "Rosterplus error", "Normal", "yar2010", date(2013, 04, 01), "Not started", "")
   tasks[102] = Task(102, "Overtime 5110", "Low", "nsb2012", date(2013, 03, 10), "Not started", "")
   tasks[103] = Task(103, "Resume pour absence export", "High", "fly2010", date(2013, 03, 11), "In progress", "")
   tasks[104] = Task(104, "Vehicle assignment - should consider last assigned place", "Normal", "nsb2012", date(2013, 04, 01), "Not started", "")
   tasks[105] = Task(105, "SWER quand on entre un record en overlap dans einfo01", "Low", "nsb2012", date(2013, 05, 01), "Not started", "")
