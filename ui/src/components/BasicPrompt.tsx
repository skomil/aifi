import * as React from "react";
import {TextField} from '@mui/material';
import { Component } from "../api";
import { ComponentHolderProps } from "./CompHolder";

class BasicPrompt extends React.Component<ComponentHolderProps> {
  data: Component = this.props.data;

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
