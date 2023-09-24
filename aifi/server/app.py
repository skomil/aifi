#!/usr/bin/env python3
from fastapi import FastAPI
import importlib
import logging

app = FastAPI(
        title="AIFI",
        description="A System for Integration of different AI Models",
        version="0.0.1",
    )

device_registry = []


def intialize(config):
    for device in config['devices']:
        __link_device(device)

def __link_device(module_path):
    logging.info(f"Loading Device: {module_path}")
    module_arr = module_path.split('.')
    module_id = module_arr.pop()
    module_cls = getattr(importlib.import_module('.'.join(module_arr)), module_id)
    module = module_cls()
    module_config = module.get_config()
    module_config['id'] = module_id 
    module_config['url'] = f'/api/device/{module_id.lower()}'
    device_registry.append(module_config)
    app.mount(module_config['url'], module.app)

@app.get("/api/rig")
async def root():
   return {"devices": device_registry}