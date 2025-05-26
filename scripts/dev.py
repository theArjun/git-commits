#!/usr/bin/env python3
"""
Development script for git-commits package.
Run common development tasks like formatting, testing, and building.
"""

import subprocess
import sys
import argparse
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


def run_command(cmd, description=""):
    """Run a command and handle errors."""
    if description:
        print(f"\n🔄 {description}")

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=PROJECT_ROOT)

    if result.returncode != 0:
        print(f"❌ Command failed with exit code {result.returncode}")
        sys.exit(1)
    else:
        print(f"✅ {description or 'Command completed successfully'}")


def format_code():
    """Format code with black and isort."""
    run_command(
        ["uv", "run", "black", "src/", "tests/", "scripts/"],
        "Formatting code with black",
    )
    run_command(
        ["uv", "run", "isort", "src/", "tests/", "scripts/"],
        "Sorting imports with isort",
    )


def lint_code():
    """Lint code with flake8."""
    run_command(["uv", "run", "flake8", "src/", "tests/"], "Linting code with flake8")


def type_check():
    """Type check with mypy."""
    run_command(["uv", "run", "mypy", "src/"], "Type checking with mypy")


def run_tests():
    """Run tests with pytest."""
    run_command(["uv", "run", "pytest", "tests/", "-v"], "Running tests")


def build_package():
    """Build the package."""
    run_command(["uv", "build"], "Building package")


def clean():
    """Clean build artifacts."""
    import shutil

    paths_to_clean = [
        PROJECT_ROOT / "dist",
        PROJECT_ROOT / "build",
        PROJECT_ROOT / "*.egg-info",
        PROJECT_ROOT / "src" / "git_commits.egg-info",
    ]

    for path in paths_to_clean:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
                print(f"🗑️  Removed directory: {path}")
            else:
                path.unlink()
                print(f"🗑️  Removed file: {path}")

    # Clean __pycache__ directories
    for pycache in PROJECT_ROOT.rglob("__pycache__"):
        shutil.rmtree(pycache)
        print(f"🗑️  Removed: {pycache}")


def check_all():
    """Run all checks (format, lint, type check, test)."""
    format_code()
    lint_code()
    type_check()
    run_tests()
    print("\n🎉 All checks passed!")


def main():
    parser = argparse.ArgumentParser(description="Development script for git-commits")
    parser.add_argument(
        "command",
        choices=["format", "lint", "type-check", "test", "build", "clean", "check-all"],
        help="Command to run",
    )

    args = parser.parse_args()

    if args.command == "format":
        format_code()
    elif args.command == "lint":
        lint_code()
    elif args.command == "type-check":
        type_check()
    elif args.command == "test":
        run_tests()
    elif args.command == "build":
        build_package()
    elif args.command == "clean":
        clean()
    elif args.command == "check-all":
        check_all()


if __name__ == "__main__":
    main()
