from fastapi import FastAPI
from aifi.builder.device import DeviceConfig

app = FastAPI()

device_config = DeviceConfig(label='Greet: An Example Device')


def __initialize():
    device_config.add_api('performGreeting', type=DeviceConfig.VALUE_BOOLEAN, label='Perform Greeting', default=False)
    device_config.add_output('result', required=True, label='Result')
    return device_config.config

__initialize()

@app.get('/')
async def root():
    return {'?': '??'}

@app.get('/process')
async def response():
    return {'message': 'hello'}



@app.get('/config')
def config():
    return device_config.config
