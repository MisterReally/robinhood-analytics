#!/usr/bin/env python3
import redis
import time
import sys
import json
import sys
import configparser
import pdb
import logging

from p import robin
from p import lib
from p import db

config = configparser.ConfigParser()
config.read('secrets.ini')

lib.upgrade()

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)
db.set_log(logger)

robin.config = config['config']

while True:
    print("> ", end="")
    cmd = input().split(' ')
    if cmd[0] == 'q':
      sys.exit(0)
    if cmd[0]:
      eval("robin." + cmd[0])(*cmd[1:])