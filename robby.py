#!/usr/bin/env python3
import sys
import logging

import robin
import db

db.upgrade()

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)
db.set_log(logger)

while True:
    print("> ", end="")
    cmd = input().split(' ')
    if cmd[0] == 'q':
      sys.exit(0)
    if cmd[0]:
      eval("robin." + cmd[0])(*cmd[1:])
