import  Grid from '@mui/material/Grid';
import './App.css';
import RackComponent from './components/Rack';


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
