import React from 'react';
import { Rack, Component } from '../api';
import ComponentHolder from './CompHolder';
class RackComponent extends React.Component<Rack> {
    promptComponent: Component = {
        id: 'basicPrompt',
        input: [],
        output: [],
        config: {},
        ui: {}
    };

    sdModel: Component = {
        id: 'sdModel',
        input: [],
        output: [],
        config: {},
        ui: {}
    };
    

    state: Rack = {
    components: [this.promptComponent, this.sdModel],
    config: {},
  };
    render() {
        return (

            <div className="Rack">
                <h1>Rack</h1>
                {this.state.components !== undefined ? this.state.components.map((component: Component) => {
                    return (
                        <div className="Component" key={component.id}>
                            <ComponentHolder data={component} uiConfig={{}}/>
                        </div>
                    );
                })
               :<></> }  
            </div>  
        ); 
    }
}
export default RackComponent;