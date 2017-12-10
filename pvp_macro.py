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


def keyWasUnPressed():
    print "keyWasUnPressed"


def keyWasPressed():
    print "keyWasPressed"


def isKeyPressed(key):
    # "if the high-order bit is 1, the key is down; otherwise, it is up."
    return (win32api.GetKeyState(key) & (1 << 7)) != 0



def setMainWindow():
    img = pyautogui.screenshot('ababa.png')
    img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')

    return RS.getFullPosition(img_rgb)


def mouse_move():
    pass
    temp_list = RS.getItemPosition([0, 0])
    num = 5
    Mouse.moveMouseTo(inventory_coord[0]+temp_list[num][0]+Mouse.randCoord(25), inventory_coord[1]+temp_list[num][1]+Mouse.randCoord(25), 0.5)
    Mouse.click()

    num = 1
    Mouse.moveMouseTo(inventory_coord[0] + temp_list[num][0] + Mouse.randCoord(25),inventory_coord[1] + temp_list[num][1] + Mouse.randCoord(25), 0.5)
    Mouse.click()

    num = 2
    Mouse.moveMouseTo(inventory_coord[0] + temp_list[num][0] + Mouse.randCoord(25),inventory_coord[1] + temp_list[num][1] + Mouse.randCoord(25), 0.5)
    Mouse.click()

def getGearList(dir):
    # dir = r"C:\Users\PPC\git\RS_BOT_2.0\library\items\pvp\range"

    range_gear_list= []
    for f in os.listdir(dir):
        if f.endswith('.png'):
            range_gear_list.append(os.path.join(dir,f))
    return range_gear_list

def item_click(inventory_coord,item_coord,size):
    Mouse.moveMouseTo(inventory_coord[0] + item_coord[0] + Mouse.randCoord(size),inventory_coord[1] + item_coord[1] + Mouse.randCoord(size), 0.5)
    # Mouse.click()

def equipItems(inventory_ss,inventory_coord,item_type):
    gear_list =  getGearList(os.path.join(r"C:\Users\PPC\git\RS_BOT_2.0\library\items\pvp",item_type))
    for item in gear_list:
        img_file = cv2.imread(item, 0)
        p1 = Match.this(inventory_ss, img_file,5,5)
        item_click(inventory_coord,p1,17)
        # print p1

if __name__ == '__main__':
    window_coord = setMainWindow()

    inventory_coord = RS.getInventoryPosition(window_coord)
    inventory_ss = Screenshot.shoot(inventory_coord[0], inventory_coord[1], inventory_coord[2], inventory_coord[3],"rgb")
    # inventory_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\inventory_03.png')



    print equipItems(inventory_ss,inventory_coord,"range")


        # Screenshot.showRectangle(inventory_ss, p1)

    # cv2.imshow('Detected', inventory_ss)
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
