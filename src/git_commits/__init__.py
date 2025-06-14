"""
A Python library for listing Git commits from local repositories.
"""

from .core import list_git_commits, get_repo_authors
from .schemas import GitCommit, RepoAuthor

__version__ = "1.0.1"
__all__ = [
    "list_git_commits",
    "get_repo_authors",
    "GitCommit",
    "RepoAuthor",
]
