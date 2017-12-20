#Keyboard.py
import pyautogui
import time
import random
import autopy
### My Modules
import  RandTime
import RS

def type_this(strings):
    """Types the passed characters with random pauses in between strokes"""
    for s in strings:
        # delay between key presses--key UP/DOWN
        #autopy.key.toggle(s, True)
        pyautogui.keyDown(s)
        RandTime.randTime(0,0,0,0,0,9)
        pyautogui.keyUp(s)
        # delay after key UP--next key 

def press(button):
    if button == 'enter':
        # autopy.key.toggle(autopy.key.K_RETURN, True)
        pyautogui.keyDown('enter')
        RandTime.randTime(0,0,1,0,0,1)
        # autopy.key.toggle(autopy.key.K_RETURN, False)
        pyautogui.keyUp('enter')
    elif button == 'f5' or button == 'spec':
        pyautogui.keyDown('f5')
        RandTime.randTime(0,0,1,0,0,1)
        pyautogui.keyUp('f5')
    elif button == 'f1' or button == 'inventory':
        pyautogui.keyDown('f1')
        RandTime.randTime(0, 0, 1, 0, 0, 1)
        pyautogui.keyUp('f1')
    elif button == 'f3' or button == 'prayer':
        pyautogui.keyDown('f3')
        RandTime.randTime(0, 0, 1, 0, 0, 1)
        pyautogui.keyUp('f3')
    elif button == 'f4' or button == 'magic':
        pyautogui.keyDown('f4')
        RandTime.randTime(0, 0, 1, 0, 0, 1)
        pyautogui.keyUp('f4')



    # else:
    #     autopy.key.toggle(autopy.key.button, True)

