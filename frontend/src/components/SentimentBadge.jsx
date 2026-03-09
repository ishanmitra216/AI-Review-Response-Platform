import React from "react";

function SentimentBadge({ sentiment }) {

  const color =
    sentiment === "positive"
      ? "green"
      : sentiment === "negative"
      ? "red"
      : "gray";

  return (
    <span style={{ color }}>
      {sentiment}
    </span>
  );

}

export default SentimentBadge;