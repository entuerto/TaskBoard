# -*- coding: utf-8 -*-
"""
  TaskBoard
  ==================================

  Runs the application 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: BSD, see LICENSE for more details.
"""
import sys, os

local_lib = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(local_lib, "Lib"))

from flask_debugtoolbar import DebugToolbarExtension
from board import create_app

if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = os.environ.get('SERVER_CONFIG')

app = create_app(config_file)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

if __name__ == '__main__':
   app.run()

