import logging 
import json
from pydantic import create_model, Field
from fastapi import FastAPI

class DeviceConfig:
    VALUE_STRING = 'STRING'
    VALUE_BOOLEAN = 'BOOLEAN'
    VALUE_INTEGER = 'INTEGER'
    VALUE_FLOAT = 'FLOAT'
    VALUE_IMAGE = 'IMAGE'

    __type_to_primitive = {
        VALUE_STRING: str,
        VALUE_BOOLEAN: bool,
        VALUE_INTEGER: int,
        VALUE_FLOAT: float,
        VALUE_IMAGE: str,
    }

    config = {}
    model = None

    def __init__(self, identifier, label='') -> None:
        self.config = {
            'identifier': identifier,
            'label': label,
            'api': {},
            'output': [],
            'templates': [],
        }
    
    def add_output(self, *args, **kwargs):
        logging.info(*args)
        self.config['output'].append(self.__add_connection(*args, **kwargs))
    
    def add_config(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            for key in data:
                if key == 'templates':
                    for template in data[key]:
                        self.config[key].append(template)

    def add_api(self, *args, **kwargs):
        connection = self.__add_connection(*args, **kwargs)
        self.config['api'][connection['id']] = connection
    
    def build_model(self):
        model = {}
        apiprops = self.__json_schema_process()
        for key in self.config['api']:
            model[key] = (self.__type_to_primitive[self.config['api'][key]['type']], Field(**apiprops[key]))
        self.model = create_model(f"{self.config['identifier']}Model", **model)
        return self.model

    def __add_connection(self, *args, **kwargs):
        output = {
            'id': args[0],
            'type': kwargs['type'] if 'type' in kwargs else DeviceConfig.VALUE_STRING,
            'label': kwargs['label'] if 'label' in kwargs else None,
            'description': kwargs['description'] if 'description' in kwargs else None,
            'required': kwargs['required'] if 'required' in kwargs else False,
        }
        if 'default' in kwargs:
            output['default'] = kwargs['default']
        return self.__clean_obj(output)
        

    def __clean_obj(self, obj):
        return {k: v for k, v in obj.items() if v is not None}
    
    def __json_schema_process(self):
        api_input = dict(self.__clean_obj(self.config['api']))
        api = {}
        for key in api_input:
            properties = dict(api_input[key])
            del(properties['type'])
            if 'label' in properties:
                properties['title'] = properties['label']
                del(properties['label'])
            api[key] = properties
        return api
    
class Device:
    app = FastAPI()
    device_config = None
    
    def __init__(self, *args, **kwargs) -> None:
        self.device_config = DeviceConfig(*args, **kwargs)
        self.app.add_api_route('/', self.execute, methods=['POST'])
        self.app.add_api_route('/config', self.config, methods=['GET'])
        self.app.add_api_route('/apiSchema', self.api, methods=['GET'])
        
    
    def get_config(self):
        return self.device_config.config

    def start(self):
        self.device_config.build_model()

    async def process(self, request):
        logging.info(f"This method should be overridden. Request: {request}")  
        return request
    
    async def execute(self, api: dict):
        object_api = self.device_config.model(**api)
        return await self.process(object_api)
        
    def config(self):
        return self.device_config.config
    
    def api(self):
        return self.device_config.model.model_json_schema()