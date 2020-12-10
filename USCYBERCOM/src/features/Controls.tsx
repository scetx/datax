// creating the sliders
import React from "react";
import { Slider, Typography } from "@material-ui/core";

import { State } from "../engine";

// FC = Function Component, process event handling
type NewType = React.FC<{ 
    onChange: (key: string, value: number) => void;
    state: State;
}>;

const Controls: NewType = ({ onChange, state }) => (
  <>
    <Typography id="virusSpreadRate-slider" gutterBottom>
      Virus Spread Rate
    </Typography>
    <Slider
      defaultValue={0.5}    // default value for virus rate
      value={state.virusSpreadRate}   // sets the slider to adjust virusSpreadRate variable
      aria-labelledby="virusSpreadRate-slider"  // naming slider
      valueLabelDisplay="on"  // displaying the little bubble above slider with the value
      step={0.05}   // step size
      onChange={(evt, value) => onChange("virusSpreadRate", value as number)}  // onChange function changes the settings of simulation 
      marks  // tick marks of slider
      min={0.05}  
      max={.5}
    />

    <Typography id="comrpomisedLength-slider" gutterBottom>
      Time in Compromised State
    </Typography>
    <Slider
      defaultValue={14}
      value={state.compromisedLength}
      aria-labelledby="comrpomisedLength-slider"
      valueLabelDisplay="on"
      step={0.5}
      onChange={(evt, value) => onChange("compromisedLength", value as number)}
      marks
      min={1}
      max={8}
    />
  </>

);

export default Controls;
