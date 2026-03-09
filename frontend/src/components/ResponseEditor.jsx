import React from "react";

function ResponseEditor({ response, setResponse }) {

  return (
    <textarea
      rows="5"
      value={response}
      onChange={(e) => setResponse(e.target.value)}
    />
  );

}

export default ResponseEditor;