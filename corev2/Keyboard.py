#Keyboard.py
import pyautogui
import time
import random
import autopy
### My Modules
import  RandTime


def type_this(strings):
    """Types the passed characters with random pauses in between strokes"""
    for s in strings:
        # delay between key presses--key UP/DOWN
        #autopy.key.toggle(s, True)
        pyautogui.keyDown(s)
        RandTime.randomTime(2, 7)
        pyautogui.keyUp(s)
        # delay after key UP--next key 



