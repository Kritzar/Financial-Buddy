import React, { useState } from 'react';
import { useFinance } from '../context/FinanceContext';

const ExpensePage = () => {
  const { addExpense } = useFinance();
  const [type, setType] = useState('');
  const [amount, setAmount] = useState('');

  const expenseTypes = [
    'Supermarkets',
    'Leisure & Entertainment',
    'Food & Drink',
    'Restaurants',
    'Clothing',
    'General Retail & High Street',
    'Health',
    'Wholesale',
    'Personal Services',
  ];

  const handleSubmit = () => {
    if (type && amount) {
      addExpense(type, parseFloat(amount));
      setType('');
      setAmount('');
    }
  };

  return (
    <div className="container">
      <h2>Add Expense</h2>
      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option value="" disabled>
          Select Expense Type
        </option>
        {expenseTypes.map((category) => (
          <option key={category} value={category}>
            {category}
          </option>
        ))}
      </select>
      <input
        type="number"
        placeholder="Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button onClick={handleSubmit}>Add Expense</button>
    </div>
  );
};


export default ExpensePage;
