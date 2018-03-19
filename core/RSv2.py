import cv2
import numpy as np
import subprocess
import pyautogui
import os
import random
import time
import Screenshot

WINDOW_SIZE = (21, 20)

def getBagAnchor(img_rgb):
    """
    Gets Runescape Window ,returns 4 coordinates
    Return List
    """

    # img = Screenshot.shoot(0, 0, 500, 500)
    # img = pyautogui.screenshot(region=(0,0,500,500))  # X1,Y1,X2,Y2
    # img = pyautogui.screenshot('temp.png')
    # cv2.imwrite('temp.png', img)


    # img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\full_screen_04.jpg')
    # img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\full_window2.JPG')

    # img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\module\temp.png')

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\bag_icon.png', 0)
    # print template

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        pt += (pt[0], pt[1])
        return list(pt)
        # cv2.rectangle(img_rgb, pt, (pt[0] + 1036, pt[1] + 539), (0,255,255), 2)
        # print pt
        # print w,h

    return None