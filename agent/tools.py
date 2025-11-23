import pathlib
import subprocess
from typing import Tuple
from langchain_core.tools import tool

# Project root where all files must be created/edited
PROJECT_ROOT = pathlib.Path.cwd() / "generated_project"


def safe_path_for_project(path: str) -> pathlib.Path:
    """Ensures a path stays inside PROJECT_ROOT."""
    # Force empty or root path to mean project root
    if path in ["", "/", ".", None]:
        return PROJECT_ROOT

    # If absolute path → convert to relative inside project
    if pathlib.Path(path).is_absolute():
        path = path.lstrip("/")

    p = (PROJECT_ROOT / path).resolve()

    # Final security check
    if PROJECT_ROOT.resolve() not in p.parents and p != PROJECT_ROOT.resolve():
        raise ValueError("Attempt to access outside project root")

    return p


# ------------------------- FILE TOOLS -----------------------------

@tool
def write_file(path: str, content: str) -> str:
    """Writes content to a file inside the project root."""
    p = safe_path_for_project(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"WROTE:{p}"


@tool
def read_file(path: str) -> str:
    """Reads a file inside the project root."""
    p = safe_path_for_project(path)
    return p.read_text(encoding="utf-8") if p.exists() else ""


# LLM compatibility alias (many models call this)
@tool
def open_file(path: str) -> str:
    """Alias for read_file (some LLMs call open_file automatically)."""
    return read_file(path)


# ------------------------- DIRECTORY TOOLS -----------------------------

@tool
def get_current_directory() -> str:
    """Returns the project root directory."""
    return str(PROJECT_ROOT)


@tool
def list_files(directory: str = ".") -> str:
    """Lists files in the given directory inside the project root."""
    p = safe_path_for_project(directory)

    if not p.is_dir():
        return f"ERROR: {p} is not a directory"

    files = [str(f.relative_to(PROJECT_ROOT)) for f in p.glob("**/*") if f.is_file()]
    return "\n".join(files) if files else "No files found."

@tool
def list_file(directory: str = ".") -> str:
    """Alias for list_files. Some models call this instead of list_files."""
    return list_files(directory)


@tool
def search_file(pattern: str = "") -> str:
    """Search for files matching a pattern in the project directory."""
    from fnmatch import fnmatch

    files = list_files(".").split("\n")
    matched = [f for f in files if fnmatch(f, f"*{pattern}*")]
    return "\n".join(matched) if matched else "No files found."

# ------------------------- COMMAND TOOL -----------------------------

@tool
def run_cmd(cmd: str, cwd: str = None, timeout: int = 30) -> Tuple[int, str, str]:
    """Runs a command inside the project root."""
    cwd_dir = safe_path_for_project(cwd) if cwd else PROJECT_ROOT
    res = subprocess.run(
        cmd,
        shell=True,
        cwd=str(cwd_dir),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return res.returncode, res.stdout, res.stderr


def init_project_root():
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    return str(PROJECT_ROOT)
