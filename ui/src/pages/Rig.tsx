import { useEffect, useState } from 'react';
import '../App.css';
import axios from 'axios';
import { Pane } from 'evergreen-ui';
import Navigation from '../components/Navigation';


/**
 * The main component of the application.
 * Renders a grid with a single RackComponent.
 * @returns {JSX.Element} The rendered component.
 */
function Rig() {
  const [rig, setRig] = useState(undefined);
  const axiosurl = process.env.NODE_ENV === 'development' ? "http://localhost:8000" : "";
  useEffect(() => {
    axios.get(`${axiosurl}/api/rig`)
    .then((response) => {
      setRig(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
  }, []);
  return (
    <Pane>
      <Pane>
        <Navigation path={["Rig"]} />
          <h1>Rig</h1>
          <h2>Devices</h2>
            {rig !== undefined && rig.devices.map((device) => {
              return (<div key={device.id}>
                <h3>Device Specification</h3>
                <div>ID: {device.id}</div>
                <div>Label: {device.label}</div>
                <div>URL: {device.url}</div>
                <h4>API</h4>
                {Object.entries(device.api).map(([apikey, apivalue]) => {
                  return (<div key={`api-${apikey}`}>
                    {apikey} : {apivalue['type']}
                  </div>)
                })}
                <h4>Output</h4>
                {device.output.map((output) => {
                  return (<div key={`output-${output.id}`}>
                    {output.id}
                  </div>)
                })}
                <h3>{device.id} Components</h3>
                {device.templates.map((template) => {
                  return (<div key={`template-${template.id}`}>
                    {template.id} : {template.label}
                  </div>)
                })}
              </div>)
            })}
      </Pane> 
    </Pane>
  );
}

export default Rig;
