import React, { useState } from "react";
import { Container, CssBaseline, Button, makeStyles } from "@material-ui/core";

import { createInitialState, createActiveHunt, createZeroTrust, runGeneration, State } from "./engine";
import { SIMULATOR_SIZE } from "./constants";
import useRequestAnimationFrame from "./useRequestAnimationFrame";

import GenerationsGraph from "./features/Histogram";
import Simulator from "./features/Simulator";
import Controls from "./features/Controls";

const useStyles = makeStyles({
  root: {
    background: "linear-gradient(90deg, #80cbc4 30%, #7e57c2 80%)",
    display: "grid",
    gridTemplateColumns: `450px ${SIMULATOR_SIZE}px`,
    marginTop: "1em",
    gridGap: 10,
  },

  graphBox: {
    background: "linear-gradient(45deg, #757575 30%, #212121 80%)",
    padding: 2,
    border: "1px solid #ccc",
    margin: 10,
  },

  description:{
      margin: 20,
      fontSize: 25,
      fontFamily: 'Trebuchet MS'
  }

});


const initialState = createInitialState();

const App = () => {
  const classes = useStyles();

  const [state, setState] = useState<State>(initialState);

  // initialState
  // function useState<S>(initialState: S | (() => S)): [S, Dispatch<SetStateAction<S>>];

  // undefined state
  // useState<S = undefined>(): [S | undefined, Dispatch<SetStateAction<S | undefined>>];

  const zeroTrust = () => {
      setState(createZeroTrust(state));
  }

  const activeHunt = () => {
    setState(createActiveHunt(state));
}

  const onRestart = () => {
    setState(createInitialState(state));
  };

  const onPause = () => {
    setState({
      ...state,
      paused: !state.paused,
    });

  };

  useRequestAnimationFrame(() => {
    setState(runGeneration(state));
  });

  return (
    <Container>
      <CssBaseline />
      <div className={classes.root}>
        <div>
          <Controls
            state={state}
            onChange={(key: string, value: number) =>
              setState({
                ...state,
                [key]: value,
              })
            }
          />
          <Button 
            variant="contained" 
            onClick={onPause} 
            fullWidth
            style={{ marginTop: "1rem", marginLeft: "1rem"}}>
            {state.paused ? "Play" : "Pause"}
          
          </Button>
          <Button
            variant="contained"
            onClick={onRestart}
            fullWidth
            style={{ marginTop: "1rem", marginLeft: "1rem"}}
          >
            Restart
          </Button>
        <div>
            <div className = {classes.description}>
                Settings for Stylized Scenarios
            </div>
        </div>

        <Button
            variant="contained"
            onClick={zeroTrust}
            fullWidth
            style={{ marginTop: "1rem", marginLeft: "1rem"}}
          >
            Zero Trust Network
          </Button>

          <Button
            variant="contained"
            onClick={activeHunt}
            fullWidth
            style={{ marginTop: "1rem", marginLeft: "1rem"}}
          >
            Active Threat Hunting
          </Button>

        </div>
        <div> 
          <div className={classes.graphBox}>
            <GenerationsGraph generations={state.generations} />
          </div>
          <div className={classes.graphBox}>
            <Simulator nodes={state.nodes} />
          </div>
        </div>
      </div>

    </Container>
  );

};

export default App;


