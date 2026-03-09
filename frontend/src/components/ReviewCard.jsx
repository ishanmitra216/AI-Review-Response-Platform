import React from "react";

function ReviewCard({ review }) {

  return (
    <div className="review-card">
      <p>{review.text}</p>
      <small>Rating: {review.rating}</small>
    </div>
  );

}

export default ReviewCard;