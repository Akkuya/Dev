# Source - https://stackoverflow.com/a/33249229
# Posted by Malachi Bazar, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-12, License - CC BY-SA 3.0

import pyautogui
import time

print("Starting in 5 seconds...")
time.sleep(5)  # Time to switch to the target application

print("Running macro...")
for i in range(999):
    pyautogui.keyDown("ctrl")
    pyautogui.press("l")
    time.sleep(0.1)
    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    time.sleep(0.1)
    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(0.1)

    pyautogui.keyUp("alt")
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    time.sleep(0.1)

    pyautogui.keyUp("ctrl")
    pyautogui.press("enter")
    pyautogui.keyDown("ctrl")
    pyautogui.press("t")
    time.sleep(0.1)

    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(0.1)

    pyautogui.keyUp("alt")

    pyautogui.keyDown("ctrl")
    pyautogui.press("tab")
    time.sleep(0.1)

    pyautogui.keyUp("ctrl")
