import win32api
import time
# from core import RS
from core import RSv2
import pyautogui
import cv2
from core import Screenshot
from core import Mouse
from core import Match




if __name__ == '__main__':



    window_coord = [0,0,33,37]

    window_coord[0] +=123
    window_coord[1] += 15
    window_coord[2] += 122
    window_coord[3] += 14


    # inventory_ss = Screenshot.shoot(window_coord[0], window_coord[1], window_coord[2], window_coord[3],"rgb")
    # cv2.imwrite("asdfsdfsdffsd.png",inventory_ss)



    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample_2.jpg')
    full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\18 Mar 2018 10-26-10.png')

    new_coord = RSv2.getBagAnchor(full_ss)
    print new_coord
    # crop_img = full_ss[window_coord[1]:window_coord[3], window_coord[0]:window_coord[2]]
    # cv2.imwrite('lunar_magic_%s.png', crop_img)

    Screenshot.showRectangle(full_ss, new_coord)
    cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()