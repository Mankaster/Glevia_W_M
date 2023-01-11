import pyautogui
import pydirectinput as pydirectinput
from ahk import AHK

ahk=AHK()
pyautogui.getWindowsWithTitle("Glevia2")[0].activate()
print("Sprawdzam buffa")
buff = pyautogui.locateCenterOnScreen("buff.png", confidence=0.65)
if not buff:
    ahk.key_press("f1")
    print("SPIERDALAJ")
