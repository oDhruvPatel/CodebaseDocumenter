import os

ex = "C:\\Users\\dhruv\\OneDrive\\Desktop\\Sites\\codebasedocumentor\\backend\\repositories\\speercheck"
IGNORE_DIR = [
    # Python
    "__pycache__",
    ".venv",
    "venv",
    "env",
    ".env",
    "site-packages",
    "dist",
    "build",
    ".eggs",
    "*.egg-info",

    # Node / React
    "node_modules",
    ".next",
    "dist",
    "build",
    ".cache",

    # Vector DB & AI artifacts
    "chroma_db",
    "vectorstore",
    "embeddings",
    "faiss_index",
    ".chroma",

    # Version control & IDE
    ".git",
    ".github",
    ".vscode",
    ".idea",

    # Misc
    "logs",
    "tmp",
    "temp",
    ".pytest_cache",
    ".mypy_cache",
    "coverage",
    "htmlcoverage",
]

IGNORE_FILES = [
    # Environment & secrets
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
    "*.pem",
    "*.key",

    # Python artifacts
    "*.pyc",
    "*.pyo",
    "*.pyd",

    # Lock files (not useful for docs)
    "package-lock.json",
    "yarn.lock",
    "poetry.lock",
    "pipfile.lock",

    # Data & model files
    "*.pdf",
    "*.csv",
    "*.json",        # remove if your config files are .json
    "*.pkl",
    "*.bin",
    "*.pt",          # PyTorch model weights
    "*.safetensors",

    # Logs
    "*.log",

    # OS files
    ".DS_Store",
    "Thumbs.db",

    # Config/boilerplate
    ".gitignore",
    ".dockerignore",
    "*.md", 
    "Dockerfile",
    "docker-compose.yml",
]
SUPPORTED_FILES = {
    ".py", ".js", ".ts", ".tsx",
    ".java", ".cs", ".json",
    ".html", ".css", ".md"
}
result_files = []
result_structure = []

def parsing_files(repository_path):


    for root, dirs, files in os.walk(repository_path):

        # dir filter
        dirs[:] = [d for d in dirs if d not in IGNORE_DIR]

        folder_structure = {
            "path": root,
            "files": files
        }

        # file loop MUST be inside os.walk
        for file in files:

            if file in IGNORE_FILES:
                continue

            name, ext = os.path.splitext(file)

            if ext not in SUPPORTED_FILES:
                continue
            
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                content = f.read()

            file_data = {
                "path": os.path.join(root, file),
                "file_name": file,
                "file_type": ext,
                "file_content": content,
            }

            result_files.append(file_data)
        result_structure.append(folder_structure)

    return result_files

print(parsing_files(ex))