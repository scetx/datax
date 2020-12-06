import React from "react";
import { NODES, COLORS, HISTORY } from "../constants";

import { Generation, Status } from "../engine";

const GenerationsGraph = ({ generations }: { generations: Generation[] }) => {
  const widthFactor = 100 / HISTORY;
  return (
    <svg width="100%" height={NODES / 2}>
      {generations.map(({ generation, counts }, index) => (
        <g key={generation}>
          {counts[Status.Resistant] > 0 && (
            <rect
              x={`${index * widthFactor}%`}
              width={`${widthFactor}%`}
              y={0}
              height={counts[Status.Resistant] / 2}
              style={{
                fill: COLORS[Status.Resistant],
              }}
            />
          )}
          {counts[Status.Compromised] > 0 && (
            <rect
              x={`${index * widthFactor}%`}
              width={`${widthFactor}%`}
              y={(NODES - counts[Status.Compromised]) / 2}
              height={counts[Status.Compromised] / 2}
              style={{
                fill: COLORS[Status.Compromised],
              }}
            />
          )}
        </g>
      ))}
    </svg>
  );
};

export default GenerationsGraph;
