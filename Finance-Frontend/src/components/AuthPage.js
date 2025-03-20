import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import "./AuthPage.css"; // Ensure styles match your design

const AuthPage = () => {
  const [isSignUp, setIsSignUp] = useState(true); // Toggle between Sign Up and Sign In
  const navigate = useNavigate(); // Use navigate hook for routing

  // Toggle between Sign Up and Sign In views
  const toggleAuthMode = () => {
    setIsSignUp((prevMode) => !prevMode);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Assuming successful authentication (no actual auth logic here)
    navigate("/bank-details"); // Redirect to BankDetails page after successful sign-in or sign-up
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <h2>{isSignUp ? "Sign Up" : "Sign In"}</h2>
        <form onSubmit={handleSubmit}> {/* Handle form submission */}
          {isSignUp && (
            <div className="input-group">
              <label>Name</label>
              <input type="text" placeholder="Enter your name" required />
            </div>
          )}
          <div className="input-group">
            <label>Email</label>
            <input type="email" placeholder="Enter your email" required />
          </div>
          <div className="input-group">
            <label>Password</label>
            <input type="password" placeholder="Enter your password" required />
          </div>
          <button type="submit" className="auth-button">
            {isSignUp ? "Sign Up" : "Sign In"}
          </button>
        </form>
        <p className="auth-footer">
          {isSignUp ? "Already have an account?" : "Don't have an account?"}{" "}
          <span onClick={toggleAuthMode}>
            {isSignUp ? "Sign In" : "Sign Up"}
          </span>
        </p>
      </div>
    </div>
  );
};

export default AuthPage;
