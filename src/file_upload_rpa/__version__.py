"""Version determination for file-upload-rpa."""

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import re


def _get_version():
    try:
        return version("file-upload-rpa")
    except PackageNotFoundError:
        # Fallback when running from uninstalled source checkout
        pyproject_path = (
            Path(__file__).resolve().parent.parent.parent / "pyproject.toml"
        )
        if pyproject_path.exists():
            content = pyproject_path.read_text(encoding="utf-8")
            match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
        return "0.1.0"


__version__ = _get_version()
