import os
import shutil
import git
from fastapi import HTTPException
from pathlib import Path

ex = "https://github.com/oDhruvPatel/speercheck"

import os

def git_repository_clone(repo_url: str) -> str:
    repo_name = repo_url.split("/")[-1].replace(".git", "")

    base_dir = os.path.dirname(os.path.abspath(__file__))  # current file folder
    repos_dir = os.path.join(base_dir, "..", "repositories")

    target_path_unresolved = os.path.join(repos_dir, repo_name)
    target_path = os.path.abspath(target_path_unresolved)

    if os.path.exists(target_path):
        shutil.rmtree(target_path)

    try:
        git.Repo.clone_from(repo_url, target_path)
        return target_path
    
    except git.exc.GitCommandError as e:
        raise HTTPException(status_code=400, detail=f"Failed to clone repo: {str(e)}")

git_repository_clone(ex)
