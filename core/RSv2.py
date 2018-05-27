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
import RSTools
import re

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

    def updateImage(self,global_rs_image):
        self.global_rs_image = global_rs_image

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


        self.self_window_coord = self.setSelfWindowCoord(self.global_rs_image)
        # Screenshot.save("blah.png",self._calculateGlobalCoord(global_rs_coord,self_window_coord))
        # Mouse.win32MoveToRadius(self_window_coord)
        self.all_items = self._setupAllItems(self.self_window_coord)
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

        return_list = []
        for item in items:
            crop_img = Screenshot.crop(self.global_rs_image, item)
            # cv2.imwrite('%s_exchange.png' % (item), crop_img)
            inventory_item = InventoryItem(crop_img,item,self.global_rs_coord )

            return_list.append(inventory_item)

        return return_list


    def getInventory(self,index_list):
        return_list = []
        for index in index_list:
            return_list.append(self.all_items[index])
        return return_list

    def findItem(self,img_rgb,item_file):
        for item in self.all_items:
            crop = Screenshot.crop(img_rgb,item.getSelfWindowCoord())
        #     cv2.imwrite("asdf.png", crop)
            if Match.this(crop,item_file,0.70):
                return item.getSelfGlobalCoord()

        return False

        # return found_coord

    def screenShotInventory(self,img_rgb):
        num = 0
        for item in self.all_items:
            # Screenshot.showRectangle(img_rgb, value)
            crop_img = Screenshot.crop(img_rgb,item.getSelfWindowCoord())
            cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\temp\%s_item_slot.png'%(num), crop_img)
            num +=1

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

        # print self.global_self_coord

    def clickItem(self):
        # Mouse.win32MoveToRadius(self.global_self_coord)
        # Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord,self.self_window_coord))
        print self._calculateGlobalCoord(self.global_rs_coord, self.self_window_coord)
        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, self.self_window_coord))


    def getSelfGlobalCoord(self):
        return self._calculateGlobalCoord(self.global_rs_coord, self.self_window_coord)

    def getSelfWindowCoord(self):
        return self.self_window_coord


class GrandExchange(RunescapeObject):
    """ runescape GrandExchange class"""
    def __init__(self,global_rs_image,global_rs_coord):
        super(GrandExchange,self).__init__(global_rs_image,global_rs_coord)

        self.WINDOWSIZE = GC.exchange_offer_page_dimensions

        self.self_window_coord = self.setSelfWindowCoord(self.global_rs_image)
        # crop = Screenshot.crop(self.global_rs_image,self.self_window_coord)
        # cv2.imwrite('C:\Users\PPC\git\RS_BOT_2.0\crop.png', crop)

        # print self.self_window_coord
        # self.global_self_coord = self._calculateGlobalCoord(global_rs_coord,self_window_coord )
        # crop = Screenshot.crop(self.global_rs_image, self.global_self_coord)
        # cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\aaaaacrop.png', crop)
        self.all_ge_offers = self._setupAllGEOffers(self.self_window_coord)


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


        return_list = []
        for offer in offers:
            crop_img = Screenshot.crop(self.global_rs_image, offer)
            # cv2.imwrite('%s_exchange.png' % (item), crop_img)
            exchange_offer = ExchangeOffers(crop_img,offer,self.global_rs_coord )
            return_list.append(exchange_offer)

        return return_list

    def setPrice(self,price):

        # found = [self.self_window_coord[0],self.self_window_coord[1],self.self_window_coord[2],self.self_window_coord[3]]
        # found = [374,200,374,200]
        found = [356, 181, 356+GC.offer_button_dimensions[0], 181+GC.offer_button_dimensions[1]]

        found_coord = [self.self_window_coord[0]+found[0],self.self_window_coord[1]+found[1],self.self_window_coord[0]+ found[2],
                       self.self_window_coord[1] + found[3]]

        # crop = Screenshot.crop(self.global_rs_image, found_coord)
        # cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\aaaaacrop.png', crop)

        # found_coord = [found[0]+self.self_window_coord[0], found[1]+self.self_window_coord[1], found[0]+self.self_window_coord[0] + GC.offer_button_dimensions[0],
        #                found[1]+self.self_window_coord[1] + GC.offer_button_dimensions[1]]

        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))

        RandTime.randTime(0, 0, 0, 2, 0, 0)
        Keyboard.type_this(price)
        Keyboard.press("enter")

        # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))


    def setQuantity(self,quantity):

        # found = [217,200,217,200]
        found = [199, 181, 199 + GC.offer_button_dimensions[0], 181 + GC.offer_button_dimensions[1]]

        found_coord = [self.self_window_coord[0]+found[0],self.self_window_coord[1]+found[1],self.self_window_coord[0]+ found[2],
                       self.self_window_coord[1] + found[3]]
        # crop = Screenshot.crop(self.global_rs_image, found_coord)
        # cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\aaaaacrop.png', crop)
        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))

        RandTime.randTime(0, 0, 0, 2, 0, 0)
        Keyboard.type_this(quantity)
        Keyboard.press("enter")

    def increasePrice(self,num_clicks):

        template = GC.offer_increase

        found = Match.this(self.global_rs_image, template)
        # cv2.imwrite("blahblah.png",self.global_rs_image)
        # print found,"found"
        if found:
            found_coord = [found[0], found[1], found[0] + GC.offer_button_dimensions[0],
                           found[1] + GC.offer_button_dimensions[1]]

            for x in range(num_clicks):
                # Mouse.moveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
                RandTime.randTime(0, 0, 0, 0, 0, 1)

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
                RandTime.randTime(0, 0, 0, 0, 0, 1)

    def confirmPrice(self):

        template = GC.offer_confirm

        found = Match.this(self.global_rs_image, template)
        # print found, "found"
        if found:
            found_coord = [found[0], found[1], found[0] + GC.offer_button_dimensions[0],
                           found[1] + GC.offer_button_dimensions[1]]


            Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
            # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))
            # Mouse.win32MoveToRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))

    def getOfferStatus(self):
        # print self.all_ge_offers
        return_list = []
        if GC.MEMBEER_STATUS == False:
            for item in self.all_ge_offers[:3]:
                return_list.append(item.getStatus())
            return return_list
        else:
            for item in self.all_ge_offers:
                return_list.append(item.getStatus())
            return return_list


            # for key,value in dict.iteritems():
            #     print value.getStatus()

    def checkSingleOffer(self):
        self.populateOfferDict()

    def populateOfferDict(self):
        ge_window = Screenshot.crop(self.global_rs_image,self.self_window_coord)
        cv2.imwrite('C:\Users\PPC\git\RS_BOT_2.0\cge_window.png', ge_window)

        item_name = RSTools.readAllText(Screenshot.crop(ge_window, [173,43,330,64]))
        item_name = item_name.replace(" ", "")

        quantity = RSTools.readNumbers(Screenshot.crop(ge_window, [50,158,210,177]))
        if quantity == "":
            quantity = RSTools.readSingleNumbers(Screenshot.crop(ge_window, [50, 158, 210, 177]))
        quantity = int(quantity.replace(",",""))

        rg_price_per_item = re.compile("^(\d+) coins")
        price_per_item = RSTools.readNumbers(Screenshot.crop(ge_window, [276, 160, 429, 177]))
        price_per_item = int(re.search(rg_price_per_item, price_per_item).group(1).replace(",",""))

        # cv2.imwrite('C:\Users\PPC\git\RS_BOT_2.0\citem_name.png', Screenshot.crop(ge_window, [55,160,210,177]))

        rg_bought = re.compile("^.*of(\d+)")
        current_total_bought= RSTools.readNumbers(Screenshot.crop(ge_window, [122,242,330,257]))
        current_total_bought = current_total_bought.replace(" ", "")
        current_total_bought = current_total_bought.replace(",", "")
        return_total_bought= int(re.search(rg_bought,current_total_bought).group(1))

        rg_price = re.compile("^.*of(\d+)coins")
        actual_total_price = RSTools.readNumbers( Screenshot.crop(ge_window, [122, 257, 330, 272]))#.replace(" ", "")
        actual_total_price = actual_total_price.replace(" ", "")
        actual_total_price = actual_total_price.replace(",", "")
        return_total_price = int(re.search(rg_price, actual_total_price).group(1))#.replace("o","0")

        return {'item_name': item_name,
               'total_quantity':quantity,
               'offer_price':price_per_item,
               'bought_quantity': return_total_bought,
               'bought_price': return_total_price
               }

    def clickBack(self):
        # found = [217,200,217,200]
        found = [19, 258,44, 277]

        found_coord = [self.self_window_coord[0] + found[0],
                       self.self_window_coord[1] + found[1],
                       self.self_window_coord[0] + found[2],
                       self.self_window_coord[1] + found[3]]
        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))


        # RandTime.randTime(0, 0, 0, 2, 0, 0)
        # Keyboard.type_this(quantity)
        # Keyboard.press("enter")


        # cv2.imwrite("blahbasdflah.png", actual_total_price)




    def getOffers(self,num):
        return self.all_ge_offers[num]

    def getAllOffers(self):
        if GC.MEMBEER_STATUS == False:
            return self.all_ge_offers[:3]
        return self.all_ge_offers

    def updateImage(self,global_rs_image):
        self.global_rs_image = global_rs_image
        self.all_ge_offers = self._setupAllGEOffers(self.self_window_coord)

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
            # Mouse.win32ClickRadius(self._calculateGlobalCoord(self.global_self_coord, found_coord))
            Mouse.clickRadius(self._calculateGlobalCoord(self.global_self_coord, found_coord))
            # return "we buying"
        # return "can't find"

    def clickOffer(self):

        crop_down = [self.global_self_coord[0]+3,
                     self.global_self_coord[1] +10,
                     self.global_self_coord[2]-7,
                     self.global_self_coord[3] - 20,
        ]

        Mouse.clickRadius(crop_down)



    def getStatus(self):
        return self.status


class Bank(RunescapeObject):
    # def __init__(self, crop_img, coord, rs_window_coord):
    def __init__(self,global_rs_image,global_rs_coord):
        super(Bank, self).__init__(global_rs_image, global_rs_coord)
        pass


class ChatWindow(RunescapeObject):
    # def __init__(self, crop_img, coord, rs_window_coord):
    def __init__(self,global_rs_image,global_rs_coord):
        super(ChatWindow, self).__init__(global_rs_image, global_rs_coord)

        self.WINDOWSIZE = GC.chat_window_dimensions

        self.self_window_coord = self.setSelfWindowCoord(self.global_rs_image)
        # print "self.self_window_coord",self.self_window_coord
        # Screenshot.save("asdfasdfasdf.png",self._calculateGlobalCoord(self.global_rs_coord,self.self_window_coord))
        # crop = Screenshot.crop(self.global_rs_image,self.self_window_coord)
        # cv2.imwrite('C:\Users\PPC\git\RS_BOT_2.0\crop.png', crop)

        # print self.self_window_coord
        # self.global_self_coord = self._calculateGlobalCoord(global_rs_coord,self_window_coord )
        # crop = Screenshot.crop(self.global_rs_image, self.global_self_coord)
        # cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\aaaaacrop.png', crop)
    def setSelfWindowCoord(self,img_rgb):

        # off_set = [-7, -7]
        off_set = [-5, -142]

        # template = GC.chat_buy_anchor
        template = GC.chat_all_anchor


        match = Match.this(img_rgb,template)
        print match

        if match:


            return_coord = [match[0] + off_set[0],
                            match[1] + off_set[1],
                            match[2] + off_set[0] + self.WINDOWSIZE[0],
                            match[3] + off_set[1] + self.WINDOWSIZE[1]
                            ]
            return return_coord
        return None

    def checkStatus(self,img_rgb):
        template = GC.chat_buy_anchor
        cv2.imwrite("basdfadfs.png",img_rgb)
        match = Match.this(img_rgb,template)
        if match:
            return True
        return False

    def clickFoundItem(self,img_rgb,template):
        # print  self.self_window_coord
        # Screenshot.display(img_rgb)
        # Screenshot.display(template)
        print self.self_window_coord
        crop = Screenshot.crop(img_rgb,self.self_window_coord)

        # Screenshot.save("balh.png",self.self_window_coord)
        found = Match.transparent_match(crop,template)

        # print "self.self_window_coord",self.self_window_coord
        #TODO hard coded
        resize_radius = [7,8,0,-4]
        if found:
            found_coord = [found[0]+self.self_window_coord[0]+resize_radius[0],
                           found[1]+self.self_window_coord[1]+resize_radius[1],
                           found[2]+self.self_window_coord[0]+resize_radius[2],
                           found[3]+self.self_window_coord[1]+resize_radius[3]]
            # Screenshot.save("balh.png",self._calculateGlobalCoord(self.global_rs_coord, found_coord))

            # Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))

    #TODO REPLACE
    def clickFoundItemHard(self, img_rgb):
        crop = Screenshot.crop(img_rgb, self.self_window_coord)
        found = [12,35,100,55]
        resize_radius = [0, 0, 0, 0]
        found_coord = [found[0]+self.self_window_coord[0]+resize_radius[0],
                       found[1]+self.self_window_coord[1]+resize_radius[1],
                       found[2]+self.self_window_coord[0]+resize_radius[2],
                       found[3]+self.self_window_coord[1]+resize_radius[3]]
        # Screenshot.save("balh.png", self._calculateGlobalCoord(self.global_rs_coord, found_coord))
        Mouse.clickRadius(self._calculateGlobalCoord(self.global_rs_coord, found_coord))