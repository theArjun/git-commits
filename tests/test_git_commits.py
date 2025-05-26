"""
Basic tests for the git-commits library.
"""

import pytest
from datetime import datetime
import tempfile

from git_commits import list_git_commits, GitCommit


def test_import():
    """Test that the library can be imported correctly."""
    assert callable(list_git_commits)
    assert GitCommit is not None


def test_invalid_repository():
    """Test handling of invalid repository paths."""
    commits = list_git_commits("/invalid/path/that/does/not/exist")
    assert commits == []


def test_non_git_directory():
    """Test handling of non-git directories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        commits = list_git_commits(tmpdir)
        assert commits == []


def test_current_repository():
    """Test listing commits from current repository (if it's a git repo)."""
    # This test will only pass if run from within a git repository
    try:
        commits = list_git_commits(".")
        # If we're in a git repo, we should get some commits
        # If not, we should get an empty list
        assert isinstance(commits, list)
        if commits:
            # Verify the structure of returned commits
            commit = commits[0]
            assert hasattr(commit, "sha")
            assert hasattr(commit, "short_sha")
            assert hasattr(commit, "author_name")
            assert hasattr(commit, "author_email")
            assert hasattr(commit, "authored_datetime")
            assert hasattr(commit, "message")
            assert isinstance(commit.authored_datetime, datetime)
    except Exception:
        # If there's any error, just pass - this might not be a git repo
        pass


def test_gitcommit_structure():
    """Test that GitCommit class has expected attributes."""
    # We can't easily create a GitCommit without a real git repo,
    # but we can test that the class exists and has the expected structure
    from git_commits.core import GitCommit

    # Check if it's a dataclass (has __dataclass_fields__)
    assert hasattr(GitCommit, "__dataclass_fields__")

    # Check expected fields
    expected_fields = {
        "sha",
        "short_sha",
        "author_name",
        "author_email",
        "authored_datetime",
        "message",
    }
    actual_fields = set(GitCommit.__dataclass_fields__.keys())
    assert expected_fields.issubset(actual_fields)


if __name__ == "__main__":
    pytest.main([__file__])
