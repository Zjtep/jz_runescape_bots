from core import RS
from core import Screenshot
from core import Mouse
from core import Keyboard
from core import RandTime
from core import Match
import cv2
import pyautogui
import os
from core import RSv2
#
# def click_bank():
#     #TODO
#     pass
#
# import psutil
#
# if __name__ == "__main__":
#     full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\26 Mar 2018 23-51-50.png')
#     my_inventory = RSv2.Inventory(full_ss)
#
#     item_one_sprite = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\1414\anchovy_pizza\0_item_slot.png')
#     item_two_sprite= cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\1414\anchovy_pizza\11_item_slot.png')
#
#     click_bank()
#
#
#     #INVENTORY PROCESSING
#
#     # print my_inventory.findItem(full_ss,pizza)
#
#
#     cat = "RuneLoader.exe" in (p.name() for p in psutil.process_iter())
#
#     print cat
#     print "5"


# import win32gui
#
# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     # x = rect[0]
#     # y = rect[1]
#     # w = rect[2] - x
#     # h = rect[3] - y
#     # print "Window %s:" % win32gui.GetWindowText(hwnd)
#     # print "\tLocation: (%d, %d)" % (x, y)
#     # print "\t    Size: (%d, %d)" % (w, h)
#
#
# def main():
#     blah = win32gui.EnumWindows(callback, None)
#
#     print blah
# if __name__ == '__main__':
#     main()


# def enumHandler(hwnd, lParam):
#     global WINDOWS_COORD
#     if win32gui.IsWindowVisible(hwnd):
#         if 'RuneLoader' in win32gui.GetWindowText(hwnd):
#             # win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)
#             rect = win32gui.GetWindowRect(hwnd)
#             x = rect[0]
#             y = rect[1]
#             w = rect[2] - x
#             h = rect[3] - y
#             # print "\tLocation: (%d, %d)" % (x, y)
#             # print "\t    Size: (%d, %d)" % (w, h)
#             WINDOWS_COORD = [x,y,w,h]
#
if __name__ == '__main__':
    # win32gui.EnumWindows(enumHandler, None)
    # print WINDOWS_COORD

    game_window = RSv2.RunescapeWindow()

    game_coord= game_window.getCoordinates()
    # print game_coord
    # print game_coord[0]
    # print game_coord[1]
    # game_coord[2] +=game_coord[0]
    # game_coord[3] +=game_coord[1]
    inventory_ss = Screenshot.this(game_coord[0], game_coord[1], game_coord[2], game_coord[3],"rgb")
    cv2.imwrite("game_coord.png",inventory_ss)
    print "done"


# window_coord = [0,0,33,37]
#
# window_coord[0] +=123
# window_coord[1] += 15
# window_coord[2] += 122
# window_coord[3] += 14
#
# inventory_ss = Screenshot.shoot(window_coord[0], window_coord[1], window_coord[2], window_coord[3],"rgb")
# cv2.imwrite("asdfsdfsdffsd.png",inventory_ss)