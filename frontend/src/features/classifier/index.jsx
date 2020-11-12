import React, { useEffect, useRef, useState } from "react";
import useInterval from "../../hooks/useInterval";
import "./styles.css";

const Classifier = () => {

  useEffect(() => {
    // Kjører når komponentet rendres på skjermen.
  }, [])

  useInterval(async () => {
    // Kjører en gang i sekundet.
  }, 1000);

  return (
    <>
      <header>
        <h1>Image classifier</h1>
      </header>
      <p>Komponent for bildeklassifisering</p>
    </>
  )
};

export default Classifier;