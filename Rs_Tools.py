import win32api
import time
# from core import RS
from core import RSv2
import pyautogui
import cv2
from core import Environment
from core import Screenshot
from core import Mouse
from core import Match
from core import RandTime
from core import Keyboard


def get_runescape_coord():
    game_window = Environment.RunescapeWindow()

    game_coord= game_window.getCoordinates()
    # print game_coord
    # print game_coord[0]
    # print game_coord[1]
    # game_coord[2] +=game_coord[0]
    # game_coord[3] +=game_coord[1]
    # inventory_ss = Screenshot.this(game_coord[0], game_coord[1], game_coord[2], game_coord[3], "rgb")
    # cv2.imwrite("game_coord.png",inventory_ss)
    # print "done"
    Screenshot.save("runelite.png",game_coord)
    return game_coord

def screen_shot_inventory():
    global_rs_coord = get_runescape_coord()
    Screenshot.save("dry_run.png",global_rs_coord)


    full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\dry_run.png')

    my_inventory = RSv2.Inventory(full_ss,global_rs_coord)
    my_inventory.screenShotInventory(full_ss)

# if __name__ == '__main__':
















