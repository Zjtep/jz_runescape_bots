#Match.py
import cv2

import numpy as np
import os
import logging

def this_old(img_pat, img_temp):
    """pass img_pat as a cv2 image format, img_temp as a file
    Passed Function to do w/e after finding img_temp"""
    cwd  = os.getcwd()
    if cwd not in img_temp:
        img_temp = cwd+img_temp
    if '.png' not in img_temp:
        img_temp = cwd+img_temp+'.png'
    #print for DEBUG
    #print(img_temp)
    #img_temp
    img_temp = cv2.imread(img_temp,0)
    #save for DEBUG
    #cv2.imwrite('img_temp', img_temp)
    w, h = img_temp.shape[::-1]
    res = cv2.matchTemplate(img_pat,img_temp,cv2.TM_CCOEFF_NORMED)
    threshold = .8 #default is 8 
    loc = np.where( res >= threshold)
    
    return loc, w, h 

def images_old(img_pat, img_temp,x,y, func):
    w, h = img_temp.shape[::-1]
    try:
        res = cv2.matchTemplate(img_temp,img_pat,cv2.TM_CCOEFF_NORMED)

    except Exception as e:
        print("cannot match")
        print(e)
    threshold = .9 #default is 8 
    loc = np.where( res >= threshold)
    
    for pt in zip(*loc[::-1]):#goes through each found image
        func(img_pat, x, y, pt, w, h)
        return 0
    return 1

    #return loc to be iterable outisde the function
    #also sometimes width and height of image is needed



def old_this(img_rgb,img_file,x,y):
    """pass img_rgb as a cv2 image format, img_file as a file
    Passed Function to do w/e after finding img_file"""
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # img_file = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\gen_item_9.png', 0)
    # print template

    w, h = img_file.shape[::-1]

    res = cv2.matchTemplate(img_gray, img_file, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        pt += (pt[0]+x, pt[1]+y)
        return list(pt)
        # cv2.rectangle(img_rgb, pt, (pt[0] + 1036, pt[1] + 539), (0,255,255), 2)
        # print pt
        # print w,h

    return None



def _this(img_rgb, template):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        point_found = pt
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # return_coord = [pt[0],pt[1],pt[0]+w,pt[1]+h]
    return list(point_found)

    # return return_coord

    # cv2.imwrite('res.png', img_rgb)
    #
    # p1 = Match.this(full_ss, item_file, 5, 5)

#MATCHES 3 CHANNELS
def this(img_rgb, template):
    # img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\17 Mar 2018 11-59-10.png')
    # template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\10_item_slot.png')

    width,height , channels = template.shape

    img_B, img_G, img_R = cv2.split(img_rgb)
    template_B, template_G, template_R = cv2.split(template)
    resB = cv2.matchTemplate(img_B, template_B, cv2.TM_CCOEFF_NORMED)
    resG = cv2.matchTemplate(img_G, template_G, cv2.TM_CCOEFF_NORMED)
    resR = cv2.matchTemplate(img_R, template_R, cv2.TM_CCOEFF_NORMED)

    res = resB + resG + resR
    threshold = 0.90
    loc = np.where(res >= 3 * threshold)
    for pt in zip(*loc[::-1]):
        point_found = pt
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return_coord = [pt[0],pt[1],pt[0]+height,pt[1]+width]
    # return list(point_found)

    return return_coord
    #
    # cv2.imwrite('res.png', img_rgb)
    #
    # p1 = Match.this(full_ss, item_file, 5, 5)