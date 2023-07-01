from aifi.api.models.component_definition import ComponentDefinition
from aifi.api.models.component_template import ComponentTemplate
from aifi.api.models.connection import Connection
from diffusers import StableDiffusionPipeline
import torch
import logging

class Sdmodel():
    sd = None
    definition = None
    active = False
    sdui_path = "../../../../../stable-diffusion-webui/models/Stable-diffusion/"
    input = {'prompt': ''}

    def __init__(self) -> None:
        self.__setup()
    
    def __setup(self):
        self.definition = ComponentDefinition(id="aifi.components.sdmodel",
                                         label="StableDiffusionModel",
                                         version="0.0.1"
                                        )
        inputs = []
        outputs = []
        inputs.append(Connection(id="prompt", label="Prompt", type="STRING"))
        outputs.append(Connection(id="image", label="Image", type="IMAGE"))
        default_template = ComponentTemplate(id="default",
                                         label="Default",
                                         input=inputs,
                                         output=outputs,)

        self.definition.component_templates = [default_template]

    def start(self):
        self.sd = StableDiffusionPipeline.from_ckpt(self.sdui_path + "analog-diffusion-1.0.ckpt",
                                         torch_dtype=torch.float16,
                                         use_safetensors=False, 
                                        )
        self.sd.to("cuda")
        self.active = True

    def update(self, input):
        self.input = input

    def get_definition(self) -> ComponentDefinition:
        return self.definition
    
    def run(self):
        logging.info("Running sdmodel")
        image = self.sd(self.input['prompt']).images[0]
        return {'image': image}
