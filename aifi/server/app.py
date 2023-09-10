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
    module_id = module_path.split(".")[-1]
    module =  importlib.import_module(module_path)
    module_config = module.initialize()
    module_config['id'] = module_id 
    module_config['url'] = f'/api/device/{module_id}'
    device_registry.append(module_config)
    app.mount(module_config['url'], module.app)

@app.get("/api/rig")
async def root():
   return {"devices": device_registry}