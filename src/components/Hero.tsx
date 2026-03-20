import React from 'react';
import './Hero.css';

const Hero: React.FC = () => {
  return (
    <section className="hero">
      <div className="hero-container">
        <div className="badge">
          <span>New · AI Docs for everyone</span>
          <span className="arrow">→</span>
        </div>
        <h1 className="hero-title">
          Clarity for Every<br />Codebase.
        </h1>
        <p className="hero-description">
          Stop struggling with messy, undocumented legacy code. Our AI-powered<br />
          system ensures a smooth understanding process, leaving your<br />
          developers satisfied and boosting your brand's reputation.
        </p>
      </div>
    </section>
  );
};

export default Hero;
