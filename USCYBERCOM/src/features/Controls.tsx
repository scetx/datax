import React from "react";
import { Slider, Typography } from "@material-ui/core";

import { State } from "../engine";

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
      defaultValue={0.5}
      value={state.virusSpreadRate}
      aria-labelledby="virusSpreadRate-slider"
      valueLabelDisplay="on"
      step={0.05}
      onChange={(evt, value) => onChange("virusSpreadRate", value as number)}
      marks
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
