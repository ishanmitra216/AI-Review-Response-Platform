import React from "react";
import Dashboard from "./pages/Dashboard";
import Reviews from "./pages/Reviews";

export const routes = [
  { path: "/", element: <Dashboard /> },
  { path: "/reviews", element: <Reviews /> }
];