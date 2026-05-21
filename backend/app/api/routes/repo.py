from fastapi import APIRouter
from services.git_service import git_repository_clone
from pydantic import BaseModel

router = APIRouter(tags=["Repo"])

class clone_repo_request(BaseModel):
    repo_url: str

@router.post("/clone-repository")
def clone(request: clone_repo_request):
    path = git_repository_clone(request.repo_url)
    return {"message": "Repository cloned successfully", "path":path}

