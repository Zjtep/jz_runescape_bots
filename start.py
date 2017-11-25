from module import Mouse
from PIL import Image

import pyautogui


if __name__ == '__main__':
    # move_mouse_to_image_within_region("library\items\Capture.JPG","cat")

    # image_loc = pyautogui.locateOnScreen("C:\Users\PPC\git\RS_BOT_2.0\library\items\Capture.png", grayscale=True)
    # print image_loc
    Mouse.moveMouseTo(850, 800)

    # moveTo(1500,800)
    # Mouse.click()

    # im = pyautogui.screenshot(region=(115, 12, 15, 15))
    # im.save('test.png')
    # image_loc = pyautogui.locateOnScreen("library\items\gold2.png")
    # print image_loc
    # if image_loc:
    #     Mouse.moveMouseTo(image_loc[0], image_loc[1])