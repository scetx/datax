// how the initial node "tranfers" the virus down the path

import React from "react";
import clsx from "clsx";

import { SIMULATOR_SIZE, BOX_SIZE, COLORS, CLASSES } from "../constants";

import { Node, Status } from "../engine";

const Simulator: React.FC<{ nodes: Node[] }> = ({ nodes }) => (
  <svg
    // using the viewBox to map between simulator area into the pixel area
    width={SIMULATOR_SIZE}
    height={SIMULATOR_SIZE}
    viewBox={`0 0 ${BOX_SIZE} ${BOX_SIZE}`}
    style={{
      overflow: "hidden",
    }}
  >
    {nodes.map(({ status, id, x, y, links }) => ( // creating graphics group for each node
      <g key={`links-${id}`}>  
        {links.map(({ status: status2, id: id2, x: x2, y: y2 }) => (
          <line
            key={[id, id2, x, y, x2, y2].join(":")}
            // the "links" key refers back to engine.ts file where the nodes and links are mapped out by a KD tree algorithm
            // creating the lines between nodes
            x1={x}
            y1={y}
            x2={x2}
            y2={y2}
            stroke={
              // if the previous node is compromise and the neighbor is normal, infect the neighbor
              status === Status.Compromised && status2 === Status.Normal
                ? COLORS[Status.Compromised]
                : "#ddd"
            }
            strokeWidth={0.8}
          />
        ))}
      </g>
    ))}
    {nodes.map(({ id, x, y, status, underAttack }) => (
      <g key={id}>
        <circle
          cx={x}
          cy={y}
          r={3}
          style={{
            stroke: "none",
            strokeWidth: 0,
          }}
          className={clsx(CLASSES[status], underAttack && "under-attack")}
        />
        {underAttack && (
          // this creates the lines that "travel" based on the state of the node
          <circle
            cx={x}
            cy={y}
            r={5}
            style={{
              stroke: COLORS[status],
              strokeWidth: 1,
              strokeOpacity: 0.2,
            }}
            className={clsx("ring", CLASSES[status])}
          />
        )}
      </g>
    ))}
  </svg>
);

export default Simulator;
