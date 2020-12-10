// custom hook that powers the ticks animation frame of simulation
import { useEffect, useRef } from 'react';

const useRequestAnimationFrame = (callback: () => void) => {
  const savedCallback = useRef<() => void>();

  useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  useEffect(() => {
    let count = 0;
    function tick() {
      count += 1;
      // we use one out of two animation frames to make it run a bit slower
      if (count % 2 === 0) {
        savedCallback?.current?.();
      }
      id = requestAnimationFrame(tick);
    }
    let id = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(id);
  }, []);
}

export default useRequestAnimationFrame;