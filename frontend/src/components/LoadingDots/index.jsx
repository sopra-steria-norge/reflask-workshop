import React from "react";
import useInterval from "../../hooks/useInterval";

const LoadingDots = () => {

  const [dots, setDots] = React.useState(".");

  useInterval(() => {
    if (dots.length >= 3) {
      setDots(".")
    } else {
      setDots(dots + ".");
    }
  }, 200);

  return (
    <span>{dots}</span>
  )

};

export default LoadingDots;