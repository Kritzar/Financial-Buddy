import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <Link to="/">Dashboard</Link>
      <Link to="/income">Income</Link>
      <Link to="/expenses">Expenses</Link>
      <Link to="/budget">Budget</Link>
    </nav>
  );
};

export default Navbar;
