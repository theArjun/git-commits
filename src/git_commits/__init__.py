"""
A Python library for listing Git commits from local repositories.
"""

from .core import list_git_commits, GitCommit

__version__ = "1.0.0"
__all__ = ["list_git_commits", "GitCommit"]
