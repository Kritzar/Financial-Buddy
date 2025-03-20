import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { FinanceProvider } from "./context/FinanceContext"; // Import the FinanceProvider
import AuthPage from "./components/AuthPage";
import BankDetails from "./components/BankDetails";
import Dashboard from "./components/Dashboard";
import IncomePage from "./components/IncomePage"; // Import the IncomePage
import ExpensePage from "./components/ExpensePage"; // Import the ExpensePage
import BudgetPage from "./components/BudgetPage"; // Import the BudgetPage

const App = () => {
  return (
    <FinanceProvider>
      {" "}
      {/* Wrap the app with FinanceProvider */}
      <Router>
        <Routes>
          <Route path="/" element={<AuthPage />} />
          <Route path="/bank-details" element={<BankDetails />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/income" element={<IncomePage />} />{" "}
          {/* Route for income page */}
          <Route path="/expenses" element={<ExpensePage />} />{" "}
          {/* Route for expenses page */}
          <Route path="/budget" element={<BudgetPage />} />{" "}
          {/* Route for budget page */}
        </Routes>
      </Router>
    </FinanceProvider>
  );
};

export default App;
