import * as React from 'react';
import { Component } from '../api';

export interface ComponentHolderProps {
    uiConfig: object;
    data: Component;
}
class ComponentHolder extends React.Component<ComponentHolderProps> {
    data: Component = this.props.data;

    
    render() {
        return (<div>{this.data.id}</div>)
    }
}
export default ComponentHolder;