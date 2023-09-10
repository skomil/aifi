

import logging 

class DeviceConfig:
    VALUE_STRING = 'STRING'
    VALUE_BOOLEAN = 'BOOLEAN'
    VALUE_INTEGER = 'INTEGER'
    VALUE_FLOAT = 'FLOAT'
    VALUE_IMAGE = 'IMAGE'

    config = {}
    def __init__(self, label='') -> None:
        self.config = {
            'label': label,
            'api': {},
            'output': [],
        }
    
    def add_output(self, *args, **kwargs):
        logging.info(*args)
        self.config['output'].append(self.__add_connection(*args, **kwargs))
    
    def add_api(self, *args, **kwargs):
        connection = self.__add_connection(*args, **kwargs)
        self.config['api'][connection['id']] = connection
    
    def __add_connection(self, *args, **kwargs):
        output = {
            'id': args[0],
            'type': kwargs['type'] if 'type' in kwargs else DeviceConfig.VALUE_STRING,
            'label': kwargs['label'] if 'label' in kwargs else None,
            'description': kwargs['description'] if 'description' in kwargs else None,
            'required': kwargs['required'] if 'required' in kwargs else False,
        }
        return self.__clean_obj(output)
        

    def __clean_obj(self, obj):
        return {k: v for k, v in obj.items() if v is not None}