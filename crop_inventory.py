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

    inventory_coord = RS.getInventoryPosition(window_coord)
    # inventory_ss = Screenshot.shoot(inventory_coord[0], inventory_coord[1], inventory_coord[2], inventory_coord[3],"rgb")
    # cv2.imwrite("asdfsdfsdffsd.png",inventory_ss)
    inventory_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\asdfsdfsdffsd.png')

    # cv2.imshow('Detected', inventory_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    temp_list = RS.getItemPosition(window_coord)

    x= 0
    for temp in temp_list:
        x+=1
        # Screenshot.showRectangle(inventory_ss, temp)
        crop_img = inventory_ss[temp[1]:temp[3], temp[0]:temp[2]]
        cv2.imwrite('gen_item_%s.png'%(x), crop_img)

