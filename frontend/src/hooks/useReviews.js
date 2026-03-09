import { useState } from "react";

export function useReviews() {

  const [reviews, setReviews] = useState([]);

  return {
    reviews,
    setReviews
  };

}