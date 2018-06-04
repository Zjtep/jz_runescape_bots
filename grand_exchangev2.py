import win32api
import time

import pyautogui
import cv2
import random
import os
import numpy
import re

from corev2 import Screenshot
from corev2 import Mouse
# from corev2 import Match
from corev2 import RandTime
from corev2 import Keyboard
from corev2 import GameConstants as GC
from corev2 import RSTools
from corev2 import Environment


def find_up_to_date_buy_price(runescape_window, ge_slot):
    # # click correct sell bag
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "status_buy_button.png"), ge_slot)
    RSTools.wait_for(os.path.join(GC.anchor_path, "set_up_offer_title.png"), runescape_window)

    # sell item for cheap

    # coords_of_item = pointfrombox.random_point(
    #     (runescape_window.bottom_right_corner[0] - 180, runescape_window.bottom_right_corner[1] - 372),
    #     (runescape_window.bottom_right_corner[0] - 166, runescape_window.bottom_right_corner[1] - 349))
    # realmouse.move_mouse_to(coords_of_item[0], coords_of_item[1])
    # pyautogui.click()
    #
    # '''move_mouse_to_image_within_region('Tools/screenshots/-5perc_button.png', runescape_window)
    # for i in range(random.randint(25,35)):
    #     pyautogui.click()
    #     time.sleep(random.random()/7)'''
    #
    # coords_of_price_box = pointfrombox.random_point(
    #     (runescape_window.bottom_right_corner[0] - 384, runescape_window.bottom_right_corner[1] - 272), (
    #     runescape_window.bottom_right_corner[0] - 291,
    #     runescape_window.bottom_right_corner[1] - 259))  ##########################
    # realmouse.move_mouse_to(coords_of_price_box[0], coords_of_price_box[1])
    # pyautogui.click()
    # time.sleep(2 + random.random())
    # random_typer('1')
    # pyautogui.press(
    #     'enter')  #########################################################################################################
    #
    # time.sleep(random.random() + 1)
    # move_mouse_to_image_within_region('Tools/screenshots/confirm_offer_button.png', runescape_window)
    # pyautogui.click()
    # wait_for('Tools/screenshots/lent_item_box.png', runescape_window)
    # # collect money
    # collect_items_from_ge_slot(ge_slot, runescape_window)
    # # click sale history
    # move_mouse_to_image_within_region('Tools/screenshots/sale_history_button.png', runescape_window)
    # pyautogui.click()
    # wait_for('Tools/screenshots/sale_history_check.png', runescape_window)
    # # check price
    # sell_price = check_price(runescape_window)
    # # updating the amount of money in the window
    # runescape_window.update_money(runescape_window.money + sell_price)
    # # update price
    # ge_slot.item.set_price_instant_sold_at(sell_price)
    # # click grand exchange window
    # move_mouse_to_box('Tools/screenshots/grand_exchange_button.png',
    #                   runescape_window.top_left_corner, runescape_window.bottom_right_corner)
    # pyautogui.click()
    # wait_for('Tools/screenshots/lent_item_box.png', runescape_window)
    # runescape_window.set_time_of_last_action()
    # print('{} instantly sold for a price of {}'.format(ge_slot.item.item_name, ge_slot.item.price_instant_sold_at))


def find_up_to_date_sell_price(runescape_window, ge_slot):
    # click correct buy bag
    # move_mouse_to_image_within_region('Tools/screenshots/buy_bag.png', ge_slot)
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "status_buy_button.png"),ge_slot)

    RSTools.wait_for(os.path.join(GC.anchor_path, "set_up_offer_title.png"), runescape_window)
    RandTime.randomTime(500, 700)
    Keyboard.type_this(ge_slot.item.item_name)

    # wait_for(r"C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\items\regular\Death_rune.png", runescape_window)
    RSTools.wait_for(ge_slot.item.image_in_ge_search, runescape_window)

    move_mouse_to_image_within_region(ge_slot.item.image_in_ge_search,runescape_window)

    # quantity_box_coord = (runescape_window.top_left_corner[0]+375,runescape_window.top_left_corner[1]+200,35,25)
    increase_price_box_coord = (runescape_window.top_left_corner[0] + 431, runescape_window.top_left_corner[1] + 200, 35, 25)
    for i in range(random.randint(5,10)):
        Mouse.click_radius(increase_price_box_coord)
        RandTime.randomTime(15,27)

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "offer_confirm.png"), runescape_window)

    # move_mouse_to_image_within_region('Tools/screenshots/confirm_offer_button.png', runescape_window)
    # pyautogui.click()
    # # need to add a way of putting this 1 item bought on cooldown
    runescape_window.add_single_item_to_cooldown(ge_slot.item)
    ge_slot.item.update_number_available_to_buy(ge_slot.item.number_available_to_buy-1)

    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)

    # # collect item
    collect_items_from_ge_slot(ge_slot, runescape_window)
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "sale_history_button.png"), runescape_window)

    # # click sale history
    # move_mouse_to_image_within_region('Tools/screenshots/sale_history_button.png', runescape_window)
    # pyautogui.click()
    RSTools.wait_for(os.path.join(GC.anchor_path, "sale_history_check.png"), runescape_window)
    # wait_for('Tools/screenshots/sale_history_check.png', runescape_window)
    # # check price
    buy_price = check_price(runescape_window)

    # # update price
    ge_slot.item.set_price_instant_bought_at(buy_price)
    # # updating the amount of money in the window
    runescape_window.update_money(runescape_window.money-buy_price)
    print runescape_window.money

    Mouse.move_to_radius((runescape_window.top_left_corner[0] + 146, runescape_window.top_left_corner[1] + 25, 35, 25))

    # # click grand exchange window
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "grand_exchange_button.png"), runescape_window)

    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
    # wait_for('Tools/screenshots/lent_item_box.png', runescape_window)
    runescape_window.set_time_of_last_action()

    ge_slot.item.set_time_of_last_pc()
    print('{} instantly bought for a price of {}'.format(ge_slot.item.item_name, ge_slot.item.price_instant_bought_at))


def check_price(runescape_window):
    off_set = [334,57,-305,-400]
    loc_of_price = (runescape_window.top_left_corner[0] +off_set[0], runescape_window.top_left_corner[1]+off_set[1],
        runescape_window.bottom_right_corner[0] +off_set[2], runescape_window.bottom_right_corner[1]+off_set[3])
    im = Screenshot.this(list(loc_of_price))
    # cv2.imwrite("basdf.png",im)
    raw_string = RSTools.readNumbers(im)
    raw_string = raw_string.replace(",","")
    my_regex = re.compile("^(\d+)")
    price = int(re.search(my_regex, raw_string).group(1))

    return price

def collect_items_from_ge_slot(ge_slot, runescape_window):
    point_to_click = Mouse.random_point(ge_slot.top_left_corner, ge_slot.bottom_right_corner)
    # print ge_slot.top_left_corner,ge_slot.bottom_right_corner
    # point_to_click  = (ge_slot.top_left_corner[0], ge_slot.top_left_corner[0], 115, 110)
    # Mouse.click_radius(point_to_click)
    #
    Mouse.move_mouse_to_click(point_to_click[0], point_to_click[1])

    RSTools.wait_for(os.path.join(GC.anchor_path,"completed_offer_page.png"), runescape_window)
    # point_of_item_collection_box_1 = Mouse.random_point((runescape_window.bottom_right_corner[0] - 303, runescape_window.bottom_right_corner[
    #                                                            1] - 166), (runescape_window.bottom_right_corner[0] - 273, runescape_window.bottom_right_corner[1] - 138))
    # point_of_item_collection_box_2 = Mouse.random_point((runescape_window.bottom_right_corner[0] - 254, runescape_window.bottom_right_corner[
    #                                                            1] - 166), (runescape_window.bottom_right_corner[0] - 222, runescape_window.bottom_right_corner[1] - 138))

    point_of_item_collection_box_1 = (
        runescape_window.top_left_corner[0] + 394, runescape_window.top_left_corner[1] + 269, 25, 25)
    point_of_item_collection_box_2 = (
        runescape_window.top_left_corner[0] + 446, runescape_window.top_left_corner[1] + 269, 25, 25)

    Mouse.click_radius(point_of_item_collection_box_1)
    Mouse.click_radius(point_of_item_collection_box_2)
    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
    # realmouse.move_mouse_to(point_of_item_collection_box_2[0], point_of_item_collection_box_2[1])
    # pyautogui.click()
    # realmouse.move_mouse_to(point_of_item_collection_box_1[0], point_of_item_collection_box_1[1])
    # pyautogui.click()
    # wait_for('Tools/screenshots/lent_item_box.png', runescape_window)

def move_mouse_to_image_within_region(image, region): # region takes in an object
    image_loc = pyautogui.locateOnScreen(image, region=(region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0]-region.top_left_corner[0], region.bottom_right_corner[1]-region.top_left_corner[1]))
    while(image_loc == None):
        image_loc = pyautogui.locateOnScreen(image, region=(region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0]-region.top_left_corner[0], region.bottom_right_corner[1]-region.top_left_corner[1]))
    print image_loc
    Mouse.click_radius(image_loc)
    # Mouse.move_to_radius(image_loc)

if __name__ == '__main__':
    list_of_items_in_use = []

    list_of_runescape_windows = Environment.detect_runescape_windows()
    for runescape_window in list_of_runescape_windows:
        for ge_slot in runescape_window.list_of_ge_slots:
            # print "1",ge_slot.top_left_corner,ge_slot.bottom_right_corner

            if ge_slot.buy_or_sell == None:
                # we have found an empty slot, so lets place an order
                list_of_items_available = []
                for item in runescape_window.items_to_merch:
                    if item.item_name not in list_of_items_in_use:
                        if item.number_available_to_buy > 0.2 * item.limit:
                            list_of_items_available.append(item)
                if len(list_of_items_available) > 0:
                    ge_slot.set_item_in_ge_slot(random.choice(list_of_items_available))
                    print('We picked {} from our list of items randomly since our list of item names with scores is empty'.format(
                        ge_slot.item.item_name))
                try:
                    list_of_items_in_use.append(ge_slot.item.item_name)
                    print(ge_slot.item.item_name)
                except:
                    ge_slot.set_item_in_ge_slot(random.choice(list_of_items_available))
                    list_of_items_in_use.append(ge_slot.item.item_name)
                    print('We picked {} from our list of items randomly'.format(ge_slot.item.item_name))
                RSTools.wait_for(os.path.join(GC.anchor_path,"status_buy_button.png"), ge_slot)
                find_up_to_date_sell_price(runescape_window, ge_slot)
                RSTools.wait_for(os.path.join(GC.anchor_path, "status_sell_button.png"), ge_slot)
                find_up_to_date_buy_price(runescape_window, ge_slot)
