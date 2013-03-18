# -*- coding: utf-8 -*-
"""
  task
  ==================================

  Represents a task todo 

  :copyright: (c) 2013 by Tomas Palazuelos.
  :license: GPLv2, see LICENSE for more details.
"""
from datetime import date

_tasks = dict()

class Task(object):

   def __init__(self, id=0, text="", priority="Normal", project="", due=date.today(), status="Not started", link=""):
      self._id = id
      self._text = text
      self._priority = priority
      self._project = project
      self._due = due
      self._status = status
      self._link = link

   @property
   def id(self):
      return self._id

   @id.setter
   def id(self, value):
      self._id = value

   @property
   def text(self):
      return self._text

   @text.setter
   def text(self, value):
      self._text = value

   @property
   def priority(self):
      return self._priority

   @priority.setter
   def priority(self, value):
      self._priority = value

   @property
   def project(self):
      return self._project

   @project.setter
   def project(self, value):
      self._project = value

   @property
   def due(self):
      return self._due

   @due.setter
   def due(self, value):
      self._due = value

   @property
   def status(self):
      return self._status

   @status.setter
   def status(self, value):
      self._status = value

   @property
   def link(self):
      return self._link

   @link.setter
   def link(self, value):
      self._link = value

   def as_dict(self):
      return {"id": self.id,
              "text": self.text,
              "priority": self.priority,
              "project": self.project,
              "due": self.due.isoformat(),
              "status": self.status,
              "link": self.link}
              
   
def task_model():
   return _tasks
