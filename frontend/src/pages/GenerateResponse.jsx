import React, { useState } from "react";
import axios from "axios";

function GenerateResponse() {

  const [review, setReview] = useState("");
  const [response, setResponse] = useState("");

  const generate = async () => {

    const res = await axios.post(
      "http://localhost:8000/responses/generate",
      { text: review }
    );

    setResponse(res.data.response);
  };

  return (
    <div>
      <textarea
        rows="5"
        value={review}
        onChange={(e) => setReview(e.target.value)}
      />

      <br/>

      <button onClick={generate}>
        Generate Response
      </button>

      <p>{response}</p>
    </div>
  );
}

export default GenerateResponse;