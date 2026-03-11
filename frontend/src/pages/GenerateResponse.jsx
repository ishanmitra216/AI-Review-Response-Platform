import React, { useState } from "react";
import API from "../services/api";

function GenerateResponse() {

  const [review, setReview] = useState("");
  const [response, setResponse] = useState("");

  const generate = async () => {
    try {
      const res = await API.post("/responses/generate", { text: review });
      setResponse(res.data.response);
    } catch (err) {
      console.error("generation error", err);
      setResponse("Error generating response");
    }
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