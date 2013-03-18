# -*- coding: utf-8 -*-
"""
  board.views
  ==================================

  This package contains all of the application's blueprints. 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: BSD, see LICENSE for more details.
"""
from flask import Flask
import main

def register_views(app):
   """Register the application views or extensions."""
   main.register(app)

