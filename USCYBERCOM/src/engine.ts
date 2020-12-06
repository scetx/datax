// we use a K-D Tree alg to connect nodes with nearby nodes
import { NODES, BOX_SIZE, HISTORY } from "./constants";
import createKDTree from "static-kdtree";

// enums allow us to delcare named variables
export enum Status {
    Resistant = -1,  // computer has enhanced defense mechanisms
    Normal = 0,      // an active, uncompromised computer
    Compromised = 1, // computer that has been infected with virus
}

// interface defines what the syntax of an object should be
export interface Node {
    id: number;         // unique ID number
    x: number;          // x position on box
    y: number;          // y position on box
    status: Status;     // status of computer
    compromisedState: number; // records time of being in compromised state
    links: Node[];      // links to nodes
    underAttack: boolean;    // True if node is under attack, else False
}

export interface Counts {
    [Status.Resistant]: number;     // num of resistant nodes
    [Status.Normal]: number;        // num of normal nodes
    [Status.Compromised]: number;   // num of compromised nodes
}

export interface Generation {
    generation: number;    // index of generation
    counts: Counts;        // current generation counts
}

export interface State {
    paused: boolean;  // True if simulation is paused
    nodes: Node[];  // nodes in simulation
    virusSpreadRate: number;     // rate of virus spread, how strong is the attack?
    compromisedLength: number;   // amount of time the node stays in compromised state
    generations: Generation[];   // history of each generation/tick
    generation: number;  // current generation index
}

// Create a generation of nodes and set the first node to get sick
export const generateNodes = (state: State): Node[] => {
    type Position = { x: number; y: number };
  
    // Creates a grid of locations for the nodes to spawn on
    const lines = Math.floor(Math.sqrt(NODES)) + 5;
    const separation = (BOX_SIZE - 10) / lines;
    const offset = 5;
    const positions: Position[] = [];
    const randomFactor = () => Math.random() * 2;
    for (let x = 0; x < lines; x++) {
      for (let y = 0; y < lines; y++) {
        positions.push({
          x: offset + x * separation + randomFactor(),
          y: offset + y * separation + randomFactor(),
        });
      }
    }
  
    // this constant will instantiate a random node to be infected 
    const grabPosition = (): Position =>
      positions.splice(Math.floor(Math.random() * positions.length), 1)[0];
      // ensures that no other node will get the same position
  
    // Create the initial set of nodes
    const nodes: Node[] = new Array(NODES).fill({}).map((n, i) => ({
      id: i,
      ...grabPosition(),
      status: i === 0 ? Status.Compromised : Status.Normal,
      compromisedState: state.compromisedLength,
      links: [] as Node[],

      underAttack: false,
    }));
  
    // Build the kd-tree from the nodes
    const tree = createKDTree(nodes.map(({ x, y }) => [x, y]));
  
    // finding neighbors for each node to link to
    nodes.forEach((node) => {
      tree
        .knn([node.x, node.y], 10)
        .slice(0, 4)
        .filter((i: number) => nodes[i].id !== node.id)
        .forEach((i: number) => {
          node.links.push(nodes[i]);
        });
    });
  
    return nodes;
  };

// run generation on all nodes
export const runGeneration = (state: State) => {
    if (state.paused) {
        return state;
    }

    // updating node status
    state.nodes.forEach((node:Node) => {
        node.underAttack = false;
        if (node.status === Status.Compromised && node.compromisedState > 0) {
            node.compromisedState -= 0.2;
            if (node.compromisedState < 1) {
                node.status = Status.Resistant;
            }
        }
    });

    // observing if compromised nodes have spread the virus
    state.nodes
        .filter(({ status }) => status === Status.Compromised)
        .forEach((node) => {
            node.links.forEach((target:Node) => {
                if (target.status === Status.Normal) {
                    if (Math.random() < state.virusSpreadRate) {
                        target.status = Status.Compromised;
                        target.compromisedState = state.compromisedLength;
                    }
                    else {
                        target.underAttack = true;
                    }
                }
            });
        });

    //record the history of current generation which will be displayed by the histogram
    const counts: Counts = state.nodes.reduce(
        (a: Counts, { status }) => {
            a[status] += 1;
            return a;
        },
        {
            [Status.Normal]: 0,
            [Status.Compromised]: 0,
            [Status.Resistant]: 0,
        }
    );
    state.generations.push({
        generation: state.generation,
        counts,
    });

    if (state.generations.length > HISTORY) {
        state.generations.splice(0,1);
    }

    return {
        ...state,
        generations: state.generations,
        generation: state.generation + 1,
        paused: counts[Status.Compromised] === 0,
    };
};

// initial status
export const createInitialState = (
    state: State = {
        virusSpreadRate: 0.05,
        compromisedLength: 10,
        generations: [],
        generation: 0,
        paused: false,
        nodes: [],
    }
): State => {
    const initialState: State = {
        ...state,
        paused: false,
        generations: [],
        nodes: []
    };
    initialState.nodes = generateNodes(initialState);
    return initialState;
};

export const createZeroTrust = (
    state: State = {
        virusSpreadRate: 0.11,
        compromisedLength: 7,
        generations: [],
        generation: 0,
        paused: false,
        nodes: [],
    }
): State => {
    const zeroTrust: State = {
        ...state,
        paused: false,
        generations: [],
        nodes: []
    };
    zeroTrust.nodes = generateNodes(zeroTrust);
    return zeroTrust;
};

export const createActiveHunt = (
    state: State = {
        virusSpreadRate: 0.11,
        compromisedLength: 4,
        generations: [],
        generation: 0,
        paused: false,
        nodes: [],
    }
): State => {
    const activeHunt: State = {
        ...state,
        paused: false,
        generations: [],
        nodes: []
    };
    activeHunt.nodes = generateNodes(activeHunt);
    return activeHunt;
};
    

