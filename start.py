from module import Mouse
from PIL import Image

import pyautogui


if __name__ == '__main__':
    # move_mouse_to_image_within_region("library\items\Capture.JPG","cat")

    # image_loc = pyautogui.locateOnScreen(r"C:\Users\PPC\git\RS_BOT_2.0\library\reference\buy_bag.png", grayscale=True)
    image_loc = pyautogui.locateOnScreen(r"C:\Users\PPC\git\RS_BOT_2.0\library\reference\runescape_menu.png")
    if image_loc:
        Mouse.moveMouseTo(image_loc[0], image_loc[1])
    # print image_loc
    # Mouse.moveMouseTo(850, 800)

    # moveTo(1500,800)
    # Mouse.click()

    # im = pyautogui.screenshot(region=(115, 12, 15, 15))
    # im.save('test.png')
