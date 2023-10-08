import { useEffect, useState } from 'react';
import '../App.css';
import axios from 'axios';
import Navigation from '../components/Navigation';
import { Pane } from 'evergreen-ui';


/**
 * The main component of the application.
 * Renders a grid with a single RackComponent.
 * @returns {JSX.Element} The rendered component.
 */
function Racks() {
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
      <Navigation path={["Racks"]} />
      <Pane>
      <h1>Racks</h1>
      {rig !== undefined && rig.racks.map((rack) => {
        return (<a href={`/rack/${rack.id}`} key={rack.id}>{rack.id}</a>)
      })}
      
      </Pane> 
    </Pane>
  );
}

export default Racks;
