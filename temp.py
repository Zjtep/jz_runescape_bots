import win32api
import time
# from core import RS
# from core import RSv2
from corev2 import Environment
import pyautogui
import cv2
from corev2 import Screenshot
from corev2 import Mouse
# from corev2 import Match
from corev2 import RandTime
from corev2 import Keyboard
from corev2 import GameConstants as GC
import random
import os
from corev2 import RSTools
import numpy
import re

def screengrab_as_numpy_array(location):
    im = numpy.array(pyautogui.screenshot(region=(location[0], location[1], location[2]-location[0], location[3] - location[1])))
    return(im)

def check_price(runescape_window):

    off_set = [334,57,-305,-400]
    loc_of_price = (runescape_window.top_left_corner[0] +off_set[0], runescape_window.top_left_corner[1]+off_set[1],
        runescape_window.bottom_right_corner[0] +off_set[2], runescape_window.bottom_right_corner[1]+off_set[3])
    im = Screenshot.this(list(loc_of_price))
    # cv2.imwrite("basdf.png",im)
    raw_string = RSTools.readNumbers(im)
    raw_string = raw_string.replace(",","")
    my_regex = re.compile("^(\d+)")
    price = int(re.search(my_regex, raw_string).group(1))

    return price

    # price = tesser_price_image(screengrab_as_numpy_array((loc_of_price[0], loc_of_price[1], loc_of_price[2], loc_of_price[3])))
    # return(price)


def move_mouse_to_image_within_region(image, region): # region takes in an object
    image_loc = pyautogui.locateOnScreen(image, region=(region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0]-region.top_left_corner[0], region.bottom_right_corner[1]-region.top_left_corner[1]))
    while(image_loc == None):
        image_loc = pyautogui.locateOnScreen(image, region=(region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0]-region.top_left_corner[0], region.bottom_right_corner[1]-region.top_left_corner[1]))
    print image_loc
    Mouse.click_radius(image_loc)

if __name__ == '__main__':
    list_of_items_in_use = []

    list_of_runescape_windows = Environment.detect_runescape_windows()
    for runescape_window in list_of_runescape_windows:
        move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "sale_history_button.png"), runescape_window)
        RSTools.wait_for(os.path.join(GC.anchor_path, "sale_history_check.png"), runescape_window)

        check_price(runescape_window)
        # Screenshot.save("blah.png",[runescape_window.top_left_corner[0]+334,
        #                              runescape_window.top_left_corner[1]+57,
        #                              runescape_window.bottom_right_corner[0]-305,
        #                              runescape_window.bottom_right_corner[1]-400])
