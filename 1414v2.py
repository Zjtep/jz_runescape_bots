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
    Screenshot.save("runelite.png",game_coord)
    return game_coord



if __name__ == '__main__':

    global_rs_coord = get_runescape_coord()
    Screenshot.save("dry_run.png",global_rs_coord)

    full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\dry_run.png')















