import win32api
import time
from core import RS
import pyautogui
import cv2
from core import Screenshot
from core import Mouse
from core import Match
import os

# mouse.moveMouseTo(800,200)

CURRENT_WORKING_DIRECTORY = os.getcwd()


def setMainWindow():
    img = pyautogui.screenshot('ababa.png')
    img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')

    coord = RS.getFullPosition(img_rgb)
    if coord == None:
        print "Can't Find Runescape Window"
        exit()
    return coord


def mouse_move():
    pass
    temp_list = RS.getItemPosition([0, 0])
    num = 5
    Mouse.moveMouseTo(inventory_coord[0] + temp_list[num][0] + Mouse.randCoord(25),
                      inventory_coord[1] + temp_list[num][1] + Mouse.randCoord(25), 0.5)
    Mouse.click()

    num = 1
    Mouse.moveMouseTo(inventory_coord[0] + temp_list[num][0] + Mouse.randCoord(25),
                      inventory_coord[1] + temp_list[num][1] + Mouse.randCoord(25), 0.5)
    Mouse.click()

    num = 2
    Mouse.moveMouseTo(inventory_coord[0] + temp_list[num][0] + Mouse.randCoord(25),
                      inventory_coord[1] + temp_list[num][1] + Mouse.randCoord(25), 0.5)
    Mouse.click()


def getGearList(dir):
    # dir = r"C:\Users\PPC\git\RS_BOT_2.0\library\items\pvp\range"

    range_gear_list = []
    for f in os.listdir(dir):
        if f.endswith('.png'):
            range_gear_list.append(os.path.join(dir, f))
    return range_gear_list


def item_click(inventory_coord, item_coord, size):
    # Mouse.quickMoveMouseTo(inventory_coord[0] + item_coord[0] + Mouse.randCoord(size),
    #                   inventory_coord[1] + item_coord[1] + Mouse.randCoord(size))
    # Mouse.click()
    Mouse.win32Click(inventory_coord[0] + item_coord[0] + Mouse.randCoord(size),inventory_coord[1] + item_coord[1] + Mouse.randCoord(size))


def equipItems(inventory_ss, inventory_coord, item_type):
    gear_path = os.path.join(CURRENT_WORKING_DIRECTORY, r"library\pvp_macro")
    gear_path = os.path.join(gear_path, item_type + "\items")

    print gear_path

    gear_list = getGearList(gear_path)
    for item in gear_list:
        img_file = cv2.imread(item, 0)
        p1 = Match.this(inventory_ss, img_file, 5, 5)
        if p1:
            item_click(inventory_coord, p1, 17)
            # print p1


def activePrayer(inventory_ss, inventory_coord, item_type):
    prayer_path = os.path.join(CURRENT_WORKING_DIRECTORY, r"library\pvp_macro")
    prayer_path = os.path.join(prayer_path, item_type + "\prayer")

    prayer_list = getGearList(prayer_path)

    for item in prayer_list:
        img_file = cv2.imread(item, 0)
        p1 = Match.this(inventory_ss, img_file, 5, 5)
        if p1:
            item_click(inventory_coord, p1, 17)

def changeMenu(inventory_ss, inventory_coord, item_type):
    prayer_path = os.path.join(CURRENT_WORKING_DIRECTORY, r"library\pvp_macro")
    prayer_path = os.path.join(prayer_path, item_type)

    prayer_list = getGearList(prayer_path)


    for item in prayer_list:
        img_file = cv2.imread(item, 0)
        p1 = Match.this(inventory_ss, img_file, 5, 5)
        if p1:
            item_click(inventory_coord, p1, 17)


def equipRangePrayer():
    print "Range Prayer"

def equipMagicPrayer():
    print "Magic Prayer"






HUMAN_KEYPRESS_TIME = 0.3

def press_key(vk_code):
    state = int(win32api.GetKeyState(vk_code))
    if state == -127 or state == -128:
        return 1 # Key was pressed.
    else:
        return 0 # Key was released.

if __name__ == "__main__":

    # p_key = 80
    q_key = 81
    e_key = 69
    w_key = 87
    # r_key = 84

    while True:

        if press_key(q_key):
            print("Q key was pressed.")
            time.sleep(HUMAN_KEYPRESS_TIME)
        if press_key(e_key):
            print("E key was pressed.")
            time.sleep(HUMAN_KEYPRESS_TIME)
        if press_key(w_key):
            print("W key was pressed.")
            time.sleep(HUMAN_KEYPRESS_TIME)







# window_coord = setMainWindow()
    # inventory_coord = RS.getInventoryStartPosition(window_coord)
    # inventory_ss = Screenshot.shoot(inventory_coord[0], inventory_coord[1], inventory_coord[2], inventory_coord[3],
    #                                 "rgb")
    #
    # prayer_coord = RS.getPrayerStartPosition(window_coord)
    # prayer_ss = Screenshot.shoot(prayer_coord[0], prayer_coord[1], prayer_coord[2], prayer_coord[3], "rgb")
    #
    # top_menu_coord = RS.getTopMenuStartPosition(window_coord)
    # top_menu_ss = Screenshot.shoot(top_menu_coord[0], top_menu_coord[1], top_menu_coord[2], top_menu_coord[3], "rgb")
    #
    # # inventory_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\inventory_03.png')
    #
    #
    #
    # equipItems(inventory_ss,inventory_coord,"range")
    # activePrayer(prayer_ss, prayer_coord, "range")
    # changeMenu(top_menu_ss, top_menu_coord, "menu")



    # Screenshot.showRectangle(inventory_ss, p1)

    # cv2.imshow('Detected', prayer_ss)
    # cv2.imwrite('normal_magic.png', inventory_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()








    # for num in range(0,5):



    # Mouse.moveMouseTo(1000, 500, 0.1)

    # crop_img = inventory_ss[temp_list[num][1]:temp_list[num][3], temp_list[num][0]:temp_list[num][2]]
    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

    # Screenshot.showRectangle(iventory_ss, temp_list[1])

    # for temp in temp_list:
    # print temp
    # Screenshot.showRectangle(inventory_ss, temp)
    # iventory_ss = Screenshot.shoot(pt5[0], pt5[1], pt5[2], pt5[3], "rgb")

    # cv2.imshow('Detected', inventory_ss)
    # # cv2.imshow('Detected', crop_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imwrite('aaaaaaaa.png', inventory_ss)
    # cv2.imshow('Detected', img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()




# key = ord('A')
#
# wasKeyPressedTheLastTimeWeChecked = False
# while True:
#     keyIsPressed = isKeyPressed(key)
#     if keyIsPressed and not wasKeyPressedTheLastTimeWeChecked:
#         keyWasPressed()
#     # if not keyIsPressed and wasKeyPressedTheLastTimeWeChecked:
#     #     keyWasUnPressed()
#     wasKeyPressedTheLastTimeWeChecked = keyIsPressed
#     time.sleep(0.01)
