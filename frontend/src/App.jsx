import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')
  const [loading, setLoading] = useState(false)

  const isValidGitHubUrl = (value) => {
    const pattern = /^https?:\/\/(www\.)?github\.com\/[\w.-]+\/[\w.-]+(\/.*)?$/i
    return pattern.test(value.trim())
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setSuccess('')

    if (!url.trim()) {
      setError('Please enter a GitHub repository URL.')
      return
    }

    if (!isValidGitHubUrl(url)) {
      setError('Enter a valid URL like https://github.com/user/repo')
      return
    }

    setLoading(true)

    try {
      const response = await fetch('http://127.0.0.1:8000/api/clone-repository', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ repo_url: url }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }

      setSuccess('Repository submitted successfully!')
      setUrl('')
    } catch (err) {
      console.error(err);
      setError('Something went wrong. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      {/* Background Image */}
      <div className="hero-bg">
        <img src="/hero-bg.png" alt="" aria-hidden="true" />
        <div className="hero-bg__overlay" />
      </div>

      {/* Navigation */}
      <nav className="navbar" id="main-nav">
        <div className="navbar__brand">
          Codebase Documenter
        </div>

        <ul className="navbar__links">
          {/* <li><a href="#home">Home</a></li> */}
        </ul>

        <div className="navbar__socials">
          <button className="navbar__social-btn" aria-label="GitHub">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.385-1.335-1.755-1.335-1.755-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.605-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12z" />
            </svg>
          </button>
          <button className="navbar__social-btn" aria-label="LinkedIn">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
            </svg>
          </button>
          <button className="navbar__social-btn" aria-label="Twitter/X">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
            </svg>
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero" id="hero-section">


        {/* Title */}
        <h1 className="hero__title">Document Your Codebase</h1>

        {/* Subtitle */}
        <p className="hero__subtitle">
          Paste any public GitHub repository URL and generate beautiful,
          comprehensive documentation — instantly powered by AI.
        </p>

        {/* Pill Input */}
        <form onSubmit={handleSubmit} id="repo-form" style={{ width: '100%', maxWidth: '520px' }}>
          <div className={`pill-input ${error ? 'pill-input--error' : ''}`}>
            <input
              id="github-url-input"
              className="pill-input__field"
              type="url"
              placeholder="Enter GitHub Repository URL"
              value={url}
              onChange={(e) => {
                setUrl(e.target.value)
                if (error) setError('')
                if (success) setSuccess('')
              }}
              autoComplete="url"
              spellCheck="false"
              aria-label="GitHub repository URL"
            />
            <button
              id="submit-btn"
              className="pill-input__btn"
              type="submit"
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="pill-input__spinner" />
                  Analyzing
                </>
              ) : (
                'Generate'
              )}
            </button>
          </div>
        </form>

        {/* Error / Success */}
        {error && (
          <div className="hero__message hero__message--error" role="alert" id="error-message">
            {error}
          </div>
        )}
        {success && (
          <div className="hero__message hero__message--success" role="status" id="success-message">
            {success}
          </div>
        )}
      </section>
    </div>
  )
}

export default App
