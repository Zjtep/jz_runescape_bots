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
import Mouse
import RandTime
import Keyboard

import GameConstants as GC

class RunescapeObject(object):
    def __init__(self,global_rs_image,global_rs_coord):
        self.global_rs_image = global_rs_image
        self.global_rs_coord = global_rs_coord
        self.global_self_coord = 0

    def _calculateGlobalCoord(self,global_rs_coord,window_coord):

        x1 = global_rs_coord[0]+ window_coord[0]
        y1= global_rs_coord[1] + window_coord[1]
        x2= global_rs_coord[0] + window_coord[2]
        y2 =global_rs_coord[1] + window_coord[3]
        return [x1,y1,x2,y2]

    def getGlobalRsCoord(self):
        return self.global_rs_coord

"""
full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample.png')
robes = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3_item_slot (3).png')
my_inventory = RSv2.Inventory(full_ss)
"""

class Inventory(RunescapeObject):
    """ runescape inventory class"""
    def __init__(self,global_rs_image,global_rs_coord):
        super(Inventory,self).__init__(global_rs_image,global_rs_coord)

        self.WINDOWSIZE = [98,293]
        self.item_size = [41, 35]

        self_window_coord = self.setSelfWindowCoord(self.global_rs_image)
        # Mouse.win32MoveToRadius(self_window_coord)
        self.all_items = self._setupAllItems(self_window_coord)
        # print self.all_items



    def setSelfWindowCoord(self,img_rgb):

        # off_set = [-7, -7]
        off_set = [-69, 42]

        template = GC.bag_icon

        match = Match.this(img_rgb,template)
        if match:
            # print match,"match"
            return [match[0]+off_set[0],match[1] + off_set[1], match[2] + self.WINDOWSIZE[0],match[3] + self.WINDOWSIZE[1]]
        return None


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
            crop_img = Screenshot.crop(self.global_rs_image, item)
            # cv2.imwrite('%s_exchange.png' % (item), crop_img)
            inventory_item = InventoryItem(crop_img,item,self.global_rs_coord )

            temp_dict = {num: inventory_item}
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

        match = Match.this(full_ss,item_file)
        match_coord = [match[0],match[1],match[2]+self.item_size[0],match[3]++self.item_size[1]]
        # print "crop_img",found_coord
        for item in self.all_items:
            for key, value in item.iteritems():
                print value.getSelfWindowCoord()
                if match_coord ==value.getSelfWindowCoord():
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
                crop_img = Screenshot.crop(img_rgb,value.getSelfWindowCoord())
                cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\temp\%s_item_slot.png'%(key), crop_img)

    def getAllItems(self):
        """
        :return list
             list of inventory dicts
        """
        return self.all_items

    def getInventoryCoord(self):
        pass


class InventoryItem(RunescapeObject):
    """ runescape GrandExchange class"""
    def __init__(self,global_rs_image,window_coord,global_rs_coord):
        super(InventoryItem, self).__init__(global_rs_image, global_rs_coord)

        # self.rs_window_coord = rs_window_coord
        # self.source_image = crop_img
        self.self_window_coord = window_coord
        self.global_self_coord = self._calculateGlobalCoord(global_rs_coord,self.self_window_coord)
        # print self.global_self_coord

    def clickItem(self):
        print self.global_self_coord
        Mouse.win32MoveToRadius(self.global_self_coord)

    def getSelfGlobalCoord(self):
        return self.global_self_coord

    def getSelfWindowCoord(self):
        return self.self_window_coord


class GrandExchange(RunescapeObject):
    """ runescape GrandExchange class"""
    def __init__(self,global_rs_image,global_rs_coord):
        super(GrandExchange,self).__init__(global_rs_image,global_rs_coord)
        print global_rs_coord
        self.WINDOWSIZE = GC.exchange_offer_page_dimensions

        self_window_coord = self.setSelfWindowCoord(self.global_rs_image)
        # crop = Screenshot.crop(self.global_rs_image,self_window_coord)
        # cv2.imwrite('C:\Users\PPC\git\RS_BOT_2.0\crop.png', crop)

        # self.global_self_coord = self._calculateGlobalCoord(global_rs_coord,self_window_coord )
        # crop = Screenshot.crop(self.global_rs_image, self.global_self_coord)
        # cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\aaaaacrop.png', crop)
        self.all_ge_offers = self._setupAllGEOffers(self_window_coord)


        # print history_anchor
        # Screenshot.save("blah",self_window_coord)
        # asdfasdf = self._setGlobalCoord( self.global_rs_coord,history_anchor)
        # Mouse.win32Click(asdfasdf[0],asdfasdf[1])


    def setSelfWindowCoord(self,img_rgb):
        """
        Gets the first item start coordinates
        :arg1 image_file
            screenschot of runescape
        :return list
            top corner's coordinate of inventory
        """

        off_set = [-7, -7]

        template = GC.exchange_history_icon

        match = Match.this(img_rgb,template)
        if match:
            return [match[0]+off_set[0],match[1] + off_set[1], match[2] + off_set[0]+ self.WINDOWSIZE[0],match[3] + off_set[1]+ self.WINDOWSIZE[1]]
        return None

    def _setupAllGEOffers(self,anchor_coord):
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
        self.item_size = [116, 119]


        off_set = [8, 59]

        x1 = anchor_coord[0] +off_set[0]
        y1 = anchor_coord[1] +off_set[1]
        x2 = anchor_coord[0] + self.item_size[0]+off_set[0]
        y2 = anchor_coord[1] + self.item_size[1]+off_set[1]

        offers = []
        for m in range(2):
            for n in range(4):
                offers.append([x1, y1, x2, y2])

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
        for offer in offers:
            crop_img = Screenshot.crop(self.global_rs_image, offer)
            # cv2.imwrite('%s_exchange.png' % (item), crop_img)
            exchange_offer = ExchangeOffers(crop_img,offer,self.global_rs_coord )
            temp_dict = {num:exchange_offer}
            num += 1
            return_list.append(temp_dict)

        return return_list

    def setPrice(self,price):

        found = [374,200,374,200]
        found_coord = [found[0], found[1], found[0] + GC.offer_button_dimensions[0],
                       found[1] + GC.offer_button_dimensions[1]]

        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        RandTime.randTime(0, 0, 0, 2, 0, 0)
        Keyboard.type_this(price)
        Keyboard.press("enter")
        # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))



    def setQuantity(self,quantity):

        found = [217,200,217,200]
        found_coord = [found[0], found[1], found[0] + GC.offer_button_dimensions[0],
                       found[1] + GC.offer_button_dimensions[1]]

        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))

        RandTime.randTime(0, 0, 0, 2, 0, 0)
        Keyboard.type_this(quantity)
        Keyboard.press("enter")

    def increasePrice(self,num_clicks):

        template = GC.offer_increase

        found = Match.this(self.global_rs_image, template)
        # print found,"found"
        if found:
            found_coord = [found[0], found[1], found[0] + GC.offer_button_dimensions[0],
                           found[1] + GC.offer_button_dimensions[1]]

            for x in range(num_clicks):
                # Mouse.moveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                RandTime.randTime(0, 0, 0, 0, 0, 5)

    def decreasePrice(self, num_clicks):

        template = GC.offer_decrease

        found = Match.this(self.global_rs_image, template)
        # print found, "found"
        if found:
            found_coord = [found[0], found[1], found[0] + GC.offer_button_dimensions[0],
                           found[1] + GC.offer_button_dimensions[1]]

            for x in range(num_clicks):
                Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                RandTime.randTime(0, 0, 0, 0, 0, 5)


    def getGEOffers(self):
        return self.all_ge_offers


class ExchangeOffers(RunescapeObject):
    # def __init__(self, crop_img, coord, rs_window_coord):
    def __init__(self,global_rs_image,window_coord,global_rs_coord):
        super(ExchangeOffers, self).__init__(global_rs_image, global_rs_coord)

        # self.rs_window_coord = rs_window_coord
        # self.source_image = crop_img
        self_window_coord = window_coord

        self.global_self_coord = self._calculateGlobalCoord(global_rs_coord,self_window_coord)
        self.status = self.setStatus()

        # print self.global_coord

        # self_window_coord = self.setSelfWindowCoord(self.global_rs_image)
        # self.global_self_coord = self._calculateGlobalCoord(global_rs_coord,self_window_coord )
        # self.all_ge_offers = self._setupAllGEOffers(self_window_coord)


    # def _setGlobalCoord(self,rs_window_coord,full_coord):
    #
    #     x1 = rs_window_coord[0]+ full_coord[0]
    #     y1= rs_window_coord[1] + full_coord[1]
    #     x2= rs_window_coord[0] + full_coord[2]
    #     y2 = rs_window_coord[1] + full_coord[3]
    #     return [x1,y1,x2,y2]

    def setStatus(self):

        template = GC.status_buy_icon
        if Match.this(self.global_rs_image,template):
            return "buy"

        template = GC.status_sell_icon
        if Match.this(self.global_rs_image,template):
            return "sell"

        template = GC.status_empty_icon
        if Match.this(self.global_rs_image, template):
            return "empty"

    def buyItem(self):
        pass

    def clickBuy(self):
        template = GC.status_buy_button

        found = Match.this(self.global_rs_image, template)
        if found:
            found_coord = [found[0],found[1],found[0]+GC.status_buy_button_dimensions[0],found[1]+GC.status_buy_button_dimensions[1]]
            # print found_coord
            # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_self_coord,found_coord))
            Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_self_coord, found_coord))
            # Mouse.win32MoveTo(found_coord[2],found_coord[3])
            # return "we buying"
        # return "can't find"


    def getStatus(self):
        return self.status




class ChatWindow(RunescapeObject):
    # def __init__(self, crop_img, coord, rs_window_coord):
    def __init__(self,global_rs_image,global_rs_coord):
        super(ChatWindow, self).__init__(global_rs_image, global_rs_coord)
        pass


