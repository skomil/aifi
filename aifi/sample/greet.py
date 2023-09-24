from aifi.builder.device import Device, DeviceConfig
import os
import logging
import asyncio

class Greet(Device):
    suffix = os.environ.get('AIFI_GREET_SUFFIX', '!')
    
    def __init__(self):
        super().__init__('Greet', label='Greet: An Example Device')
        self.device_config.add_api('prompt', type=DeviceConfig.VALUE_STRING, label='Prompt', required=True)
        self.device_config.add_api('performGreeting', type=DeviceConfig.VALUE_BOOLEAN, label='Perform Greeting', default=True)
        self.device_config.add_api('waitTime', type=DeviceConfig.VALUE_INTEGER, label='Wait Time', description='Simulate Wait time for testing async actions', default=3)
        self.device_config.add_config(f'{os.path.dirname(os.path.abspath(__file__))}/greet.config.json')
        self.device_config.add_output('result', required=True, label='Result')
        self.start()

    async def process(self, request):
        logging.info(f"Processing Request: {request}")  
        if request.performGreeting:
            greeting = 'Hello '
        else:
            greeting = ''
        return await asyncio.sleep(request.waitTime, result={'result': f"{greeting}{request.prompt}{self.suffix}"})

