import cv2
import numpy as np
import subprocess
import pyautogui
import os
import random
import time
import Screenshot

WINDOW_SIZE = (1036, 539)


def getFullPosition():
    """
    Gets Runescape Window ,returns 4 coordinates
    Return List
    """

    # img = Screenshot.shoot(0, 0, 500, 500)
    # img = pyautogui.screenshot(region=(0,0,500,500))  # X1,Y1,X2,Y2
    img = pyautogui.screenshot('temp.png')
    # cv2.imwrite('temp.png', img)


    img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\full_screen_04.jpg')
    # img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\full_window2.JPG')

    # img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\module\temp.png')

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\osbuddy_logo.png', 0)
    # print template

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        pt += (pt[0] + WINDOW_SIZE[0], pt[1] + WINDOW_SIZE[1])
        return list(pt)
        # cv2.rectangle(img_rgb, pt, (pt[0] + 1036, pt[1] + 539), (0,255,255), 2)
        # print pt
        # print w,h

    return [0, 0, 0, 0]


def getGamePosition(win_coord):
    off_set = [8, 36]
    window_size = [513, 337]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getChatPosition(win_coord):
    off_set = [8, 378]
    window_size = [490, 113]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getInventoryPosition(win_coord):
    off_set = [563, 244]
    window_size = [162, 252]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getItemPosition(win_coord):
    item_size = 36
    spacing = 7

    item = []

    x1 = win_coord[0]
    y1 = win_coord[1]
    x2 = win_coord[0]+item_size
    y2 = win_coord[1]+item_size

    for m in range(7):
        for n in range(4):
            # print n

            item.append([x1, y1, x2, y2])

            x1 += item_size
            x2 += item_size
            x1 +=spacing
            x2 +=spacing
        x1 = win_coord[0]
        x2 = win_coord[0]+item_size
        y1 += item_size
        y2 += item_size

    return item
def getMapPosition(win_coord):
    off_set = [573, 41]
    window_size = [144, 151]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getHpPosition(win_coord):
    off_set = [523, 88]
    window_size = [22, 15]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getPrayerPosition(win_coord):
    off_set = [524, 122]
    window_size = [22, 15]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getRunPosition(win_coord):
    off_set = [536, 154]
    window_size = [22, 15]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getSpecPosition(win_coord):
    off_set = [566, 179]
    window_size = [22, 15]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]
    return [start_coord[0], start_coord[1], start_coord[0] + window_size[0], start_coord[1] + window_size[1]]

def getMenuPosition(win_coord):
    off_set = [530, 201]
    item_size = [33,36]

    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]

    item = []
    x1 = start_coord[0]
    y1 = start_coord[1]
    x2 = start_coord[0] + item_size[0]
    y2 = start_coord[1] + item_size[1]

    for m in range(7):
        item.append([x1, y1, x2, y2])

        x1 += item_size[0]
        x2 += item_size[0]


    off_set = [530, 499]
    start_coord = [win_coord[0] + off_set[0], win_coord[1] + off_set[1]]

    x1 = start_coord[0]
    y1 = start_coord[1]
    x2 = start_coord[0] + item_size[0]
    y2 = start_coord[1] + item_size[1]

    for m in range(7):
        item.append([x1, y1, x2, y2])

        x1 += item_size[0]
        x2 += item_size[0]

    print item
    return item

    # x1 = win_coord[0]
    # y1 = win_coord[1]
    # y2 = win_coord[1]+ item_size
    # for x in range(4):
    #
    #     offset_x = item_size + (x*item_size)
    #
    #     x2 = win_coord[0] + offset_x+(x*spacing)
    #     if x > 0:
    #         # x2 = win_coord[0] + offset_x + (x * spacing)
    #         x2 = win_coord[0] + offset_x +(x*spacing)
    #
    #
    #
    #
    #     item.append([x1, y1, x2, y2])
    #     # x1 += offset_x + spacing







img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\full_screen_04.jpg')

pt = getFullPosition()
cv2.rectangle(img_rgb, (pt[0], pt[1]), (pt[2], pt[3]), (0, 255, 100), 3)

pt2 = getGamePosition(pt)
cv2.rectangle(img_rgb, (pt2[0], pt2[1]), (pt2[2], pt2[3]), (0, 255, 100), 1)

pt3 = getChatPosition(pt)
cv2.rectangle(img_rgb, (pt3[0], pt3[1]), (pt3[2], pt3[3]), (0, 255, 100), 1)

pt4 = getChatPosition(pt)
cv2.rectangle(img_rgb, (pt4[0], pt4[1]), (pt4[2], pt4[3]), (0, 255, 100), 1)

pt5 = getInventoryPosition(pt)
# cv2.rectangle(img_rgb, (pt5[0], pt5[1]), (pt5[2], pt5[3]), (0, 255, 100), 1)

temp_list = getItemPosition(pt5)

for temp in temp_list:
    # print temp
    # print temp[0]
    cv2.rectangle(img_rgb, (temp[0], temp[1]), (temp[2], temp[3]), (0, 255, 100), 1)

temp_list2 = getMenuPosition(pt)
for temp2 in temp_list2:
    cv2.rectangle(img_rgb, (temp2[0], temp2[1]), (temp2[2], temp2[3]), (0, 255, 100), 1)

pt5 = getMapPosition(pt)
cv2.rectangle(img_rgb, (pt5[0], pt5[1]), (pt5[2], pt5[3]), (0, 255, 100), 1)

pt6 = getHpPosition(pt)
cv2.rectangle(img_rgb, (pt6[0], pt6[1]), (pt6[2], pt6[3]), (0, 255, 100), 1)

pt7 = getPrayerPosition(pt)
cv2.rectangle(img_rgb, (pt7[0], pt7[1]), (pt7[2], pt7[3]), (0, 255, 100), 1)

pt8 = getRunPosition(pt)
cv2.rectangle(img_rgb, (pt8[0], pt8[1]), (pt8[2], pt8[3]), (0, 255, 100), 1)

pt9 = getSpecPosition(pt)
cv2.rectangle(img_rgb, (pt9[0], pt9[1]), (pt9[2], pt9[3]), (0, 255, 100), 1)


cv2.imwrite('asdf.png', img_rgb)
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img = Screenshot.shoot(0, 0, 500, 500)
# cv2.imwrite('messigray.png', img)


# Local Modules



# menu = Screenshot.shoot(0, 0,500, 500)
# print menu
#
# cv2.imshow("test",menu)
# cv2.waitKey()
# print subprocess.check_output("ls non_existent_file; exit 0",stderr=subprocess.STDOUT,shell=True)


# rs_x, rs_y = position()
#
# print rs_x,rs_y
#


# import psutil
#
# # PROCNAME = "python.exe"
# PROCNAME = "OSBuddy.exe"
#
# for proc in psutil.process_iter():
#     if proc.name() == PROCNAME:
#         print(proc)
