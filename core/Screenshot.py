#!/usr/bin/python2
import cv2
import numpy as np
import pyautogui


def shoot(x1,y1,x2,y2, *args, **kwargs):
    """Takes screenshot at given coordinates as PIL image format, the converts to cv2 grayscale image format and returns it"""
    # creates widht & height for screenshot region
    w = x2 - x1
    h = y2 - y1
    # PIL format as RGB
    img = pyautogui.screenshot(region=(x1,y1,w,h)) #X1,Y1,X2,Y2
    #im.save('screenshot.png')

    # Converts to an array used for OpenCV
    img = np.array(img)

    try:
        for arg in args:
            if arg == 'hsv':
                # Converts to BGR format for OpenCV
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                return hsv_img

            if arg == 'rgb':
                rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                return rgb_img
    except:
        pass

    cv_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv_gray


def crop(img_rgb,coord):
    return img_rgb[coord[1]:coord[3], coord[0]:coord[2]]
    # return img_rgb[x2:y2, x1:y1]


def this(x1,y1,x2,y2, *args, **kwargs):
    return shoot(x1,y1,x2,y2, *args, **kwargs)

def showRectangle(img,coord_list):
    cv2.rectangle(img, (coord_list[0], coord_list[1]), (coord_list[2], coord_list[3]), (0, 255, 100), 1)

