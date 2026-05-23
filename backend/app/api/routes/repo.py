# app/routes/repo.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.git_service import git_repository_clone
from services.parser_service import parsing_files
from services.chunking import devide_in_chunks
from services.embedding import embeddings
from services.userQuery import generate_docs, load_vector_store
import traceback

router = APIRouter(tags=["Repo"])

class clone_repo_request(BaseModel):
    repo_url: str

@router.post("/clone-repository")
def clone(request: clone_repo_request):
    try:
        # Step 1 — Clone
        print("Cloning repo...")
        path = git_repository_clone(request.repo_url)
        print(f"Cloned to: {path}")

        # Step 2 — Parse files
        print("Parsing files...")
        files = parsing_files(path)
        print(f"Found {len(files)} files")

        if not files:
            raise HTTPException(status_code=400, detail="No supported files found in repo")

        # Step 3 — Chunk
        print("Chunking...")
        chunks = devide_in_chunks(files)
        print(f"Created {len(chunks)} chunks")

        # Step 4 — Embed
        print("Embedding...")
        embeddings(chunks)
        print("Embeddings stored!")

        # Step 5 — Generate docs
        print("Generating docs...")
        db = load_vector_store()
        generate_docs(db)
        print("Docs generated!")

        return {
            "message": "Done!",
            "path": path,
            "total_files": len(files),
            "total_chunks": len(chunks),
            "docs": "output/index.html"
        }

    except Exception as e:
        print("ERROR:", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))