import React, { useState } from 'react';
import { useFinance } from '../context/FinanceContext';

const BudgetPage = () => {
  const { budget, updateBudget } = useFinance();
  const [amount, setAmount] = useState('');

  const handleUpdateBudget = (type) => {
    updateBudget(type, parseFloat(amount));
    setAmount('');
  };

  return (
    <div>
      <h2>Set Budget</h2>
      <div>
        <button onClick={() => handleUpdateBudget('week')}>Set Weekly Budget</button>
        <button onClick={() => handleUpdateBudget('month')}>Set Monthly Budget</button>
        <button onClick={() => handleUpdateBudget('year')}>Set Yearly Budget</button>
      </div>
      <input
        type="number"
        placeholder="Budget Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <div>
        <h3>Current Budget</h3>
        <p>Weekly: {budget.week}</p>
        <p>Monthly: {budget.month}</p>
        <p>Yearly: {budget.year}</p>
      </div>
    </div>
  );
};

export default BudgetPage;
