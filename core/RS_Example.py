import cv2
import numpy as np
import subprocess
import pyautogui
import os
import random
import time
import Screenshot

import RS

# img = pyautogui.screenshot('temp.png')
img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\full_screen_04.jpg')



pt = RS.getFullPosition(img_rgb)
cv2.rectangle(img_rgb, (pt[0], pt[1]), (pt[2], pt[3]), (0, 255, 100), 3)

pt2 = RS.getGamePosition(pt)
cv2.rectangle(img_rgb, (pt2[0], pt2[1]), (pt2[2], pt2[3]), (0, 255, 100), 1)

pt3 = RS.getChatPosition(pt)
cv2.rectangle(img_rgb, (pt3[0], pt3[1]), (pt3[2], pt3[3]), (0, 255, 100), 1)

pt4 = RS.getChatPosition(pt)
cv2.rectangle(img_rgb, (pt4[0], pt4[1]), (pt4[2], pt4[3]), (0, 255, 100), 1)

pt5 = RS.getInventoryPosition(pt)
# cv2.rectangle(img_rgb, (pt5[0], pt5[1]), (pt5[2], pt5[3]), (0, 255, 100), 1)

temp_list = RS.getItemPosition(pt5)

for temp in temp_list:
    # print temp
    # print temp[0]
    cv2.rectangle(img_rgb, (temp[0], temp[1]), (temp[2], temp[3]), (0, 255, 100), 1)

temp_list2 = RS.getMenuPosition(pt)
for temp2 in temp_list2:
    cv2.rectangle(img_rgb, (temp2[0], temp2[1]), (temp2[2], temp2[3]), (0, 255, 100), 1)

pt5 = RS.getMapPosition(pt)
cv2.rectangle(img_rgb, (pt5[0], pt5[1]), (pt5[2], pt5[3]), (0, 255, 100), 1)

pt6 = RS.getHpPosition(pt)
cv2.rectangle(img_rgb, (pt6[0], pt6[1]), (pt6[2], pt6[3]), (0, 255, 100), 1)

pt7 = RS.getPrayerPosition(pt)
cv2.rectangle(img_rgb, (pt7[0], pt7[1]), (pt7[2], pt7[3]), (0, 255, 100), 1)

pt8 = RS.getRunPosition(pt)
cv2.rectangle(img_rgb, (pt8[0], pt8[1]), (pt8[2], pt8[3]), (0, 255, 100), 1)

pt9 = RS.getSpecPosition(pt)
cv2.rectangle(img_rgb, (pt9[0], pt9[1]), (pt9[2], pt9[3]), (0, 255, 100), 1)


# import Screenshot
# rs_bag = Screenshot.shoot(pt5[0],pt5[1],pt5[2],pt5[3])
# # cv2.imwrite('aaaaaaa.png', rs_bag)
# cv2.imshow('Detected', rs_bag)
# cv2.waitKey(0)

cv2.imwrite('asdf.png', img_rgb)
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

