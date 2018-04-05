import win32api
import time
# from core import RS
from core import RSv2
import pyautogui
import cv2
from core import Screenshot
from core import Mouse
from core import Match



def get_runescape_coord():
    game_window = RSv2.RunescapeWindow()

    game_coord= game_window.getCoordinates()
    # print game_coord
    # print game_coord[0]
    # print game_coord[1]
    # game_coord[2] +=game_coord[0]
    # game_coord[3] +=game_coord[1]
    # inventory_ss = Screenshot.this(game_coord[0], game_coord[1], game_coord[2], game_coord[3], "rgb")
    # cv2.imwrite("game_coord.png",inventory_ss)
    # print "done"

    return game_coord

if __name__ == '__main__':

    global_rs_coord = get_runescape_coord()
    # Screenshot.save("dry_run",global_rs_coord)

    # window_coord = [2559, -1, 3332, 556]
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\31 Mar 2018 21-02-10.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\1 Apr 2018 02-59-46.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\^8CFE0E4D71CFF4F482815B8070080A76F51667BC75C70EDE0E^pimgpsh_fullsize_distr.png')
    # full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\dry_run.png')
    full_ss = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\1 Apr 2018 02-59-46.png')


    grand_exchange = RSv2.GrandExchange(full_ss,global_rs_coord)

    offer_list = grand_exchange.getGEOffers()
    # print offer_list

    for key,value in offer_list[0].iteritems():
        value.clickBuy()
        # print value.getCoord()
        # print value.getGlobalCoord()
        # Mouse.win32MoveTo(value.getGlobalCoord()[2],value.getGlobalCoord()[3])
        # Mouse.win32Click(value.getGlobalCoord()[0], value.getGlobalCoord()[1])
        # print value.getStatus()

    #     print "key: %s , value: %s" % (key, offer_list[key])

    #
    # # blah =  my_exchange.getFullCoord()
    # blah = my_exchange.getAllWindows()
    # print blah
    #
    #
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