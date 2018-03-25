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


    # window_coord = [0,0,33,37]
    #
    # window_coord[0] +=123
    # window_coord[1] += 15
    # window_coord[2] += 122
    # window_coord[3] += 14

    # inventory_ss = Screenshot.shoot(window_coord[0], window_coord[1], window_coord[2], window_coord[3],"rgb")
    # cv2.imwrite("asdfsdfsdffsd.png",inventory_ss)



    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample_2.jpg')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\18 Mar 2018 10-26-10.png')
    full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample.png')

    robes = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\23_item_slot.png', 0)

    my_inventory = RSv2.Inventory(full_ss)

    print my_inventory.findItem(robes)
    print my_inventory.getAllItems()


    # my_inventory.screenShotInventory(full_ss)

    # for item in item_position:
    for item in my_inventory.getInventory([24,27]):
        for key,value in item.iteritems():
            Screenshot.showRectangle(full_ss, value)
    # Screenshot.showRectangle(full_ss, my_inventory.getInventoryCoord())
    cv2.imshow('Detected', full_ss)
    cv2.imwrite("jzjz.png", full_ss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    # Screenshot.showRectangle(full_ss, item_position)
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # for index, item in enumerate(my_inventory.getFullInventory()):
    #     # if index >= 2 and index<=5:
    #     if index >= 15 and index <= 24:
    #         for key,value in item.iteritems():
    #             Screenshot.showRectangle(full_ss, value)
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()