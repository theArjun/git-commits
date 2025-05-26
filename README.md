# Git Commits Library

A Python library for listing Git commits from local repositories with advanced filtering options.

## Features

- 📝 List commits from any local Git repository
- 👤 Filter commits by author (name or email, case-insensitive)
- 📅 Filter commits by date range with flexible date parsing
- 🌍 Timezone support for date filtering
- 🌿 Support for searching across all branches
- 🛡️ Robust error handling
- 📦 Clean dataclass-based return objects

## Installation

Install from PyPI:

```bash
pip install git-commits
```

Or using uv:

```bash
uv add git-commits
```

For development installation:

```bash
git clone https://github.com/yourusername/git-commits.git
cd git-commits
uv install -e .
```

## Quick Start

```python
from git_commits import list_git_commits

# List all commits from current repository
commits = list_git_commits(".")

# Print first few commits
for commit in commits[:3]:
    print(f"{commit.short_sha} - {commit.author_name}: {commit.message}")
```

## API Reference

### `list_git_commits(repo_path, **kwargs)`

List Git commits from a specified local repository with filtering options.

#### Parameters

- **`repo_path`** (str): The absolute or relative path to the local Git repository
- **`author`** (str, optional): Filter commits by author's name or email (case-insensitive partial matching)
- **`since`** (Union[str, datetime], optional): Filter commits authored after this date
- **`until`** (Union[str, datetime], optional): Filter commits authored before this date  
- **`timezone`** (str, optional): Timezone string for interpreting string dates (defaults to "UTC")
- **`all_branches`** (bool, optional): If True, search across all branches (defaults to False)

#### Returns

List of `GitCommit` objects with the following attributes:

- **`sha`** (str): Full SHA-1 hash of the commit
- **`short_sha`** (str): First 7 characters of the SHA-1 hash
- **`author_name`** (str): Name of the commit author
- **`author_email`** (str): Email of the commit author
- **`authored_datetime`** (datetime): Timezone-aware datetime when the commit was authored
- **`message`** (str): Full commit message

## Usage Examples

### Basic Usage

```python
from git_commits import list_git_commits

# List all commits
commits = list_git_commits("/path/to/repo")

# List commits from current directory
commits = list_git_commits(".")
```

### Filter by Author

```python
# Filter by author name (case-insensitive)
commits = list_git_commits(".", author="john")

# Filter by email
commits = list_git_commits(".", author="john@example.com")
```

### Date Filtering

#### Using String Dates

```python
# Commits since a specific date
commits = list_git_commits(".", since="2024-01-01")

# Commits in the last week
commits = list_git_commits(".", since="1 week ago")

# Commits between dates
commits = list_git_commits(
    ".", 
    since="2024-01-01", 
    until="2024-12-31"
)

# Relative dates
commits = list_git_commits(".", since="yesterday")
commits = list_git_commits(".", since="2 months ago")
```

#### Using Datetime Objects

```python
from datetime import datetime
import pytz

# Using timezone-aware datetime objects
eastern = pytz.timezone('America/New_York')
since_dt = eastern.localize(datetime(2024, 1, 1))
until_dt = datetime.now(eastern)

commits = list_git_commits(
    ".", 
    since=since_dt, 
    until=until_dt
)
```

### Timezone Support

```python
# Interpret string dates in a specific timezone
commits = list_git_commits(
    ".",
    since="2024-01-01 09:00:00",
    timezone="America/New_York"
)
```

### Search Across All Branches

```python
# Include commits from all branches (including remote-tracking)
commits = list_git_commits(".", all_branches=True)
```

### Combined Filters

```python
# Combine multiple filters
commits = list_git_commits(
    ".",
    author="john",
    since="1 month ago",
    until="now",
    timezone="UTC",
    all_branches=True
)
```

### Working with Results

```python
commits = list_git_commits(".")

for commit in commits:
    print(f"SHA: {commit.sha}")
    print(f"Short SHA: {commit.short_sha}")
    print(f"Author: {commit.author_name} <{commit.author_email}>")
    print(f"Date: {commit.authored_datetime}")
    print(f"Message: {commit.message}")
    print("-" * 50)
```

## Supported Date Formats

The library supports various date string formats:

- **ISO dates**: `"2024-01-01"`, `"2024-01-01 15:30:00"`
- **Relative dates**: `"yesterday"`, `"today"`, `"now"`
- **Relative periods**: `"1 week ago"`, `"2 months ago"`, `"3 days ago"`
- **Natural language**: Most date strings parseable by `python-dateutil`

## Error Handling

The library gracefully handles various error conditions:

- Invalid repository paths
- Non-Git repositories
- Invalid date strings
- Permission errors

In case of errors, an informative message is printed and an empty list is returned.

```python
# This will print an error message and return []
commits = list_git_commits("/invalid/path")
```

## Requirements

- Python 3.9+
- GitPython >= 3.1.40
- python-dateutil >= 2.8.2
- pytz >= 2024.1

## Development

### Setting up for Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/git-commits.git
cd git-commits
```

2. Install with development dependencies using uv:
```bash
uv install -e ".[dev]"
```

3. Run the examples:
```bash
python main.py
```

4. Run tests (when available):
```bash
pytest
```

5. Format code:
```bash
black src/ tests/
isort src/ tests/
```

6. Type checking:
```bash
mypy src/
```

### Publishing to PyPI

This project is configured to be published using `uv`. Here's how to publish:

1. **Ensure you have the latest version of uv:**
```bash
uv --version  # Should be 0.1.0+
```

2. **Update the version in `pyproject.toml`:**
```toml
[project]
version = "0.1.1"  # Increment as needed
```

3. **Build the package:**
```bash
uv build
```

4. **Publish to PyPI:**
```bash
uv publish
```

5. **Test the installation:**
```bash
uv run --with git-commits --no-project -- python -c "import git_commits"
```

#### Authentication

For publishing, you'll need to set up authentication:

1. **Create API tokens** on PyPI
2. **Configure uv with your credentials:**
```bash
# For PyPI
uv config set credentials.pypi.username __token__
uv config set credentials.pypi.password pypi-your-api-token-here

```

Alternatively, you can use environment variables:
```bash
export UV_PUBLISH_USERNAME="__token__"
export UV_PUBLISH_PASSWORD="pypi-your-api-token-here"
```

## License

MIT License - see [LICENSE](LICENSE) file for details.
