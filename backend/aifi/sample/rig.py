from aifi.api.models.rig import Rig as RigModel
from aifi.components.prompt import Prompt

class Rig():
    rig = None
    def __init__(self) -> None:
        self.__setup()
    
    
    def __setup(self):
        self.rig = RigModel()
        self.rig.racks = []
        self.rig.component_definitions = []
        self.rig.component_definitions.append(Prompt().get_definition())
    
    def get_instance(self):
        return self.rig