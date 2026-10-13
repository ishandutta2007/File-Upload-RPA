"""Backward compatibility runner for file-upload-RPA."""

import sys
from pathlib import Path

# Ensure src/ package is resolvable when executing directly from source tree
SRC_DIR = Path(__file__).resolve().parent / "src"
if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from file_upload_rpa.cli import main, parse_arguments
from file_upload_rpa.uploader import (
    DEFAULT_BUTTONS,
    DEFAULT_FILE_PATH,
    focus_edge_window,
    vision_upload_flow,
)

# Retain backward compatibility variables for scripts inspecting module attributes
FILE_PATH, BUTTON_PATHS = parse_arguments()
BUTTONS = BUTTON_PATHS

__all__ = [
    "BUTTONS",
    "BUTTON_PATHS",
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
