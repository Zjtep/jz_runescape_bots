import pyautogui
# from core import RandTime
import RandTime
import random

import time

def click():
    #autopy.mouse.click()
    # pyautogui.moveTo(100, 200)
    pyautogui.mouseDown(button='right')
    RandTime.randTime(0,1,0,0,2,9)#time between click
    pyautogui.mouseUp(button='right')

def moveMouseTo(x,y,speed):
    # if duration:

        # duration_of_move=duration


    while(True):
        try:
            cur_x, cur_y = pyautogui.position()
            distance = int(((x - cur_x)**2 + (y - cur_y)**2)**0.5)
            # calculates a random time to make the move take based on the distance
            # duration_of_move = (distance * random.random() / 2000) + 0.5
            duration_of_move = (distance * random.random() / 2000) + speed
            print duration_of_move
            pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)
            #pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeOutElastic)
            break
        except:
            print('paused for 10 seconds')
            time.sleep(10)