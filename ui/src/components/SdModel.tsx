import * as React from 'react';
import { Component } from '../api';
import { ComponentHolderProps } from './CompHolder';

class SdModel extends React.Component<ComponentHolderProps> {
    data: Component = this.props.data;
    config: any = this.data.config;
    
    render() {
        return (<div>
            <div>Width: {this.config.width}</div>
            <div>Height: {this.config.height}</div>
            </div>)
    }
}
export default SdModel;
