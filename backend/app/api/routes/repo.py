from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.git_service import git_repository_clone
from services.parser_service import parsing_files
from services.chunking import devide_in_chunks
from services.embedding import embeddings

from services.userQuery import (
    generate_docs,
    load_vector_store
)

from services.s3bucket import upload_docs_to_s3

import os
import shutil
import tempfile
import uuid
import traceback

router = APIRouter(tags=["Repo"])

class clone_repo_request(BaseModel):
    repo_url: str

@router.post("/clone-repository")
def clone(request: clone_repo_request):

    job_id = uuid.uuid4().hex

    base_dir = os.path.join(
        tempfile.gettempdir(),
        "codebasedocumentor",
        job_id
    )

    repo_dir = os.path.join(base_dir, "repo")

    chroma_dir = os.path.join(
        base_dir,
        "chroma_db"
    )

    os.makedirs(repo_dir, exist_ok=True)
    os.makedirs(chroma_dir, exist_ok=True)

    try:
        print("Cloning repo...")

        path = git_repository_clone(
            request.repo_url,
            target_dir=repo_dir
        )

        print(f"Cloned to: {path}")

        print("Parsing files...")

        files = parsing_files(path)

        print(f"Found {len(files)} files")

        if not files:
            raise HTTPException(
                status_code=400,
                detail="No supported files found in repo"
            )
        
        print("Chunking...")

        chunks = devide_in_chunks(files)

        print(f"Created {len(chunks)} chunks")

        print("Embedding...")

        embeddings(chunks, chroma_dir)

        print("Embeddings stored!")
        print("Generating docs...")

        db = load_vector_store(chroma_dir)

        result = generate_docs(db)

        if not result:
            raise HTTPException(
                status_code=500,
                detail="Documentation generation failed"
            )

        print("Docs generated!")
        print("Uploading to S3...")

        uploaded_files = upload_docs_to_s3(
            job_id,
            result["files"]
        )

        print("Upload complete!")
        return {
            "message": "Done!",
            "download_links": uploaded_files
        }

    except Exception as e:

        print(
            "ERROR:",
            traceback.format_exc()
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        shutil.rmtree(
            base_dir,
            ignore_errors=True
        )