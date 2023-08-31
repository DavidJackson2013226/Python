import mouse
import pyautogui
import time

time.sleep(3)
# add button click
mouse.move(1610, 1018, duration=0.5)
mouse.click()

# read file
for line in open("MyFile.txt", "r"):
    # auto type
    pyautogui.typewrite(line)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("delete")
