# -*- coding: utf-8 -*-
"""
  make_password
  ==================================

  Encodes a password for UserAccessManager 

  :copyright: (c) 2012 by Tomas Palazuelos.
  :license: BSD, see LICENSE for more details.
"""
import sys, os

local_lib = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(local_lib, "Lib"))

from werkzeug.security import generate_password_hash

def usage() :
    print """Usage: make_password.py (password to encode)
          """

if __name__ == "__main__":
   if len(sys.argv) < 2:
      usage()
      exit()

   print generate_password_hash(sys.argv[1], 'sha1', 16)

