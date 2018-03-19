from core import RS
from core import Screenshot
from core import Mouse
from core import Keyboard
from core import RandTime
from core import Match
import cv2
import pyautogui
import os

CURRENT_WORKING_DIRECTORY = os.getcwd()
WINDOWS_COORD = 0

def getRunescapeWindow():
    # img = pyautogui.screenshot('ababa.png')
    img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')

    coord = RS.getFullPosition(img_rgb)
    if coord == None:
        print "Can't Find Runescape Window"
        exit()
    return coord

def set_runescape_coord():
    global WINDOWS_COORD
    global GAME_MIDDLE_COORD
    WINDOWS_COORD = getRunescapeWindow()
    game_pos = RS.getGamePosition(WINDOWS_COORD)
    # GAME_MIDDLE_COORD = [game_pos[0]+513/2,game_pos[0]+337/2]
    GAME_MIDDLE_COORD = [game_pos[0]+513/2+20,game_pos[1]+337/2-50]


if __name__ == "__main__":
    set_runescape_coord()