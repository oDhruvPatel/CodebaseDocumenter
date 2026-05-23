# Codebase Documenter

Codebase Documenter is an AI-powered tool that automatically generates comprehensive documentation for any public GitHub repository. By simply pasting a repository URL, the system clones the codebase, analyzes its contents, generates vector embeddings, and produces beautiful, easily navigable documentation.

## 🚀 Features

- **Instant Documentation**: Generate documentation for any public GitHub repository with a single click.
- **AI-Powered Analysis**: Utilizes LLMs (Google Gemini) and LangChain to understand code context and semantics.
- **Vector Search Ready**: Chunks and embeds code using FAISS for efficient similarity search and contextual understanding.
- **Modern UI**: Clean, responsive, and minimalistic frontend built with React and Vite.
- **FastAPI Backend**: High-performance asynchronous backend for handling repository cloning and processing pipelines.

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 19 (via Vite)
- **Styling**: Custom CSS with a modern, minimalist dark-mode aesthetic

### Backend
- **Framework**: FastAPI & Uvicorn
- **AI & NLP**: LangChain, Google Generative AI (Gemini)
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Tools**: GitPython (Repository Cloning), PyPDF2 (Document processing)

## 🏗️ Architecture Pipeline

1. **Clone**: The backend receives a GitHub URL and securely clones the target repository.
2. **Parse**: Scans and extracts content from supported source code files.
3. **Chunk**: Divides the parsed codebase into manageable context chunks optimized for LLMs.
4. **Embed**: Generates vector embeddings for each chunk and stores them in a FAISS vector store.
5. **Generate**: Queries the vector store to extract meaningful context and generates comprehensive documentation.

## ⚙️ Prerequisites

- Node.js (v18+ recommended)
- Python (3.9+ recommended)
- Google Gemini API Key

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone <this-repository-url>
cd CodebaseDocumenter
```

### 2. Backend Setup

```bash
cd backend

# Create a virtual environment
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file in the backend directory and add your keys:
# GOOGLE_API_KEY=your_gemini_api_key_here
```

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```
*The backend API will run on http://127.0.0.1:8000*

### 3. Frontend Setup

Open a new terminal window and navigate to the frontend directory:

```bash
cd frontend

# Install Node dependencies
npm install
```

Start the development server:
```bash
npm run dev
```
*The frontend application will run on http://localhost:5173*

## 💡 Usage

1. Open the frontend application in your browser (`http://localhost:5173`).
2. Paste any public GitHub repository URL (e.g., `https://github.com/user/repo`) into the sleek pill-shaped input field.
3. Click **Generate** and let the AI analyze the codebase.
4. Once completed, the documentation will be successfully generated!

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome! Feel free to check the issues page if you want to contribute.

## 📝 License

This project is licensed under the MIT License.
