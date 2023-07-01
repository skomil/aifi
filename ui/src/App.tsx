import  Grid from '@mui/material/Grid';
import './App.css';
import RackComponent from './components/Rack';


/**
 * The main component of the application.
 * Renders a grid with a single RackComponent.
 * @returns {JSX.Element} The rendered component.
 */
function App() {
  return (
    <Grid container spacing={5} padding={2}>
      <Grid item xs={6}>
        <RackComponent/>
      </Grid> 
    </Grid>
  );
}

export default App;
