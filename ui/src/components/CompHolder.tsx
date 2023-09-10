import * as React from 'react';
import { Device } from '../api';
import SdModel from './SdModel';
import BasicPrompt from './BasicPrompt';

export interface ComponentHolderProps {
    uiConfig: object;
    data: Device;
}
const componentSwitch = (data: Device, config: Object) => {
    if (data.id === 'SdModel') {
        return <SdModel data={data} uiConfig={config} />
    } else if (data.id === 'BasicPrompt') {
        return <BasicPrompt data={data} uiConfig={config} />
    }
    return <div>Component Not Available</div>
}
class ComponentHolder extends React.Component<ComponentHolderProps> {
    
    render() {
        return (componentSwitch(this.props.data, this.props.uiConfig))
    }
}
export default ComponentHolder;