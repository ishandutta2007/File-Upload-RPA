import argparse
import sys

from file_upload_rpa.__version__ import __version__
from file_upload_rpa.uploader import (
    DEFAULT_FILE_PATH,
    get_default_buttons,
    vision_upload_flow,
)


def build_parser():
    """Constructs the command-line interface argument parser."""
    parser = argparse.ArgumentParser(
        prog="file-upload-rpa",
        description="Vision-based file upload automation CLI.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "file_path",
        nargs="?",
        default=None,
        help=f"Path to the file to upload (default: {DEFAULT_FILE_PATH})",
    )
    parser.add_argument(
        "buttons",
        nargs="*",
        default=None,
        help="Paths to button template images to click in sequence",
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="file_opt",
        default=None,
        help="Path to the file to upload",
    )
    parser.add_argument(
        "-b",
        "--buttons",
        dest="buttons_opt",
        nargs="+",
        default=None,
        help="Paths to button template images to click in sequence",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def parse_arguments(argv=None):
    """Parses and resolves command line arguments."""
    parser = build_parser()
    args, _ = parser.parse_known_args(argv)

    file_path = args.file_opt or args.file_path or DEFAULT_FILE_PATH
    buttons = (
        args.buttons_opt
        or (args.buttons if args.buttons else None)
        or get_default_buttons()
    )
    return file_path, buttons


def main(argv=None):
    """Entry point for the file-upload-rpa CLI."""
    if argv is None:
        argv = sys.argv[1:]
    try:
        file_path, buttons = parse_arguments(argv)
        vision_upload_flow(file_path=file_path, buttons=buttons, focus_window=True)
        return 0
    except KeyboardInterrupt:
        print("\n[STOP] Automation cancelled by user.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
