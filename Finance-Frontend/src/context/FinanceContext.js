import React, { createContext, useContext, useState } from 'react';

const FinanceContext = createContext();

export const FinanceProvider = ({ children }) => {
  const [income, setIncome] = useState(0); 
  const [expenses, setExpenses] = useState(0);
  const [budget, setBudget] = useState({ week: 0, month: 0, year: 0, total: 0 });

  // Add income to the total income
  const addIncome = (amount) => setIncome((prev) => prev + amount);

  // Add expense to the total expenses
  const addExpense = (amount) => setExpenses((prev) => prev + amount);

  // Update specific budget type (week, month, year) and the total budget
  const updateBudget = (type, amount) => {
    setBudget((prev) => {
      const newAmount = prev[type] + amount; // Add the new amount to the existing value
      const newTotal = prev.week + prev.month + prev.year + newAmount;
      return {
        ...prev,
        [type]: newAmount, // Update the specific type
        total: newTotal,    // Update the total budget
      };
    });
  };

  return (
    <FinanceContext.Provider
      value={{
        income,
        setIncome, // Provide the setter in case you need direct updates
        expenses,
        setExpenses, // Provide the setter for expenses
        budget,
        addIncome,
        addExpense,
        updateBudget,
      }}
    >
      {children}
    </FinanceContext.Provider>
  );
};

export const useFinance = () => {
  const context = useContext(FinanceContext);
  if (!context) {
    throw new Error("useFinance must be used within a FinanceProvider");
  }
  return context;
};
