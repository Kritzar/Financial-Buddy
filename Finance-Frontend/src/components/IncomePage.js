import React, { useState } from 'react';
import { useFinance } from '../context/FinanceContext';

const IncomePage = () => {
  const { addIncome } = useFinance(); // Use the provided addIncome function
  const [amount, setAmount] = useState('');

  const handleSubmit = () => {
    if (amount > 0) {
      addIncome(parseFloat(amount)); // Ensure the amount is a valid number
      setAmount('');
    } else {
      alert("Please enter a valid income amount.");
    }
  };

  return (
    <div>
      <h2>Manage Income</h2>
      <input
        type="number"
        placeholder="Income Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button onClick={handleSubmit}>Add Income</button>
    </div>
  );
};

export default IncomePage;
