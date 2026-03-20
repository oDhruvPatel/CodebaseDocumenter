import React from 'react';
import './Navbar.css';

const Navbar: React.FC = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="logo">
          <div className="logo-icon">D</div>
          <span>DocuAI</span>
        </div>
        <div className="nav-links">
          <a href="#login">Login</a>
          <a href="#documents">Documents</a>
          <button className="get-started-btn">
            Get Started <span>→</span>
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
