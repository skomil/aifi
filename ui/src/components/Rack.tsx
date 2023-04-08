import React from 'react';
import { Stack, ListItem } from '@mui/material';
import { Rack, Component } from '../api';
import ComponentHolder from './CompHolder';
class RackComponent extends React.Component<Rack> {
    promptComponent: Component = {
        id: 'BasicPrompt',
        input: [],
        output: [{type: 'text'}],
        config: {},
        ui: {}
    };

    sdModel: Component = {
        id: 'SdModel',
        input: [{type: 'text'}],
        output: [{type: 'image'}],
        config: {width: 512, height: 512},
        ui: {}
    };
    

    state: Rack = {
    components: [this.promptComponent, this.sdModel],
    config: {},
  };
    render() {
        return (
            <div>
                 <h1>Rack</h1>
            
            <Stack className="Rack" spacing={4}>
               
                {this.state.components !== undefined ? this.state.components.map((component: Component) => {
                    return (
                        <ListItem className="Component" key={component.id}>
                            <ComponentHolder data={component} uiConfig={{}}/>
                        </ListItem>
                    );
                })
               :<></> }  
            </Stack>
            </div>  
        ); 
    }
}
export default RackComponent;