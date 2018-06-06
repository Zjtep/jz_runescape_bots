import win32api
import time
# from core import RS
# import RSv2
import pyautogui
import cv2
import Environment
import Screenshot
import Mouse
# import Match
import RandTime
import Keyboard
import pytesseract
import numpy

# Page segmentation modes:
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR.
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line,
#                         bypassing hacks that are Tesseract-specific.

def readNumbers(img_rgb):
    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test2\08r.PNG"))
    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test3\water123(3).png"))
    source = numpy.array(img_rgb)
    # NOTE The fucking thing is BLUE,GREEN, RED
    # source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [62, 74, 83]
    source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [52, 64, 73]
    final = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    ret, final = cv2.threshold(final, 80, 255, cv2.THRESH_BINARY)
    # ret, final = cv2.threshold(final, 70, 255, cv2.THRESH_BINARY)
    final = cv2.resize(final, (0, 0), fx=5, fy=5)
    cv2.imwrite("blahblah.png", final)
    text = pytesseract.image_to_string(final, lang="Runescape", boxes=False,
                                       config="--psm 4 --eom 3 -c tessedit_char_whitelist=-01234567890coinseach=,")

    return text

def readSingleNumbers(img_rgb):
    source = numpy.array(img_rgb)
    # NOTE The fucking thing is BLUE,GREEN, RED
    # source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [62, 74, 83]
    source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [52, 64, 73]
    final = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    ret, final = cv2.threshold(final, 80, 255, cv2.THRESH_BINARY)
    # ret, final = cv2.threshold(final, 70, 255, cv2.THRESH_BINARY)
    final = cv2.resize(final, (0, 0), fx=5, fy=5)
    cv2.imwrite("blahblah.png", final)
    text = pytesseract.image_to_string(final, lang="Runescape", boxes=False,
                                       config="--psm 10 --eom 3 -c tessedit_char_whitelist=-01234567890coinseachfar=,")

    return text


def readAllText(img_rgb):
    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test2\08r.PNG"))
    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test3\water123(3).png"))
    source = numpy.array(img_rgb)
    # NOTE The fucking thing is BLUE,GREEN, RED
    # source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [62, 74, 83]
    source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [52, 64, 73]
    final = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    ret, final = cv2.threshold(final, 80, 255, cv2.THRESH_BINARY)
    # ret, final = cv2.threshold(final, 70, 255, cv2.THRESH_BINARY)
    final = cv2.resize(final, (0, 0), fx=5, fy=5)
    cv2.imwrite("blahblah.png", final)
    text = pytesseract.image_to_string(final, lang="Runescape", boxes=False,
                                       config="--psm 4 --eom 3, -c tessedit_char_whitelist= 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=,)(")

    return text

def wait_for(image, runescape_window):
    # adding a possible failsafe in here
    time_entered = time.time()
    # could add a failsafe in here incase we misclick or something, this
    # should be something to come back to
    failsafe_count = 0
    while(True):
        found = pyautogui.locateOnScreen(image, region=(runescape_window.top_left_corner[0], runescape_window.top_left_corner[1], runescape_window.bottom_right_corner[
                                         0] - runescape_window.top_left_corner[0], runescape_window.bottom_right_corner[1] - runescape_window.top_left_corner[1]))
        if found != None:
            break
        elif failsafe_count > 10:
            print("We can't seem to fix the problem so the script is now aborting")
            quit()
        elif time.time()-time_entered > 5 :
            failsafe_count += 1
            print('We appear to be stuck so attempting to move the mouse and see if this fixes it')
            #print('For debug:')
            #print(runescape_window.bottom_right_corner[0], runescape_window.top_left_corner[0])
            #print(runescape_window.bottom_right_corner[1], runescape_window.top_left_corner[1])
            # realmouse.move_mouse_to(random.randint(runescape_window.top_left_corner[0], runescape_window.bottom_right_corner[0]), random.randint(runescape_window.top_left_corner[1], runescape_window.bottom_right_corner[1]))
            #pyautogui.click()
            time_entered = time.time()

def wait_for_w_coord(image, top_left_corner,bottom_right_corner):
    # adding a possible failsafe in here
    time_entered = time.time()
    # could add a failsafe in here incase we misclick or something, this
    # should be something to come back to
    failsafe_count = 0
    while(True):
        found = pyautogui.locateOnScreen(image, region=(top_left_corner[0], top_left_corner[1], bottom_right_corner[
                                         0] - top_left_corner[0], bottom_right_corner[1] - top_left_corner[1]))
        if found != None:
            break
        elif failsafe_count > 10:
            print("We can't seem to fix the problem so the script is now aborting")
            quit()
        elif time.time()-time_entered > 5 :
            failsafe_count += 1
            print('We appear to be stuck so attempting to move the mouse and see if this fixes it')
            #print('For debug:')
            #print(runescape_window.bottom_right_corner[0], runescape_window.top_left_corner[0])
            #print(runescape_window.bottom_right_corner[1], runescape_window.top_left_corner[1])
            # realmouse.move_mouse_to(random.randint(runescape_window.top_left_corner[0], runescape_window.bottom_right_corner[0]), random.randint(runescape_window.top_left_corner[1], runescape_window.bottom_right_corner[1]))
            #pyautogui.click()
            time_entered = time.time()


def read_total_coins(img_rgb):
    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test2\08r.PNG"))
    # source = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test3\water123(3).png"))
    source = numpy.array(img_rgb)
    # NOTE The fucking thing is BLUE,GREEN, RED
    # source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [62, 74, 83]
    source[numpy.where((source == [0, 0, 0]).all(axis=2))] = [52, 64, 73]
    final = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    ret, final = cv2.threshold(final, 80, 255, cv2.THRESH_BINARY)
    # ret, final = cv2.threshold(final, 70, 255, cv2.THRESH_BINARY)
    final = cv2.resize(final, (0, 0), fx=5, fy=5)
    cv2.imwrite("blahblah.png", final)
    text = pytesseract.image_to_string(final, lang="Runescape", boxes=False,
                                       config="--psm 4 --eom 3 -c tessedit_char_whitelist=-01234567890Coinsx,.")

    return text


# if __name__ == '__main__':
#     screen_shot_inventory()
#     print readAllText(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test3\adfafdsafdsafdsafdsfadsfdsa.PNG"))















