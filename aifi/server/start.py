#!/usr/bin/env python3
from aifi.server.app import intialize
import uvicorn
import json
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

def start(config_path):
    intialize(json.load(open(config_path, 'r')))
    uvicorn.run('aifi.server.app:app')

