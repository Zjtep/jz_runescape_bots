import win32api
import time
from core import RS
import pyautogui
import cv2
from core import Screenshot


def keyWasUnPressed():
    print "keyWasUnPressed"


def keyWasPressed():
    print "keyWasPressed"


def isKeyPressed(key):
    # "if the high-order bit is 1, the key is down; otherwise, it is up."
    return (win32api.GetKeyState(key) & (1 << 7)) != 0


def setup_screen():
    img = pyautogui.screenshot('ababa.png')
    img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')

    pt = RS.getFullPosition(img_rgb)
    Screenshot.showRectangle(img_rgb, pt)

    pt5 = RS.getInventoryPosition(pt)

    # temp_list = RS.getItemPosition(pt5)
    # for temp in temp_list:
    #     Screenshot.showRectangle(img_rgb, temp)


    iventory_ss = Screenshot.shoot(pt5[0], pt5[1], pt5[2], pt5[3], "rgb")
    # cv2.rectangle(iventory_ss, (50, 50), (100,200), (255, 255, 100), 1)
    temp_list = RS.getItemPosition([0, 0])

    print temp_list[6]

    # crop_img = iventory_ss[temp_list[0][0]:(temp_list[0][0] + 36), temp_list[0][1]:(temp_list[0][1] + 36)]
    # crop_img = iventory_ss[36:72,43:79]
    num = 2
    crop_img = iventory_ss[temp_list[num][1]:temp_list[num][3], temp_list[num][0]:temp_list[num][2]]
    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

    # Screenshot.showRectangle(iventory_ss, temp_list[1])

    for temp in temp_list:
        print temp
        Screenshot.showRectangle(iventory_ss, temp)
        # iventory_ss = Screenshot.shoot(pt5[0], pt5[1], pt5[2], pt5[3], "rgb")

    # cv2.imshow('Detected', iventory_ss)
    cv2.imshow('Detected', crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.imwrite('asdf.png', img_rgb)
    # cv2.imshow('Detected', img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    setup_screen()


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
