import * as React from 'react';
import { Device } from '../api';
import { ComponentHolderProps } from './CompHolder';

class SdModel extends React.Component<ComponentHolderProps> {
    data: Device = this.props.data;
    
    render() {
        return (<div>
            <div>Width: {}</div>
            <div>Height: {}</div>
            </div>)
    }
}
export default SdModel;
