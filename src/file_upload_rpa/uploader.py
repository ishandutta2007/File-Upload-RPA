import os
import sys
import time
from pathlib import Path

import pyautogui
import pygetwindow as gw
from colorama import Fore, Style, init

# Initialize colorama for Windows console support
init(autoreset=True)

# ANSI Styling helper constants & icons
ICON_ROCKET = "🚀"
ICON_GEAR = "⚙️"
ICON_CHECK = "✅"
ICON_WARN = "⚠️"
ICON_WAIT = "⏳"
ICON_STOP = "🛑"
ICON_FILE = "📄"
ICON_KEY = "🔑"
ICON_TERMINAL = "🖥️"

C_CYAN = Fore.CYAN + Style.BRIGHT
C_GREEN = Fore.GREEN + Style.BRIGHT
C_YELLOW = Fore.YELLOW + Style.BRIGHT
C_RED = Fore.RED + Style.BRIGHT
C_MAGENTA = Fore.MAGENTA + Style.BRIGHT
C_BLUE = Fore.BLUE + Style.BRIGHT
C_WHITE = Fore.WHITE + Style.BRIGHT
C_DIM = Style.DIM
RESET = Style.RESET_ALL


def log_info(msg, indent=0):
    prefix = "  " * indent + f"{C_BLUE}[INFO]{RESET} "
    print(f"{prefix}{msg}")


def log_success(msg, indent=0):
    prefix = "  " * indent + f"{C_GREEN}[{ICON_CHECK} SUCCESS]{RESET} "
    print(f"{prefix}{msg}")


def log_warn(msg, indent=0):
    prefix = "  " * indent + f"{C_YELLOW}[{ICON_WARN} WARNING]{RESET} "
    print(f"{prefix}{msg}")


def log_wait(msg, indent=0):
    prefix = "  " * indent + f"{C_MAGENTA}[{ICON_WAIT} WAITING]{RESET} "
    print(f"{prefix}{msg}")


def log_step(step_name, indent=0):
    prefix = "  " * indent + f"{C_WHITE}{Style.BRIGHT}━━━ {step_name} ━━━{RESET}"
    print(f"\n{prefix}")


# --- RESOLVE PACKAGE ASSETS & DEFAULTS ---
PACKAGE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = PACKAGE_DIR / "assets"

DEFAULT_FILE_PATH = os.path.join(os.getcwd(), "assets", "social-preview.gif")


def get_default_buttons():
    """Resolve default button templates, checking cwd first, then bundled package assets."""
    buttons = ["upload_button1.png", "upload_button2.png"]
    resolved = []
    for btn in buttons:
        if os.path.exists(btn):
            resolved.append(btn)
        else:
            bundled = ASSETS_DIR / btn
            if bundled.exists():
                resolved.append(str(bundled))
            else:
                resolved.append(btn)
    return resolved


DEFAULT_BUTTONS = get_default_buttons()


def focus_edge_window():
    """Focus and bring Microsoft Edge to front if running."""
    windows = gw.getWindowsWithTitle("Edge")
    if windows:
        win = windows[0]
        if win.isMinimized:
            win.restore()  # Un-minimize if minimized
        win.activate()  # Bring to front
        log_info("Focused Microsoft Edge window.", indent=2)


def vision_upload_flow(file_path=None, buttons=None, focus_window=True):
    """Executes the vision-based file upload automation flow.

    Args:
        file_path (str, optional): Absolute or relative path to the file to upload.
        buttons (list of str, optional): List of image template paths for buttons to click in sequence.
        focus_window (bool): Whether to un-minimize and focus Microsoft Edge prior to upload.
    """
    if file_path is None:
        file_path = DEFAULT_FILE_PATH
    if buttons is None:
        buttons = get_default_buttons()

    if focus_window:
        focus_edge_window()

    print("Starting vision-based automation...")
    print("Please ensure the browser window is visible on your screen.")
    time.sleep(
        3
    )  # Give yourself 3 seconds to switch focus to the target screen if needed

    # Ensure the upload file exists locally before running
    if not os.path.exists(file_path):
        print(f"Error: Target file not found at {file_path}")
        sys.exit(1)

    # ----------------------------------------------------
    # STEP 1: Find and Click the Upload Button via Vision
    # ----------------------------------------------------
    print("Searching for the upload button on screen...")

    for i, button in enumerate(buttons):
        try:
            btn_location = pyautogui.locateOnScreen(button, confidence=0.8)
            if btn_location is None:
                raise pyautogui.ImageNotFoundException
            print(f"Button found at: {btn_location}")
            btn_center = pyautogui.center(btn_location)
            pyautogui.click(btn_center)
            print(f"Clicked button {i}.{button}.")

        except (pyautogui.ImageNotFoundException, TypeError, FileNotFoundError):
            print(f"Error: Could not find the button {i}.{button} image on the screen.")
            print(
                "Make sure the button is completely visible and looks identical to your template image."
            )
            return
        time.sleep(4)

    # ----------------------------------------------------
    # STEP 2: Interact with the OS File Dialogue Window
    # ----------------------------------------------------
    # Pause to allow the file manager dialog box to open up completely
    time.sleep(4)

    print(f"Typing file path: {file_path}")
    # Type out the absolute file path into the file dialog's active filename input field
    pyautogui.write(file_path, interval=0.01)
    time.sleep(0.5)

    # Press 'enter' to confirm and close the file dialogue box, submitting the file
    print("Pressing Enter to select file...")
    pyautogui.press("enter")
    print("Upload automation flow completed successfully!")
