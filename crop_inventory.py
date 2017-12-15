import win32api
import time
from core import RS
import pyautogui
import cv2
from core import Screenshot
from core import Mouse
from core import Match


def setMainWindow():
    img = pyautogui.screenshot('ababa.png')
    img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')

    return RS.getFullPosition(img_rgb)

if __name__ == '__main__':
    window_coord = setMainWindow()

    inventory_coord = RS.getPrayerStartPosition(window_coord)
    inventory_coord = RS.getInventoryStartPosition(window_coord)
    inventory_coord = RS.getTopMenuStartPosition(window_coord)
    print inventory_coord
    inventory_ss = Screenshot.shoot(inventory_coord[0], inventory_coord[1], inventory_coord[2], inventory_coord[3],"rgb")
    cv2.imwrite("asdfsdfsdffsd.png",inventory_ss)
    inventory_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\asdfsdfsdffsd.png')
    # temp_list = RS.getAllPrayerPosition([0, 0, 0, 0])
    # temp_list = RS.getInventoryStartPosition([0, 0, 0, 0])
    temp_list = RS.getAllTopMenuPosition([0, 0, 0, 0])
    # print temp_list
    # print len(temp_list),temp_list

    # for temp in temp_list:
    #     print temp
    #     Screenshot.showRectangle(inventory_ss, temp)

    cv2.imshow('Detected', inventory_ss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # temp_list = RS.getAllInventoryPosition([0,0,0,0])



    x= 0
    for temp in temp_list:
        x+=1
        # Screenshot.showRectangle(inventory_ss, temp)
        crop_img = inventory_ss[temp[1]:temp[3], temp[0]:temp[2]]
        cv2.imwrite('top_menu_%s.png'%(x), crop_img)

