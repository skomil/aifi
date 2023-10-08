#!/usr/bin/env python3
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import importlib
import logging

app = FastAPI(
        title="AIFI",
        description="A System for Integration of different AI Models",
        version="0.0.1",
    )

device_registry = []

racks = []

ui_routes = ["/rig", "/racks"]

templates = Jinja2Templates(directory="templates")

def intialize(config):
    for device in config['devices']:
        __link_device(device)
    for rack in config['racks']:
        racks.append(rack)
        ui_routes.append(f"/rack/{rack['id']}")
    for route in ui_routes:
        app.mount(route, StaticFiles(directory="ui_build", html=True), name=route)
        logging.info(f"adding ui route: {route}")


def __link_device(module_path):
    logging.info(f"Loading Device: {module_path}")
    module_arr = module_path.split('.')
    module_id = module_arr.pop()
    module_cls = getattr(importlib.import_module('.'.join(module_arr)), module_id)
    module = module_cls()
    module_config = module.get_config()
    module_config['id'] = module_path
    module_config['url'] = f'/api/device/{"/".join(module_arr)}'
    module_config['module'] = module_arr
    device_registry.append(module_config)
    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_methods=['*'],
                       allow_headers=['*'])
    app.mount(module_config['url'], module.app)

@app.get("/")
async def root(request: Request):
    if 'info' in request.query_params:
        return templates.TemplateResponse("index.html", {'request': request, 'devices': device_registry})
    else:
        return RedirectResponse(url='/racks')
    

@app.get("/api/rig")
async def rig():
   return {"devices": device_registry, "racks": racks}
