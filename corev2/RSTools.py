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
from PIL import Image
from PIL import ImageOps
from PIL import ImageGrab
import subprocess
import datetime
import os


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


def custom_locate_all_on_screen(image, **kwargs):

    screenshotIm = _screenshot_win32(region=None) # the locateAll() function must handle cropping to return accurate coordinates, so don't pass a region here.
    retVal = _locateAll_opencv(image, screenshotIm, **kwargs)
    try:
        screenshotIm.fp.close()
    except AttributeError:
        # Screenshots on Windows won't have an fp since they came from
        # ImageGrab, not a file. Screenshots on Linux will have fp set
        # to None since the file has been unlinked
        pass
    return retVal


def _screenshot_win32(imageFilename=None, region=None):
    im = ImageGrab.grab()
    if region is not None:
        assert len(region) == 4, 'region argument must be a tuple of four ints'
        region = [int(x) for x in region]
        im = im.crop((region[0], region[1], region[2] + region[0], region[3] + region[1]))
    if imageFilename is not None:
        im.save(imageFilename)
    return im



def _load_cv2(img, grayscale=None):
    # load images if given filename, or convert as needed to opencv
    # Alpha layer just causes failures at this point, so flatten to RGB.
    # RGBA: load with -1 * cv2.CV_LOAD_IMAGE_COLOR to preserve alpha
    # to matchTemplate, need template and image to be the same wrt having alpha

    if grayscale is None:
        grayscale = False
    if isinstance(img, str):
        # The function imread loads an image from the specified file and
        # returns it. If the image cannot be read (because of missing
        # file, improper permissions, unsupported or invalid format),
        # the function returns an empty matrix
        # http://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html
        if grayscale:
            img_cv = cv2.imread(img)
        else:
            img_cv = cv2.imread(img)
        if img_cv is None:
            raise IOError("Failed to read %s because file is missing, "
                          "has improper permissions, or is an "
                          "unsupported or invalid format" % img)
    elif isinstance(img, numpy.ndarray):
        # don't try to convert an already-gray image to gray
        if grayscale and len(img.shape) == 3:  # and img.shape[2] == 3:
            img_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif hasattr(img, 'convert'):
        # assume its a PIL.Image, convert to cv format
        img_array = numpy.array(img.convert('RGB'))
        img_cv = img_array[:, :, ::-1].copy()  # -1 does RGB -> BGR
        if grayscale:
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    else:
        raise TypeError('expected an image filename, OpenCV numpy array, or PIL image')
    return img_cv




def _locateAll_opencv(needleImage, haystackImage, grayscale=None, limit=10000, region=None, step=1,
                      confidence=0.85):
    """ faster but more memory-intensive than pure python
        step 2 skips every other row and column = ~3x faster but prone to miss;
            to compensate, the algorithm automatically reduces the confidence
            threshold by 5% (which helps but will not avoid all misses).
        limitations:
          - OpenCV 3.x & python 3.x not tested
          - RGBA images are treated as RBG (ignores alpha channel)
    """
    if grayscale is None:
        grayscale = False

    confidence = float(confidence)

    needleImage = _load_cv2(needleImage, grayscale)
    needleHeight, needleWidth = needleImage.shape[:2]
    haystackImage = _load_cv2(haystackImage, grayscale)

    if region:
        haystackImage = haystackImage[region[1]:region[1]+region[3],
                                      region[0]:region[0]+region[2]]
    else:
        region = (0, 0)  # full image; these values used in the yield statement
    if (haystackImage.shape[0] < needleImage.shape[0] or
        haystackImage.shape[1] < needleImage.shape[1]):
        # avoid semi-cryptic OpenCV error below if bad size
        raise ValueError('needle dimension(s) exceed the haystack image or region dimensions')

    if step == 2:
        confidence *= 0.95
        needleImage = needleImage[::step, ::step]
        haystackImage = haystackImage[::step, ::step]
    else:
        step = 1

    # get all matches at once, credit: https://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image/9253805#9253805
    result = cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)
    match_indices = numpy.arange(result.size)[(result > confidence).flatten()]
    matches = numpy.unravel_index(match_indices[:limit], result.shape)


    # use a generator for API consistency:
    matchx = matches[1] * step + region[0]  # vectorized
    matchy = matches[0] * step + region[1]
    for x, y in zip(matchx, matchy):
        yield (x, y, needleWidth, needleHeight)


# if __name__ == '__main__':
#     screen_shot_inventory()
#     print readAllText(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test3\adfafdsafdsafdsafdsfadsfdsa.PNG"))













