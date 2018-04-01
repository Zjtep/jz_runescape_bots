import cv2
import numpy as np
from PIL import Image
import subprocess
import pyautogui
import os
import random
import time
import Screenshot
import Match

import win32gui

"""
full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample.png')
robes = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3_item_slot (3).png')
my_inventory = RSv2.Inventory(full_ss)
"""

class Inventory():
    """ runescape inventory class"""
    def __init__(self,img_rgb):
        self.item_size = [41, 35]
        bag_anchor = self.setBagAnchor(img_rgb)
        self.all_items = self._setupAllItems(bag_anchor)
        self.inventory_coord = self._setupInventoryCoord(bag_anchor)

    def setBagAnchor(self,img_rgb):
        """
        Gets the first item start coordinates
        :arg1 image_file
            screenschot of runescape
        :return list
            top corner's coordinate of inventory
        """

        off_set = [-69, 42]

        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\bag_icon.png', 0)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            pt += (pt[0], pt[1])
            anchor_coord = list(pt)
            return [anchor_coord[0] + off_set[0], anchor_coord[1] + off_set[1], anchor_coord[2] + off_set[0],
                    anchor_coord[3] + off_set[1]]
        return None

    def _setupInventoryCoord(self,anchor_coord):
        x1 = anchor_coord[0]
        y1 = anchor_coord[1]
        x2 = anchor_coord[0] + self.item_size[0]
        y2 = anchor_coord[1] + self.item_size[1]

        return_x = 3+x2+self.item_size[0]*3
        return_y = 6+y2+self.item_size[1]*6

        return [x1, y1, return_x, return_y]

    def _setupAllItems(self,anchor_coord):
        """
        sets up the inventory
        :arg1 image_file
            screenschot of runescape
        :return list[int:{dict}]
            list of inventory dicts with number + coordinate pairing
            eg: [{0: [557, 210, 598, 245]}, {1: [599, 210, 640, 245]}, {2: [641, 210, 682, 245]}]
        """

        # anchor_coord = self.getBagAnchor(img_rgb)
        # item_size = [41, 35]

        x1 = anchor_coord[0]
        y1 = anchor_coord[1]
        x2 = anchor_coord[0] + self.item_size[0]
        y2 = anchor_coord[1] + self.item_size[1]

        items = []
        for m in range(7):
            for n in range(4):
                items.append([x1, y1, x2, y2])

                x1 += self.item_size[0]
                x2 += self.item_size[0]
                x1 += 1
                x2 += 1
            x1 = anchor_coord[0]
            x2 = anchor_coord[0] + self.item_size[0]
            y1 += self.item_size[1]
            y2 += self.item_size[1]
            y1 += 1
            y2 += 1

        num = 0
        return_list = []
        for item in items:
            temp_dict = {num: item}
            num += 1
            return_list.append(temp_dict)

        return return_list

    def getInventory(self,index_list):
        return_list = []
        for index in index_list:
            return_list.append(self.all_items[index])
        return return_list

    def findItem(self,full_ss,item_file):
        # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample.png')

        found_coord = Match.this(full_ss,item_file)
        # print "crop_img",found_coord
        for item in self.all_items:
            for key, value in item.iteritems():
                if found_coord ==value:
                    return key
        return False

        # Screenshot.showRectangle(full_ss, found_coord)
        # cv2.imshow('Detected', full_ss)
        # cv2.imwrite("123.png", Screenshot.crop(full_ss,found_coord))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


        # return found_coord

    def screenShotInventory(self,img_rgb):
        for item in self.all_items:
            for key, value in item.iteritems():
                # Screenshot.showRectangle(img_rgb, value)
                crop_img = Screenshot.crop(img_rgb,value)
                cv2.imwrite('%s_item_slot.png'%(key), crop_img)

    def getAllItems(self):
        """
        :return list
             list of inventory dicts
        """
        return self.all_items

    def getInventoryCoord(self):
        return self.inventory_coord


class GrandExchange():
    """ runescape GrandExchange class"""
    def __init__(self,img_rgb):
        pass
        # self.item_size = [115, 111]
        self.item_size = [116, 118]
        history_anchor = self.setHistoryAnchor(img_rgb)
        self.all_windows = self._setupAllWindows(history_anchor)
        self.full_coord = self._setFullCoord(history_anchor)

    def setHistoryAnchor(self,img_rgb):
        """
        Gets the first item start coordinates
        :arg1 image_file
            screenschot of runescape
        :return list
            top corner's coordinate of inventory
        """

        off_set = [-7, -7]

        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\exchange_history_icon.png', 0)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            pt += (pt[0], pt[1])
            anchor_coord = list(pt)
            return [anchor_coord[0] + off_set[0], anchor_coord[1] + off_set[1], anchor_coord[2] + off_set[0],
                    anchor_coord[3] + off_set[1]]
        return None

    def _setFullCoord(self,anchor_coord):
        x1 = anchor_coord[0]
        y1 = anchor_coord[1]
        x2 = anchor_coord[0]
        y2 = anchor_coord[1]

        return_x = x2+483
        return_y = y2+303

        return [x1, y1, return_x, return_y]

    def _setupAllWindows(self,anchor_coord):
        """
        sets up the inventory
        :arg1 image_file
            screenschot of runescape
        :return list[int:{dict}]
            list of inventory dicts with number + coordinate pairing
            eg: [{0: [557, 210, 598, 245]}, {1: [599, 210, 640, 245]}, {2: [641, 210, 682, 245]}]
        """

        # anchor_coord = self.getBagAnchor(img_rgb)
        # item_size = [41, 35]

        off_set = [8, 59]

        x1 = anchor_coord[0] +off_set[0]
        y1 = anchor_coord[1] +off_set[1]
        x2 = anchor_coord[0] + self.item_size[0]+off_set[0]
        y2 = anchor_coord[1] + self.item_size[1]+off_set[1]

        items = []
        for m in range(2):
            for n in range(4):
                items.append([x1, y1, x2, y2])

                x1 += self.item_size[0]
                x2 += self.item_size[0]
                x1 += 1
                x2 += 1
            x1 = anchor_coord[0]+off_set[0]
            x2 = anchor_coord[0] + self.item_size[0]+off_set[0]
            y1 += self.item_size[1]
            y2 += self.item_size[1]
            y1 += 1
            y2 += 1

        num = 0
        return_list = []
        for item in items:
            exchange_offer = ExchangeOffers(item)
            temp_dict = {num:exchange_offer}
            num += 1
            return_list.append(temp_dict)

        return return_list

    def getFullCoord(self):
        return self.full_coord

    def getAllWindows(self):
        return self.all_windows



class ExchangeOffers():
    def __init__(self,coord):
        self.full_coord = coord
        # pass
    def getCoord(self):
        return self.full_coord



class RunescapeWindow():
    """ Finds Runeloader Game Window"""
    def __init__(self):
        self.game_coord = 0
        self.setCoordinates()

    def setCoordinates(self):
        win32gui.EnumWindows(self._enumHandler, None)

    def _enumHandler(self,hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if 'RuneLoader' in win32gui.GetWindowText(hwnd):
                # win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)
                rect = win32gui.GetWindowRect(hwnd)
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]
                # w = rect[2] - x
                # h = rect[3] - y
                # print "\tLocation: (%d, %d)" % (x, y)
                # print "\t    Size: (%d, %d)" % (w, h)
                self.game_coord = [x, y, w, h]

    def getCoordinates(self):
        return self.game_coord
