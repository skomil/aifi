from aifi.api.models.component_definition import ComponentDefinition
from aifi.api.models.component_template import ComponentTemplate
from aifi.api.models.connection import Connection
from aifi.api.models.ui_setting import UiSetting

class Prompt():
    active = True
    definition = None
    output = {'output': ''}

    def __init__(self) -> None:
        self.__setup()
    
    def __setup(self):
        self.definition = ComponentDefinition(id="aifi.components.prompt",
                                         label="SimplePrompt",
                                         version="0.0.1"
                                        )
        basetemplate = ComponentTemplate(id="default", label="Default")
        basetemplate.input = []
        basetemplate.output = []
        basetemplate.output.append(Connection(id="output", label="Output", type="STRING"))
        basetemplate._ui_settings = []
        basetemplate._ui_settings.append(UiSetting(id="prompt", label="Prompt", data_type="STRING", ui_type="TEXT_AREA"))
        self.definition.component_templates = []
        self.definition.component_templates.append(basetemplate)


    def get_definition(self) -> ComponentDefinition:
        return self.definition
    
    def ui_update(self, input):
        self.output['output'] = input['prompt']

    def run(self):
        return self.output