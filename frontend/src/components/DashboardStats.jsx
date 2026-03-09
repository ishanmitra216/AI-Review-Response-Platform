import React from "react";

function DashboardStats({ stats }) {

  return (
    <div>
      <h3>Total Reviews: {stats.total}</h3>
    </div>
  );

}

export default DashboardStats;