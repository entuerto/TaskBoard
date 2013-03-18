# -*- coding: utf-8 -*-
"""
  tasks.utils
  ==================================

  utility functions 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: BSD, see LICENSE for more details.
"""
from flask import flash
from flaskext.wtf import Form


def flash_errors(form):
   for field, errors in form.errors.items():
      for error in errors:
         flash(u"[{0}]: {1}".format(field, error), 'error')

