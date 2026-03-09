import API from "./api";

export const login = async (data) => {

  const res = await API.post("/auth/login", data);

  return res.data;

};