import React, { useEffect, useRef, useState } from "react";
import useInterval from "../../hooks/useInterval";
import "./styles.css";

const Classifier = () => {
  const videoRef = useRef();
  const imageRef = useRef();
  const canvasRef = useRef();

  const [result, setResult] = useState("");

  useEffect(() => {
    // Kjører når komponentet rendres på skjermen.
    async function getCameraStream() {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: false, video: { facingMode: 'environment' }
      })
      videoRef.current.srcObject = stream;
    };
      getCameraStream();
  }, []);

  useInterval(async () => {
    // Kjører en gang i sekundet.
    await captureImageFromCamera();

    if (imageRef.current) {
      const formData = new FormData();
      formData.append('image', imageRef.current);

      const response = await fetch('/classify', {
        method: "POST",
        body: formData,
      });

      if (response.status === 200) {
        const text = await response.text();
        setResult(text);
      } else {
        setResult("Error from API.");
      }
    }
  }, 1000);

  const playCameraStream = () => {
    if (videoRef.current) {
      videoRef.current.play();
    }
  };

  const captureImageFromCamera = async () => {
    const context = canvasRef.current.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    context.drawImage(videoRef.current, 0, 0, window.innerWidth, window.innerHeight);

    canvas.toBlob((blob) => {
      imageRef.current = blob;
    })
  };

  return (
    <>
      <header>
        <h1>Image classifier</h1>
      </header>
        <main>
          <div className="video-container">
            <video ref={videoRef} onCanPlay={() => playCameraStream()} id="video" />
            <p className="result-text">Currently seeing: {result}</p>
            <canvas ref={canvasRef} id="canvas"></canvas>
          </div>
        </main>
    </>
  )
};

export default Classifier;