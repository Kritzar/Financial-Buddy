import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import "./BankDetails.css";

const BankDetails = () => {
  const [bankDetails, setBankDetails] = useState({
    accountHolder: "",
    accountNumber: "",
    ifscCode: "",
    bankName: "",
    branchName: "",
  });

  const navigate = useNavigate(); // Use navigate hook for routing

  const handleChange = (e) => {
    const { name, value } = e.target;
    setBankDetails({ ...bankDetails, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Bank Details Submitted: ", bankDetails);
    // Perform validation and API call here if needed
    navigate("/dashboard"); // Redirect to the Dashboard page
  };

  return (
    <div className="bank-details-container">
      <h1>Bank Verification</h1>
      <form className="bank-details-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Account Holder Name</label>
          <input
            type="text"
            name="accountHolder"
            value={bankDetails.accountHolder}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Account Number</label>
          <input
            type="text"
            name="accountNumber"
            value={bankDetails.accountNumber}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>IFSC Code</label>
          <input
            type="text"
            name="ifscCode"
            value={bankDetails.ifscCode}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Bank Name</label>
          <input
            type="text"
            name="bankName"
            value={bankDetails.bankName}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Branch Name</label>
          <input
            type="text"
            name="branchName"
            value={bankDetails.branchName}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="submit-button">
          Submit
        </button>
      </form>
    </div>
  );
};

export default BankDetails;
