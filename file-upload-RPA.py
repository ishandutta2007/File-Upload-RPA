import time
import os
import sys
import pyautogui

# --- CONFIGURE YOUR PATHS ---
# 1. Path to the file you want to upload
FILE_PATH = r"C:\path\to\your\file.txt" 
# 2. Image template of the upload button (cropped screenshot)
UPLOAD_BUTTON_TEMPLATE = "upload_btn.png"

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
    try:
        # locateOnScreen searches the visible monitor area for a match. 
        # confidence=0.8 allows slight variations in rendering or anti-aliasing.
        btn_location = pyautogui.locateOnScreen(UPLOAD_BUTTON_TEMPLATE, confidence=0.8)
        
        if btn_location is None:
            raise pyautogui.ImageNotFoundException
            
        print(f"Button found at: {btn_location}")
        # Get the center coordinates of the found image region
        btn_center = pyautogui.center(btn_location)
        
        # Click the button to open the OS file dialog box
        pyautogui.click(btn_center)
        print("Clicked the upload button.")
        
    except (pyautogui.ImageNotFoundException, TypeError):
        print("Error: Could not find the upload button image on the screen.")
        print("Make sure the button is completely visible and looks identical to your template image.")
        return

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
