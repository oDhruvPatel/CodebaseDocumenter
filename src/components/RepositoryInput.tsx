import React from 'react';
import { Github } from 'lucide-react';
import './RepositoryInput.css';
import meadowImg from '../assets/meadow.png';

const RepositoryInput: React.FC = () => {
  return (
    <section className="repo-section">
      <div className="repo-container">
        <div className="meadow-card" style={{ backgroundImage: `url(${meadowImg})` }}>
          <div className="input-overlay">
            <div className="input-group">
              <div className="input-wrapper">
                <Github size={20} className="github-icon" />
                <input 
                  type="text" 
                  placeholder="paste your GitHub repo link here." 
                  className="repo-input"
                />
              </div>
              <button className="analyze-btn">
                Analyze Repository
              </button>
            </div>
            <p className="footer-note">Get your documentation today</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default RepositoryInput;
