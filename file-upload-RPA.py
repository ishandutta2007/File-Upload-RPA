"""Backward compatibility runner for file-upload-RPA."""

from pathlib import Path
import sys

# Ensure src/ package is resolvable when executing directly from source tree
SRC_DIR = Path(__file__).resolve().parent / "src"
if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from file_upload_rpa.cli import main, parse_arguments  # noqa: E402
from file_upload_rpa.uploader import (  # noqa: E402
    DEFAULT_BUTTONS,
    DEFAULT_FILE_PATH,
    focus_edge_window,
    vision_upload_flow,
)

# Retain backward compatibility variables for scripts inspecting module attributes
FILE_PATH, BUTTON_PATHS = parse_arguments()
BUTTONS = BUTTON_PATHS

__all__ = [
    "BUTTON_PATHS",
    "BUTTONS",
    "DEFAULT_BUTTONS",
    "DEFAULT_FILE_PATH",
    "FILE_PATH",
    "focus_edge_window",
    "main",
    "parse_arguments",
    "vision_upload_flow",
]

if __name__ == "__main__":
    sys.exit(main())
