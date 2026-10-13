"""File Upload RPA - Automated vision-based desktop file upload package."""

from file_upload_rpa.__version__ import __version__
from file_upload_rpa.cli import main
from file_upload_rpa.uploader import (
    DEFAULT_BUTTONS,
    DEFAULT_FILE_PATH,
    focus_edge_window,
    get_default_buttons,
    vision_upload_flow,
)

__all__ = [
    "DEFAULT_BUTTONS",
    "DEFAULT_FILE_PATH",
    "__version__",
    "focus_edge_window",
    "get_default_buttons",
    "main",
    "vision_upload_flow",
]
