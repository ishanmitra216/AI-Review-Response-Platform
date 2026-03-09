import API from "./api";

export const fetchReviews = async () => {

  const res = await API.get("/reviews");

  return res.data;

};