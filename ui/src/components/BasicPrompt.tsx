import * as React from "react";
import {TextField} from '@mui/material';
import { Device } from "../api";
import { ComponentHolderProps } from "./CompHolder";

class BasicPrompt extends React.Component<ComponentHolderProps> {
  data: Device = this.props.data;

  render() {
    return (
      
        <TextField
          id="outlined-multiline-flexible"
          label="Prompt"
          multiline
          fullWidth
        />
      
    );
  }
}
export default BasicPrompt;
