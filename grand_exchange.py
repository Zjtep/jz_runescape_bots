import win32api
import time
# from core import RS
from core import RSv2
import pyautogui
import cv2
from core import Environment
from core import Screenshot
from core import Mouse
from core import Match
from core import RandTime
from core import Keyboard


def get_runescape_coord():
    game_window = Environment.RunescapeWindow()

    game_coord= game_window.getCoordinates()
    # print game_coord
    # print game_coord[0]
    # print game_coord[1]
    # game_coord[2] +=game_coord[0]
    # game_coord[3] +=game_coord[1]
    # inventory_ss = Screenshot.this(game_coord[0], game_coord[1], game_coord[2], game_coord[3], "rgb")
    # cv2.imwrite("game_coord.png",inventory_ss)
    # print "done"
    Screenshot.save("runelite.png",game_coord)
    return game_coord


def buy_items_sequences():
    pass


def margin_checker(full_ss):
    template_item = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\4_item_slot (2).png')

    purchased_item = False


    # my_inventory = RSv2.Inventory(full_ss, global_rs_coord)
    # print Mouse.clickRadius( my_inventory.findItem(full_ss,template_item))
    # # print my_inventory.getInventory([4])
    # blah = my_inventory.getAllItems()


    # for b in blah:
    #     b.clickItem()
    # print my_inventory.getAllItems()[0].getSelfWindowCoord()
    # my_inventory.screenShotInventory(full_ss)




    grand_exchange = RSv2.GrandExchange(full_ss,global_rs_coord)
    chat_window = RSv2.ChatWindow(full_ss, global_rs_coord)
    offer_status =  grand_exchange.getOfferStatus()
    for item in grand_exchange.getAllOffers():
        print  item.getStatus()
        # purchased_item = False
        if item.getStatus() == "empty":
            while purchased_item == False:
                item.clickBuy()
                # RandTime.randTime(0, 0, 0, 2, 0, 0)
                RandTime.randomTime(2000,3000)
                if chat_window.checkStatus(Screenshot.this(global_rs_coord)):
                    Keyboard.type_this("air rune")
                    # RandTime.randTime(0, 0, 0, 5, 0, 0)
                    RandTime.randomTime(5000, 6000)
                    # Keyboard.press("enter")
                    chat_window.clickFoundItemHard(Screenshot.this(global_rs_coord))
                    RandTime.randomTime(1000, 2000)
                    # RandTime.randTime(0, 0, 0, 3, 0, 0)

                    grand_exchange.updateImage(Screenshot.this(global_rs_coord))
                    # RandTime.randTime(0, 0, 0, 0,0, 50)
                    RandTime.randomTime(500, 1000)
                    # grand_exchange.increasePrice(1)
                    grand_exchange.increasePrice(5)
                    # grand_exchange.setPrice("1")
                    # grand_exchange.increasePrice(1)
                    # grand_exchange.setQuantity("49")
                    # RandTime.randTime(0, 0, 0, 3, 0, 0)
                    grand_exchange.updateImage(Screenshot.this(global_rs_coord))
                    grand_exchange.confirmPrice()
                    purchased_item = True


def checkAllOffers(full_ss):

    grand_exchange = RSv2.GrandExchange(full_ss, global_rs_coord)
    # print grand_exchange.getOfferStatus()

    grand_exchange.updateImage(Screenshot.this(global_rs_coord))

    for item in grand_exchange.getAllOffers():
        print  item.getStatus()
        if item.getStatus() != "empty":
            item.clickOffer()
            grand_exchange.updateImage(Screenshot.this(global_rs_coord))
            print grand_exchange.populateOfferDict()
            grand_exchange.clickBack()
            grand_exchange.updateImage(Screenshot.this(global_rs_coord))

if __name__ == '__main__':

    global_rs_coord = get_runescape_coord()
    Screenshot.save("dry_run.png",global_rs_coord)

    # window_coord = [2559, -1, 3332, 556]
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\31 Mar 2018 21-02-10.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\1 Apr 2018 02-59-46.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\^8CFE0E4D71CFF4F482815B8070080A76F51667BC75C70EDE0E^pimgpsh_fullsize_distr.png')
    full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\dry_run.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\18 Mar 2018 10-15-35.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\^D54A76B6687EA1725469C2DF27280CBA5A98E15113CA23E5A6^pimgpsh_fullsize_distr.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\23 Apr 2018 00-31-10.png')



    air_rune = ['air rune', r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\4_item_slot (2).png']

    # margin_checker(full_ss)
    checkAllOffers(full_ss)



    # chat_window = RSv2.ChatWindow(full_ss, global_rs_coord)

    # chat_window.clickFoundItem(full_ss,template_item)






    # print my_inventory.getAllItems()
    # print
    # crop = Screenshot.crop(full_ss,my_inventory.getInventory([0])[0].get(0).getSelfCoord())
    # cv2.imwrite(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\temp\%s_item_slot.png' % ("asdf"), crop)
    # print my_inventory.findItem(full_ss,death_rune)

    # for item in items:
    #     for key,value in item.iteritems():
    #         value.clickItem()

            # Mouse.win32MoveToRadius(value)



















    # offer_list = grand_exchange.getGEOffers()
    # for key,value in offer_list[2].iteritems():
    #     value.clickBuy()

    # chat_window = RSv2.ChatWindow(full_ss,global_rs_coord)


    #     print "key: %s , value: %s" % (key, offer_list[key])

    #
    # # blah =  my_exchange.getFullCoord()
    # blah = my_exchange.getAllWindows()
    # print blah
    #
    # for item in blah:
    #     for key,value in item.iteritems():
    #         Screenshot.showRectangle(full_ss, value.getCoord())
    #         # print value.getStatus()
    #         print value.clickBuy()
    # # Screenshot.showRectangle(full_ss, my_inventory.getInventoryCoord())
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # img = pyautogui.screenshot('ababa.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\inventory_sample.png')
    # robes = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\items\3_item_slot (3).png')
    # my_inventory = RSv2.Inventory(full_ss)
    # my_inventory.screenShotInventory(full_ss)
    # print my_inventory.findItem(full_ss,robes)
    # print my_inventory.getAllItems()





    # my_inventory.screenShotInventory(full_ss)


    # my_inventory.screenShotInventory(full_ss)

    # for item in item_position:


    # for item in my_inventory.getInventory([23,27]):
    #     for key,value in item.iteritems():
    #         Screenshot.showRectangle(full_ss, value)
    # # Screenshot.showRectangle(full_ss, my_inventory.getInventoryCoord())
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    # Screenshot.showRectangle(full_ss, item_position)
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # for index, item in enumerate(my_inventory.getFullInventory()):
    #     # if index >= 2 and index<=5:
    #     if index >= 15 and index <= 24:
    #         for key,value in item.iteritems():
    #             Screenshot.showRectangle(full_ss, value)
    # cv2.imshow('Detected', full_ss)
    # cv2.imwrite("jzjz.png", full_ss)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()