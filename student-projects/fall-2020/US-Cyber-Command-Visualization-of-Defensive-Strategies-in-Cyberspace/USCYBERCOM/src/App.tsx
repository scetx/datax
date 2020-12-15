import React, { useState } from "react";
import { Container, CssBaseline, Button, makeStyles } from "@material-ui/core";

import { createInitialState, createActiveHunt, createZeroTrust, runGeneration, State } from "./engine";
import { SIMULATOR_SIZE } from "./constants";
import useRequestAnimationFrame from "./useRequestAnimationFrame";

import GenerationsGraph from "./features/Histogram";
import Simulator from "./features/Simulator";
import Controls from "./features/Controls";
// this file is the root of our project and contains all the of child components for the rest of the program


// defining the aesthetics of our web page
const useStyles = makeStyles({

  // styling the background of our container
  root: {
    background: "linear-gradient(45deg, #80cbc4 30%, #7e57c2 80%)",
    display: "grid",
    gridTemplateColumns: `450px ${SIMULATOR_SIZE}px`,
    marginTop: "1em",
    gridGap: 10,
  },

  // styling the background of our simulation
  graphBox: {
    background: "linear-gradient(90deg, #757575 30%, #212121 80%)",
    padding: 2,
    border: "1px solid #ccc",
    margin: 10,
  },

  // the wording above the scenario buttons
  description:{
      margin: 20,
      fontSize: 25,
      fontFamily: 'Trebuchet MS'
  }

});

// instantiating the variable initialState to the function createInitialState
const initialState = createInitialState();


const App = () => {

  // ensures that each instance follows the styling defined above in useStyles()
  const classes = useStyles();

  const [state, setState] = useState<State>(initialState);
  // useState<State> is a hook/function that updates the state

  // other useState methods for undefined initial states
  // initialState
  // function useState<S>(initialState: S | (() => S)): [S, Dispatch<SetStateAction<S>>];

  // undefined state
  // useState<S = undefined>(): [S | undefined, Dispatch<SetStateAction<S | undefined>>];


  const zeroTrust = () => {
      setState(createZeroTrust(state));
      // returns settings of zero trust scenario
  }

  const activeHunt = () => {
    setState(createActiveHunt(state));
    // returns setting of active threat hunting
}

  const onRestart = () => {
    setState(createInitialState(state));
    // returns the simulation in an initial state
  };

  const onPause = () => {
    setState({
      ...state,
      paused: !state.paused,
      // returns a paused simulation with the current normal/compromised/resistant nodes
    });

  };

  useRequestAnimationFrame(() => {
    setState(runGeneration(state));
    // runs the ticks for simulation
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
            // defining the buttons that start/pause simulation/set parameter ticks
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
                Stylized Scenarios
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


