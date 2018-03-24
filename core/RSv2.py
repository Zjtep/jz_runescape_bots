import cv2
import numpy as np
import subprocess
import pyautogui
import os
import random
import time
import Screenshot

class Inventory():
    def __init__(self,img_rgb):
        self.item_size = [41, 35]
        bag_anchor = self.getBagAnchor(img_rgb)
        self.inventory_list = self.setupInventory(bag_anchor)
        self.inventory_coord = self.setupInventoryCoord(bag_anchor)

    def getBagAnchor(self,img_rgb):
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

    def setupInventoryCoord(self,anchor_coord):
        x1 = anchor_coord[0]
        y1 = anchor_coord[1]
        x2 = anchor_coord[0] + self.item_size[0]
        y2 = anchor_coord[1] + self.item_size[1]

        return_x = 3+x2+self.item_size[0]*3
        return_y = 6+y2+self.item_size[1]*6

        return [x1, y1, return_x, return_y]


    def setupInventory(self,anchor_coord):
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
            return_list.append(self.inventory_list[index])
        return return_list


    def getFullInventory(self):
        """
        :return list
             list of inventory dicts
        """
        return self.inventory_list

    def getInventoryCoord(self):
        return self.inventory_coord


