import  Grid from '@mui/material/Grid';
import { useEffect, useState } from 'react';
import '../App.css';
import axios from 'axios';


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
    <Grid container spacing={5} padding={2}>
      <Grid item xs={6}>
      <h1>Racks</h1>
      {rig !== undefined && rig.racks.map((rack) => {
        return (<div key={rack.id}>{rack.id}</div>)
      })}
      
      </Grid> 
    </Grid>
  );
}

export default Racks;
