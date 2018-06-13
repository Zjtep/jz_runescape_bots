import win32api
import time

import pyautogui
import cv2
import random
import os
import numpy
import re
import pickle

from corev2 import Screenshot
from corev2 import Mouse
# from corev2 import Match
from corev2 import RandTime
from corev2 import Keyboard
from corev2 import GameConstants as GC
from corev2 import RSTools
from corev2 import Environment
from corev2 import items_to_merch_module


class runescape_instance():
    def __init__(self, position):
        off_set = [8, 0, 769, 499]
        Screenshot.save("blahblah.png",
                        [position[0] + off_set[0], position[1], position[0] + off_set[2], position[1] + off_set[3]])
        self.top_left_corner = (position[0] + off_set[0], position[1])
        self.bottom_right_corner = (position[0] + off_set[2], position[1] + off_set[3])
        self.last_action_time = time.time()


def detect_runescape_windows():  # this function will detect how many runescape windows are present and where they are
    list_of_runescape_windows = []
    # for i in pyautogui.locateAllOnScreen('Tools/screenshots/collect_all_buttons.png'):
    for i in pyautogui.locateAllOnScreen(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\Rune_Lite.png'):
        list_of_runescape_windows.append(
            runescape_instance((i[0], i[1] + i[3])))
    return (list_of_runescape_windows)


def setup_runescape_screen(runescape_window):

    coords_of_compass = (
        runescape_window.top_left_corner[0] + 550, runescape_window.top_left_corner[1] + 14, 20, 15)

    # Screenshot.save("blahblah.png", [coords_of_compass[0],coords_of_compass[1],coords_of_compass[0]+coords_of_compass[2],coords_of_compass[1]+coords_of_compass[3]])

    hm.move_radius(coords_of_compass)
    # hm.move_radius((953,784,20,20))
    Mouse.click()
    Keyboard.hold_key("down")

    # printrandom.randint(100,200)
    # Mouse.scroll(-100)
    # Mouse.scroll(100)

# hm.move_radius()

def set_up_humidify_clay(runescape_window):

    Keyboard.press("exit")
    RSTools.wait_for(os.path.join(GC.global_anchor, "astra_runes.png"), runescape_window)
    RandTime.randomTime(100, 200)

    Keyboard.press("equipment")
    RSTools.wait_for(os.path.join(GC.global_anchor, "smoke_staff.png"), runescape_window)
    RandTime.randomTime(100, 200)


    RSTools.wait_for(os.path.join(GC.global_anchor, "lunar_magic.png"), runescape_window)
    lunar_magic_tab = pyautogui.locateOnScreen(os.path.join(GC.global_anchor, "lunar_magic.png"), region=(
        runescape_window.top_left_corner[0], runescape_window.top_left_corner[1],
        runescape_window.bottom_right_corner[0] - runescape_window.top_left_corner[0],
        runescape_window.bottom_right_corner[1] - runescape_window.top_left_corner[1]))

    hm.move_radius(lunar_magic_tab)
    Mouse.click()

    RSTools.wait_for(os.path.join(GC.global_anchor, "humidify.png"), runescape_window)
    RandTime.randomTime(100,200)

def set_up_bank_tab(runescape_window):
    wait_for_bank(os.path.join(GC.global_anchor, "bank_chest2.png"), runescape_window)
    bank_location = RSTools.custom_locate_on_screen(os.path.join(GC.global_anchor, "bank_chest2.png"), region=(
        runescape_window.top_left_corner[0], runescape_window.top_left_corner[1],
        runescape_window.bottom_right_corner[0] - runescape_window.top_left_corner[0],
        runescape_window.bottom_right_corner[1] - runescape_window.top_left_corner[1]))

    hm.move_radius(bank_location)
    Mouse.click()
    RSTools.wait_for(os.path.join(GC.global_anchor, "bank_interface.png"), runescape_window)
    coords_of_tab = (
        runescape_window.top_left_corner[0] + 425, runescape_window.top_left_corner[1] + 45, 20, 15)
    hm.move_radius(coords_of_tab)
    Mouse.click()
    RandTime.randomTime(100, 200)
    Keyboard.press("exit")


def wait_for_bank(image, runescape_window):
    # adding a possible failsafe in here
    time_entered = time.time()
    # could add a failsafe in here incase we misclick or something, this
    # should be something to come back to
    failsafe_count = 0
    while(True):
        found = RSTools.custom_locate_on_screen(image, region=(runescape_window.top_left_corner[0], runescape_window.top_left_corner[1], runescape_window.bottom_right_corner[
                                         0] - runescape_window.top_left_corner[0], runescape_window.bottom_right_corner[1] - runescape_window.top_left_corner[1]))
        if found != None:
            break
        elif failsafe_count > 3:
            print("We can't seem to fix the problem so the script is now aborting")
            quit()
        elif time.time()-time_entered > 5:
            failsafe_count += 1
            print('We appear to be stuck finding the bank booth')
            setup_runescape_screen(runescape_window)
            time_entered = time.time()

def play_with_tabs():
    pass


if __name__ == '__main__':

    hm = Mouse.HumanMouse()


    list_of_runescape_windows = detect_runescape_windows()
    for runescape_window in list_of_runescape_windows:
        setup_runescape_screen(runescape_window)
        set_up_humidify_clay(runescape_window)
        set_up_bank_tab(runescape_window)

    for runescape_window in list_of_runescape_windows:
        pass


        # knife_coord = pyautogui.locateOnScreen(os.path.join(GC.global_anchor, "knife.png"), region=(
        #     runescape_window.top_left_corner[0], runescape_window.top_left_corner[1],
        #     runescape_window.bottom_right_corner[0] - runescape_window.top_left_corner[0],
        #     runescape_window.bottom_right_corner[1] - runescape_window.top_left_corner[1]))
        #
        # log_coord = pyautogui.locateOnScreen(os.path.join(GC.global_anchor, "maple_log.png"), region=(
        #     runescape_window.top_left_corner[0], runescape_window.top_left_corner[1],
        #     runescape_window.bottom_right_corner[0] - runescape_window.top_left_corner[0],
        #     runescape_window.bottom_right_corner[1] - runescape_window.top_left_corner[1]))
        #
        #
        # print knife_coord
        # print log_coord