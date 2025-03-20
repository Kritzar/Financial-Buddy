import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import Graph from "./Graph";
import { useFinance } from "../context/FinanceContext";
import LineChart from "./LineChart";
import { Table } from "./Table";

const Dashboard = () => {
  const { income, expenses, budget } = useFinance();
  const navigate = useNavigate(); // Hook to navigate to other routes

  const [summary, setSummary] = useState({});
  const [transactionData, setTransactionData] = useState([]);
  const [predictions, setPredictions] = useState([]);

  const handleSignOut = () => {
    // Clear authentication or user data if needed
    localStorage.removeItem("user"); // Example: Remove user data from localStorage
    navigate("/"); // Redirect to sign-in page
  };

  async function fetchData() {
    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/get_transactions_data`,
        {
          params: { user_id: "BpYnK5iz7sbAGnl3Un5NxuSb6FC3" }, // Query parameter
          headers: { "Content-Type": "application/json" },
        }
      );

      setSummary(response.data.summary);
      setPredictions(response.data.predictions);

      setTransactionData(response.data.transactions);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="container" style={{ position: "relative" }}>
      <h1>Welcome to Your Personal Finance Dashboard</h1>

      {/* Sign Out Button */}
      {/* <button className="sign-out-btn" onClick={handleSignOut}>
        Sign Out
      </button> */}

      <div class="summary">
        <h3>Current Summary</h3>
        <p>Expected Income: {summary.income}</p>
        <p>Expected Expenses: {summary.expenses}</p>
        <p>Expected Savings: {summary.budget}</p>
      </div>

      {/* <div className="graph-container">
        <Graph />
      </div> */}

      {/* <div>
        <Link to="/income">Manage Income</Link>
        <Link to="/expenses">Manage Expenses</Link>
        <Link to="/budget">Set Budget</Link>
      </div> */}
      <br></br>
      <h1>Last Month Data:</h1>
      <div class="filter">
        <Table data={transactionData} />
      </div>
      <br></br>
      <h1>Predictions:</h1>
      <div class="line-chart">
        <LineChart dataInput={predictions} deviationThreshold={0} />
      </div>
    </div>
  );
};

export default Dashboard;
