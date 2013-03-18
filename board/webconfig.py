# -*- coding: utf-8 -*-
"""
  tasks.webconfig
  ==================================

  Default config variables. 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: BSD, see LICENSE for more details.
"""
#: Whether to run the application in debug mode or not. (Most of the time,
#: this should be `False`. Running this with `True` in production is a HUGE
#: security loophole.)
DEBUG = True


#: The secret key used to sign sessions. You can generate one with the command
#: ``python -c "import os; print(repr(os.urandom(20)))"``.
SECRET_KEY = 'TqBCxZahslzor9IbIhz2NTQd1fER08iWaUOHHCzrjY8='

#: Application title
TITLE = u'Task Board' 
