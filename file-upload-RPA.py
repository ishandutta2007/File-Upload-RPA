import time
import os
import sys
import pyautogui
import pygetwindow as gw
from colorama import init, Fore, Style

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


# --- CONFIGURE YOUR PATHS ---
# 1. Path to the file you want to upload
FILE_PATH = r"C:\Users\ishan\Documents\Projects\Awesome-Event-Driven-Component-Framework\assets\social-preview.gif"

windows = gw.getWindowsWithTitle("Edge")
if windows:
    win = windows[0]
    if win.isMinimized:
        win.restore()  # Un-minimize if minimized
    win.activate()  # Bring to front
    log_info("Focused Microsoft Edge window.", indent=2)

def vision_upload_flow():
    print("Starting vision-based automation...")
    print("Please ensure the browser window is visible on your screen.")
    time.sleep(3) # Give yourself 3 seconds to switch focus to the target screen if needed

    # Ensure the upload file exists locally before running
    if not os.path.exists(FILE_PATH):
        print(f"Error: Target file not found at {FILE_PATH}")
        sys.exit(1)

    # ----------------------------------------------------
    # STEP 1: Find and Click the Upload Button via Vision
    # ----------------------------------------------------
    print("Searching for the upload button on screen...")

    buttons = ["upload_button1.png", "upload_button2.png"] 

    for i in range(2):
        try:
            btn_location = pyautogui.locateOnScreen(buttons[i], confidence=0.8)
            if btn_location is None:
                raise pyautogui.ImageNotFoundException                
            print(f"Button found at: {btn_location}")
            btn_center = pyautogui.center(btn_location)
            pyautogui.click(btn_center)
            print(f"Clicked button {i}.{buttons[i]}.")

        except (pyautogui.ImageNotFoundException, TypeError):
            print(f"Error: Could not find the button {i}.{buttons[i]} image on the screen.")
            print("Make sure the button is completely visible and looks identical to your template image.")
            return
        time.sleep(4)

    # ----------------------------------------------------
    # STEP 2: Interact with the OS File Dialogue Window
    # ----------------------------------------------------
    # Pause to allow the file manager dialog box to open up completely
    time.sleep(2) 

    print(f"Typing file path: {FILE_PATH}")
    # Type out the absolute file path into the file dialog's active filename input field
    pyautogui.write(FILE_PATH, interval=0.01)
    time.sleep(0.5)

    # Press 'enter' to confirm and close the file dialogue box, submitting the file
    print("Pressing Enter to select file...")
    pyautogui.press('enter')
    print("Upload automation flow completed successfully!")

if __name__ == "__main__":
    vision_upload_flow()
