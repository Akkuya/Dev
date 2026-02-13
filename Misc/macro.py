# Source - https://stackoverflow.com/a/33249229
# Posted by Malachi Bazar, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-12, License - CC BY-SA 3.0

import pyautogui
import time

print("Starting in 5 seconds...")
time.sleep(5)  # Time to switch to the target application

print("Running macro...")
for i in range(999):
    pyautogui.press("down")
    pyautogui.press("space")

