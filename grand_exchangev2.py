import win32api
import time

import pyautogui
import cv2
import random
import os
import numpy
import re
import pickle

from corev2 import Screenshot
from corev2 import Mouse
# from corev2 import Match
from corev2 import RandTime
from corev2 import Keyboard
from corev2 import GameConstants as GC
from corev2 import RSTools
from corev2 import Environment
from corev2 import items_to_merch_module


def buy_item(runescape_window, ge_slot):
    # # click the correct buy bag

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "status_buy_button.png"), ge_slot)

    RSTools.wait_for(os.path.join(GC.anchor_path, "set_up_offer_title.png"), runescape_window)
    RSTools.wait_for(os.path.join(GC.anchor_path, "start_typing_the_name_of_an_item_to_search.png"), runescape_window)
    RandTime.randomTime(500, 700)
    Keyboard.type_this(ge_slot.item.item_name)

    # wait_for(r"C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\items\regular\Death_rune.png", runescape_window)
    RSTools.wait_for(ge_slot.item.image_in_ge_search, runescape_window)

    move_mouse_to_image_within_region(ge_slot.item.image_in_ge_search, runescape_window)

    coords_of_price_box = (
        runescape_window.top_left_corner[0] + 377, runescape_window.top_left_corner[1] + 203, 20, 15)

    Mouse.click_radius(coords_of_price_box)

    time.sleep(2 + random.random())
    RSTools.wait_for(os.path.join(GC.anchor_path, "set_price_for_each_item.png"), runescape_window)
    # # type price in and hit enter
    Keyboard.type_this(str(ge_slot.item.price_instant_bought_at))
    pyautogui.press('enter')

    coords_of_quantity_box = (
        runescape_window.top_left_corner[0] + 377, runescape_window.top_left_corner[1] + 203, 20, 15)

    Mouse.click_radius(coords_of_quantity_box)

    time.sleep(2 + random.random())
    RSTools.wait_for(os.path.join(GC.anchor_path, "how_many_do_you_wish_to_buy.png"), runescape_window)
    # # type price in and hit enter

    print('Min afunc is using values of {} and {}'.format(ge_slot.item.number_available_to_buy - 2, (
    runescape_window.money / ge_slot.item.price_instant_sold_at) / runescape_window.number_of_empty_ge_slots))
    ge_slot.item.set_quantity_to_buy(int(min(ge_slot.item.number_available_to_buy - 2, (
    runescape_window.money / ge_slot.item.price_instant_sold_at) / runescape_window.number_of_empty_ge_slots)))
    runescape_window.update_money(
        runescape_window.money - (ge_slot.item.quantity_to_buy * ge_slot.item.price_instant_sold_at))


    Keyboard.type_this(str(ge_slot.item.quantity_to_buy))
    pyautogui.press('enter')

    # # click confirm off
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "offer_confirm.png"), runescape_window)

    ge_slot.item.set_time_item_buy_was_placed()
    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)

    # # update states accordingly
    runescape_window.set_time_of_last_action()
    ge_slot.update_buy_or_sell_state('buy')
    runescape_window.check_for_empty_ge_slots()
    print('Placed a buy order for {} {} at {} each'.format(ge_slot.item.quantity_to_buy, ge_slot.item.item_name,
                                                           ge_slot.item.price_instant_sold_at))
    time.sleep(2 + random.random())
    ge_slot.set_image_of_slot()


def sell_items(runescape_window, ge_slot, record_number_selling=False):
    # # click correct sell bag
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "status_sell_button.png"), ge_slot)
    RSTools.wait_for(os.path.join(GC.anchor_path, "set_up_offer_title.png"), runescape_window)

    coords_of_item = (
        runescape_window.top_left_corner[0] + 556, runescape_window.top_left_corner[1] + 213, 20, 15)

    Mouse.click_radius(coords_of_item)
    # # click item in inv

    # # recording number selling if needed
    if record_number_selling:
        try:
            time.sleep(1 + random.random())
            quantity = check_quantity(runescape_window)
            runescape_window.update_money(runescape_window.money + (
            (ge_slot.item.quantity_to_buy - quantity) * ge_slot.item.price_instant_sold_at))
            print('About to update the quantity to buy to {}'.format(quantity))
            ge_slot.item.set_quantity_to_buy(quantity)
        except:
            print(
            "Couldn't read the quantity bought correctly so setting score to invalid to prevent artificial high scores, money for the window may now be wrong too, we think there is {}gp in this window available".format(
                runescape_window.money))
            ge_slot.item.set_score_invalid()
    # # click price button

    coords_of_price_box = (
        runescape_window.top_left_corner[0] + 377, runescape_window.top_left_corner[1] + 203, 20, 15)

    Mouse.click_radius(coords_of_price_box)

    time.sleep(2 + random.random())
    RSTools.wait_for(os.path.join(GC.anchor_path, "set_price_for_each_item.png"), runescape_window)
    # # type price in and hit enter
    Keyboard.type_this(str(ge_slot.item.price_instant_bought_at))
    pyautogui.press('enter')
    # # click confirm

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "offer_confirm.png"), runescape_window)

    # # update state of ge slot
    ge_slot.update_buy_or_sell_state('sell')
    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
    runescape_window.set_time_of_last_action()
    print('Placed a sell order for {} {} at {} each'.format(ge_slot.item.quantity_to_buy, ge_slot.item.item_name,
                                                            ge_slot.item.price_instant_bought_at))
    time.sleep(2 + random.random())
    ge_slot.set_image_of_slot()


def find_up_to_date_buy_price(runescape_window, ge_slot):
    # # click correct sell bag
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "status_sell_button.png"), ge_slot)
    RSTools.wait_for(os.path.join(GC.anchor_path, "set_up_offer_title.png"), runescape_window)

    # sell item for cheap

    # coords_of_item = pointfrombox.random_point(
    #     (runescape_window.top_left_corner[0] + 556, runescape_window.top_left_corner[1] + 213),
    #     (runescape_window.top_left_corner[0] + 576, runescape_window.top_left_corner[1] +228))


    coords_of_item = (
        runescape_window.top_left_corner[0] + 556, runescape_window.top_left_corner[1] + 213, 20, 15)

    Mouse.click_radius(coords_of_item)

    decrease_price_box_coord = (
    runescape_window.top_left_corner[0] + 277, runescape_window.top_left_corner[1] + 200, 35, 25)
    for i in range(random.randint(5, 10)):
        Mouse.click_radius(decrease_price_box_coord)
        RandTime.randomTime(15, 27)

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "offer_confirm.png"), runescape_window)

    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)

    # # collect money
    collect_items_from_ge_slot(ge_slot, runescape_window)
    # # click sale history

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "sale_history_button.png"), runescape_window)
    RSTools.wait_for(os.path.join(GC.anchor_path, "sale_history_check.png"), runescape_window)

    # # check price
    sell_price = check_price(runescape_window)
    # # updating the amount of money in the window
    runescape_window.update_money(runescape_window.money + sell_price)
    print "Wallet", runescape_window.money
    # # update price
    ge_slot.item.set_price_instant_sold_at(sell_price)
    # # click grand exchange window
    # # blocking exchange button
    Mouse.move_to_radius((runescape_window.top_left_corner[0] + 146, runescape_window.top_left_corner[1] + 25, 35, 25))

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "grand_exchange_button.png"), runescape_window)

    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)

    runescape_window.set_time_of_last_action()
    print('{} instantly sold for a price of {}'.format(ge_slot.item.item_name, ge_slot.item.price_instant_sold_at))


def find_up_to_date_sell_price(runescape_window, ge_slot):
    # click correct buy bag
    # move_mouse_to_image_within_region('Tools/screenshots/buy_bag.png', ge_slot)
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "status_buy_button.png"), ge_slot)

    RSTools.wait_for(os.path.join(GC.anchor_path, "set_up_offer_title.png"), runescape_window)
    RandTime.randomTime(500, 700)
    Keyboard.type_this(ge_slot.item.item_name)

    # wait_for(r"C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\items\regular\Death_rune.png", runescape_window)
    RSTools.wait_for(ge_slot.item.image_in_ge_search, runescape_window)

    move_mouse_to_image_within_region(ge_slot.item.image_in_ge_search, runescape_window)

    # quantity_box_coord = (runescape_window.top_left_corner[0]+375,runescape_window.top_left_corner[1]+200,35,25)
    increase_price_box_coord = (
    runescape_window.top_left_corner[0] + 431, runescape_window.top_left_corner[1] + 200, 35, 25)
    for i in range(random.randint(5, 10)):
        Mouse.click_radius(increase_price_box_coord)
        RandTime.randomTime(15, 27)

    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "offer_confirm.png"), runescape_window)

    # move_mouse_to_image_within_region('Tools/screenshots/confirm_offer_button.png', runescape_window)
    # pyautogui.click()
    # # need to add a way of putting this 1 item bought on cooldown
    runescape_window.add_single_item_to_cooldown(ge_slot.item)
    ge_slot.item.update_number_available_to_buy(ge_slot.item.number_available_to_buy - 1)

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
    runescape_window.update_money(runescape_window.money - buy_price)
    print "Wallet", runescape_window.money
    # blocking exchange button
    Mouse.move_to_radius((runescape_window.top_left_corner[0] + 146, runescape_window.top_left_corner[1] + 25, 35, 25))

    # # click grand exchange window
    move_mouse_to_image_within_region(os.path.join(GC.anchor_path, "grand_exchange_button.png"), runescape_window)

    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
    # wait_for('Tools/screenshots/lent_item_box.png', runescape_window)
    runescape_window.set_time_of_last_action()

    ge_slot.item.set_time_of_last_pc()
    print('{} instantly bought for a price of {}'.format(ge_slot.item.item_name, ge_slot.item.price_instant_bought_at))


def check_quantity(runescape_window):
    off_set = [77, 175, 222, 194]
    loc_of_quantity = (
    runescape_window.top_left_corner[0] + off_set[0], runescape_window.top_left_corner[1] + off_set[1],
    runescape_window.top_left_corner[0] + off_set[2], runescape_window.top_left_corner[1] + off_set[3])
    im = Screenshot.this(list(loc_of_quantity))
    cv2.imwrite("basdf.png", im)
    raw_string = RSTools.readNumbers(im)
    # print "raw_string",raw_string
    raw_string = raw_string.replace(",", "")
    my_regex = re.compile("^(\d+)")
    price = int(re.search(my_regex, raw_string).group(1))

    return price


def check_price(runescape_window):
    off_set = [334, 57, -305, -400]
    loc_of_price = (runescape_window.top_left_corner[0] + off_set[0], runescape_window.top_left_corner[1] + off_set[1],
                    runescape_window.bottom_right_corner[0] + off_set[2],
                    runescape_window.bottom_right_corner[1] + off_set[3])
    im = Screenshot.this(list(loc_of_price))
    # cv2.imwrite("basdf.png",im)
    raw_string = RSTools.readNumbers(im)
    raw_string = raw_string.replace(",", "")
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

    RSTools.wait_for(os.path.join(GC.anchor_path, "completed_offer_page.png"), runescape_window)
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


def move_mouse_to_image_within_region(image, region):  # region takes in an object
    image_loc = pyautogui.locateOnScreen(image, region=(
    region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0] - region.top_left_corner[0],
    region.bottom_right_corner[1] - region.top_left_corner[1]))
    while (image_loc == None):
        image_loc = pyautogui.locateOnScreen(image, region=(
        region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0] - region.top_left_corner[0],
        region.bottom_right_corner[1] - region.top_left_corner[1]))
    print image_loc
    Mouse.click_radius(image_loc)
    # Mouse.move_to_radius(image_loc)


def prevent_logout(top_left_corner, bottom_right_corner, runescape_window):
    RSTools.wait_for_w_coord(os.path.join(GC.anchor_path, "main_ge_anchor.png"), top_left_corner, bottom_right_corner)
    coords_of_item = (
        top_left_corner[0] + 690, top_left_corner[1] + 433, 20, 15)

    Mouse.move_to_radius(coords_of_item)
    Mouse.click()
    RandTime.randomTime(100, 150)
    Mouse.click()


# if __name__ == '__main__':
#     list_of_items_in_use = []
#     list_of_runescape_windows = Environment.detect_runescape_windows()
#     for runescape_window in list_of_runescape_windows:
#         for ge_slot in runescape_window.list_of_ge_slots:
#             # print "1",ge_slot.top_left_corner,ge_slot.bottom_right_corner
#
#             if ge_slot.buy_or_sell == None:
#                 # we have found an empty slot, so lets place an order
#                 list_of_items_available = []
#                 for item in runescape_window.items_to_merch:
#                     if item.item_name not in list_of_items_in_use:
#                         if item.number_available_to_buy > 0.2 * item.limit:
#                             list_of_items_available.append(item)
#                 if len(list_of_items_available) > 0:
#                     ge_slot.set_item_in_ge_slot(random.choice(list_of_items_available))
#                     print('We picked {} from our list of items randomly since our list of item names with scores is empty'.format(
#                         ge_slot.item.item_name))
#                 try:
#                     list_of_items_in_use.append(ge_slot.item.item_name)
#                     print(ge_slot.item.item_name)
#                 except:
#                     ge_slot.set_item_in_ge_slot(random.choice(list_of_items_available))
#                     list_of_items_in_use.append(ge_slot.item.item_name)
#                     print('We picked {} from our list of items randomly'.format(ge_slot.item.item_name))
#                 RSTools.wait_for(os.path.join(GC.anchor_path,"status_buy_button.png"), ge_slot)
#                 find_up_to_date_sell_price(runescape_window, ge_slot)
#                 RSTools.wait_for(os.path.join(GC.anchor_path, "status_sell_button.png"), ge_slot)
#                 find_up_to_date_buy_price(runescape_window, ge_slot)

if __name__ == '__main__':

    try:
        failfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfailfail
        with (open("list_of_runescape_windows.txt", "rb")) as openfile:
            list_of_runescape_windows = pickle.load(openfile)
        with (open("list_of_items_in_use.txt", "rb")) as openfile:
            list_of_items_in_use = pickle.load(openfile)
        with (open("start_time.txt", "rb")) as openfile:
            start_time = pickle.load(openfile)
        with (open("time_of_last_save.txt", "rb")) as openfile:
            time_of_last_save = pickle.load(openfile)
        print('We have found previous save data so will attempt to pick up where we left off previously')
        print('If you would not like this then please delete any of the 4 save files and try to run this again')
        # score_items = False
        if time.time() - time_of_last_save > 300:
            print('Not counting scores since it was over 5 minutes ago since our last save')
            score_items = False  # this variable prevents false scores being obtained by tracking when a save is loaded and not letting items be scored straight after a load
        else:
            print('Counting scores since it was under 5 minutes ago since our last save')
            score_items = True
    except Exception as e:
        score_items = True
        start_time = time.time()
        with (open("start_time.txt", "wb")) as openfile:
            pickle.dump(start_time, (openfile))

        list_of_runescape_windows = Environment.detect_runescape_windows()

        if len(list_of_runescape_windows) > 1:
            print('We have detected {} windows'.format(len(list_of_runescape_windows)))
        elif len(list_of_runescape_windows) == 1:
            print('We have detected {} window'.format(len(list_of_runescape_windows)))
        elif len(list_of_runescape_windows) == 0:
            print("Failed, we couldn't detect a runescape window, script will now abort")
            quit()
        list_of_items_in_use = []

        try:
            with (open("list_of_item_names_with_scores.txt", "rb")) as openfile:
                list_of_item_names_with_scores = pickle.load(openfile)
            list_of_item_names_with_scores.sort(key=lambda x: x[1])
        except:
            list_of_item_names_with_scores = []
            print("We couldn't find a save file for item scores so items will be picked randomly")
        # this will check if all items used are scored and if not will give them a default score of 10
        print(list_of_item_names_with_scores)
        for i in (items_to_merch_module.p2p_items() + items_to_merch_module.f2p_items()):
            item_not_in_list = True
            for j in list_of_item_names_with_scores:
                if i in j[0]:
                    item_not_in_list = False
            if item_not_in_list:
                list_of_item_names_with_scores.append([i, 500])
                print('{} was added to our list of items with scores and given a score of 500'.format(i))
        # this will check for negative values and set them equal to 10
        for i in range(len(list_of_item_names_with_scores)):
            if list_of_item_names_with_scores[i][1] < 1:
                list_of_item_names_with_scores[i][1] = 100
                print('{} was a negative score so we have set it to 100'.format(list_of_item_names_with_scores[i][0]))
        with (open("list_of_item_names_with_scores.txt", "wb")) as openfile:
            pickle.dump(list_of_item_names_with_scores, (openfile))
        logout_prevention_random_number = random.randint(150, 200)
        previous_total_profit = None
        time_of_last_save = time.time()
        last_saved_list_of_runescape_windows = list_of_runescape_windows
        last_saved_list_of_items_in_use = list_of_items_in_use
        time_of_last_update_check = time.time()
        time_of_last_save = time.time()




        while (True):
            print('Loop started')
            time.sleep(3)
            total_profit = 0
            for runescape_window in list_of_runescape_windows:
                if time.time() - runescape_window.last_action_time > logout_prevention_random_number:  # prevent auto logout
                    logout_prevention_random_number = random.randint(150, 200)
                    runescape_window.set_time_of_last_action()
                    prevent_logout(runescape_window.top_left_corner, runescape_window.bottom_right_corner,
                                   runescape_window)
                    RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
            # for each window we need to check if there are any completed offers
            # and if so handle them
            completed_offer_check = False  # variable to see if there was a completed offer
            # this will be used so that if there is one we can skip the rest of the code
            # and cycle back through to check again untill there is no completed offers
            # to handle, and we can continue filling ge slots, this gives completed offers
            # 100% priority, hopefully increasing performance
            for runescape_window in list_of_runescape_windows:
                coords_of_completed_offer = pyautogui.locateOnScreen(os.path.join(GC.anchor_path, "complete_offer.png"),
                                                                     region=(runescape_window.top_left_corner[0],
                                                                             runescape_window.top_left_corner[
                                                                                 1],
                                                                             runescape_window.bottom_right_corner[0] -
                                                                             runescape_window.top_left_corner[0],
                                                                             runescape_window.bottom_right_corner[1] -
                                                                             runescape_window.top_left_corner[1]))
                if coords_of_completed_offer == None:
                    continue
                else:
                    completed_offer_check = True
                    for ge_slot in runescape_window.list_of_ge_slots:
                        print "coords_of_completed_offer",coords_of_completed_offer
                        if ge_slot.top_left_corner[0] < coords_of_completed_offer[0] and \
                                        ge_slot.top_left_corner[1] < coords_of_completed_offer[1] and \
                                        ge_slot.bottom_right_corner[0] >coords_of_completed_offer[0] and \
                                        ge_slot.bottom_right_corner[1] >coords_of_completed_offer[1]:
                            # collects the items from the offer
                            collect_items_from_ge_slot(ge_slot, runescape_window)
                            # do stuff based on buy or sell
                            if not score_items:  # if the item has an offer complete during downtime of the script the score will be mark invalid and not be counted
                                ge_slot.item.set_score_invalid()
                            if ge_slot.buy_or_sell == 'buy':
                                # if the item was bought then it would simply sell it at the correct price (assuming the order was filled in under
                                # a certain amount of time), if the item took too long to buy then we would buy another just to confirm that our
                                # price is right). We would also place the item in the cooldown list as a tuple. this tuple would contain
                                # the item name, the time it was bought, the quantity that were bought
                                # do buy stuff
                                # place the item on cooldown
                                runescape_window.add_to_items_on_cooldown(ge_slot.item)
                                # ge_slot.item.number_available_to_buy -= ge_slot.item.quantity_to_buy old line, new is below
                                ge_slot.item.update_number_available_to_buy(
                                    ge_slot.item.number_available_to_buy - ge_slot.item.quantity_to_buy)
                                if time.time() - ge_slot.item.time_of_last_pc > 1800:
                                    # grab a new price to sell items at since it
                                    # has been a long time since we collected this
                                    # info
                                    if ge_slot.item.number_available_to_buy > 0:
                                        find_up_to_date_sell_price(runescape_window, ge_slot)
                                        if ge_slot.item.price_instant_bought_at - ge_slot.item.price_instant_sold_at > 5:
                                            ge_slot.item.set_price_instant_bought_at(
                                                ge_slot.item.price_instant_bought_at - 1)
                                # sell our items at the price instant bought at
                                sell_items(runescape_window, ge_slot)
                                RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
                                # time.sleep(2+random.random())
                                # ge_slot.set_image_of_slot()
                            elif ge_slot.buy_or_sell == 'sell':
                                runescape_window.update_money(runescape_window.money + (
                                (ge_slot.item.quantity_to_buy - 1) * ge_slot.item.price_instant_bought_at))
                                runescape_window.update_profit((ge_slot.item.quantity_to_buy - 2) * (
                                ge_slot.item.price_instant_bought_at - ge_slot.item.price_instant_sold_at))
                                print('Total profit made from this window is {}'.format(runescape_window.profit))
                                # score the item
                                # check if the item has a score, if it does update the score, if not then set the score
                                if ge_slot.item.is_score_valid:
                                    for i in range(len(list_of_item_names_with_scores)):
                                        if list_of_item_names_with_scores[i][0] == ge_slot.item.item_name:
                                            print(
                                            "{} is about to have it's score updated, it's current score is {}".format(
                                                ge_slot.item.item_name, list_of_item_names_with_scores[i][1]))
                                            list_of_item_names_with_scores[i][1] = int(((list_of_item_names_with_scores[
                                                                                             i][1] * 5) + ((
                                                                                                           10 * ge_slot.item.quantity_to_buy * (
                                                                                                           ge_slot.item.price_instant_bought_at - ge_slot.item.price_instant_sold_at)) / (
                                                                                                           time.time() - ge_slot.item.time_buy_order_placed))) / 6)
                                            print("{} has had it's score updated, it's new score is {}".format(
                                                ge_slot.item.item_name, list_of_item_names_with_scores[i][1]))
                                            break
                                        if list_of_item_names_with_scores[i] == list_of_item_names_with_scores[-1]:
                                            list_of_item_names_with_scores.append([ge_slot.item.item_name, int(((
                                                                                                                10 * ge_slot.item.quantity_to_buy * (
                                                                                                                ge_slot.item.price_instant_bought_at - ge_slot.item.price_instant_sold_at)) / (
                                                                                                                time.time() - ge_slot.item.time_buy_order_placed)))])
                                            print('{} was added to the list of scores with a score of {}'.format(
                                                ge_slot.item.item_name, list_of_item_names_with_scores[-1][1]))
                                    if len(list_of_item_names_with_scores) == 0:
                                        print("The list of scored items is about to have it's first entry added")
                                        list_of_item_names_with_scores.append([ge_slot.item.item_name, int(((
                                                                                                            ge_slot.item.quantity_to_buy * (
                                                                                                            ge_slot.item.price_instant_bought_at - ge_slot.item.price_instant_sold_at)) / (
                                                                                                            time.time() - ge_slot.item.time_buy_order_placed)))])
                                with (open("list_of_item_names_with_scores.txt", "wb")) as openfile:
                                    pickle.dump(list_of_item_names_with_scores, (openfile))
                                # if the item was sold then we would score the item based on the profit it made us and the time it took to buy and sell
                                ge_slot.update_buy_or_sell_state(
                                    None)  # updates the buy or sell state to none to indiate the slot is now empty
                                # still need to update lists of items in use accordingly
                                # perhaps like this
                                list_of_items_in_use.remove(ge_slot.item.item_name)
                                ge_slot.item.set_price_instant_bought_at(None)
                                ge_slot.item.set_price_instant_sold_at(None)
                                ge_slot.set_item_in_ge_slot(None)
                            break

            if not score_items:
                print('Since we have just loaded from a save all scores are currently being marked as invalid and will not effect their rating')
            if not completed_offer_check:
                if not score_items:
                    print('Scores from now will be valid')
                    score_items = True
                empty_slot_check = False # check if we have found an empty slot, this will be used to break out
                                        # once we have, so that we only place 1 order before going back through
                                        # the loop to check for completed offers and such


                highest_cash = 0
                for runescape_window in list_of_runescape_windows:
                    if runescape_window.number_of_empty_ge_slots > 0:
                        highest_cash = max(highest_cash, runescape_window.money)


                for runescape_window in list_of_runescape_windows:
                    if runescape_window.money == highest_cash:  # scans until it finds the window with the most money in
                        for ge_slot in runescape_window.list_of_ge_slots:
                            if ge_slot.buy_or_sell == None:
                                # we have found an empty slot, so lets place an order
                                print "# we have found an empty slot, so lets place an order"
                                list_of_items_available = []
                                for item in runescape_window.items_to_merch:
                                    if item.item_name not in list_of_items_in_use:
                                        if item.number_available_to_buy > 0.2*item.limit:
                                            list_of_items_available.append(item)
                                if len(list_of_items_available) > 0:
                                    ###########################################################################################################################################################################################################################################################################
                                    if len(list_of_item_names_with_scores) > 0:
                                        # need to filter list_of_item_names_with_scores to only include items that are also in list_of_items_available
                                        temp_list_of_item_names_with_scores = []
                                        temp_list_of_items_available_by_name = []
                                        for i in range(len(list_of_items_available)):
                                            temp_list_of_items_available_by_name.append(list_of_items_available[i].item_name)
                                        for i in range(len(list_of_item_names_with_scores)):
                                            if list_of_item_names_with_scores[i][0] in temp_list_of_items_available_by_name:
                                                temp_list_of_item_names_with_scores.append(list_of_item_names_with_scores[i]) ##################################THIS WHOLE SECTION IS UN TESTED
                                        list_of_items = []
                                        list_of_scores = []
                                        for i in range(len(temp_list_of_item_names_with_scores)):
                                            list_of_items.append(temp_list_of_item_names_with_scores[i][0])
                                            list_of_scores.append(temp_list_of_item_names_with_scores[i][1])
                                        normalised_scores = []
                                        for i in range(len(list_of_scores)):
                                            normalised_scores.append(list_of_scores[i]/sum(list_of_scores))
                                        #print(normalised_scores)
                                        #print(list_of_items)
                                        seed = random.random()
                                        for i in range(len(normalised_scores)):
                                            seed -= normalised_scores[i]
                                            if seed < 0:
                                                for item in runescape_window.items_to_merch:
                                                    if item.item_name == list_of_items[i]:
                                                        ge_slot.set_item_in_ge_slot(item)
                                                        print('We picked {} from our list of items with scores'.format(ge_slot.item.item_name))

                                                        for i in range(len(list_of_item_names_with_scores)):
                                                            if list_of_item_names_with_scores[i][0] == ge_slot.item.item_name:
                                                                list_of_item_names_with_scores[i][1] = int(list_of_item_names_with_scores[i][1]*0.9)
                                                        break
                                                break
    #                                 ###########################################################################################################################################################################################################################################################################
    #                                 else:
    #                                     ge_slot.set_item_in_ge_slot(random.choice(list_of_items_available)) # This is the line where I will later be choosing items based on score instead of randomly
    #                                     print('We picked {} from our list of items randomly since our list of item names with scores is empty'.format(ge_slot.item.item_name))
    #                                 try:
    #                                     list_of_items_in_use.append(ge_slot.item.item_name)
    #                                     print(ge_slot.item.item_name)   #TESTING TAKING THIS BLOCK OF CODE OUT
    #                                 except:
    #                                     ge_slot.set_item_in_ge_slot(random.choice(list_of_items_available))
    #                                     list_of_items_in_use.append(ge_slot.item.item_name)
    #                                     print('We picked {} from our list of items randomly'.format(ge_slot.item.item_name))
    #                                 RSTools.wait_for(os.path.join(GC.anchor_path, "status_buy_button.png"), ge_slot)
    #                                 find_up_to_date_sell_price(runescape_window, ge_slot)
    #                                 RSTools.wait_for(os.path.join(GC.anchor_path, "status_sell_button.png"), ge_slot)
    #                                 find_up_to_date_buy_price(runescape_window, ge_slot)
    #                                 if ge_slot.item.price_instant_bought_at < ge_slot.item.price_instant_sold_at:
    #                                     temp = ge_slot.item.price_instant_bought_at
    #                                     ge_slot.item.set_price_instant_bought_at(ge_slot.item.price_instant_sold_at)
    #                                     ge_slot.item.set_price_instant_sold_at(temp)
    #                                 if ge_slot.item.price_instant_bought_at - ge_slot.item.price_instant_sold_at > 5:
    #                                     ge_slot.item.set_price_instant_bought_at(ge_slot.item.price_instant_bought_at -1)
    #                                     ge_slot.item.set_price_instant_sold_at(ge_slot.item.price_instant_sold_at +1)
    #                                 ge_slot.item.set_score_valid()
    #                                 RSTools.wait_for(os.path.join(GC.anchor_path, "status_buy_button.png"),ge_slot)
    #
    #                                 buy_item(runescape_window, ge_slot)
    #
    #                                 RSTools.wait_for(os.path.join(GC.anchor_path, "main_ge_anchor.png"), runescape_window)
    #                                 #time.sleep(2+random.random())
    #                                 #ge_slot.set_image_of_slot()
    #                             empty_slot_check = True
    #                         if empty_slot_check == True:
    #                             break
    #                 if empty_slot_check == True:
    #                     break
    #         for runescape_window in list_of_runescape_windows:
    #             runescape_window.check_for_empty_ge_slots() # this will update states of ge slots correctly
    #             # we can also add other updates into here such as checking items on cooldown, more to add later
    #             if len(runescape_window.list_of_items_on_cooldown) > 0:
    #                 cooldown_tuple = runescape_window.list_of_items_on_cooldown[0]
    #                 if time.time() - cooldown_tuple[1] > 14400: # then it has been 4 hours so remove from list
    #                     for item in runescape_window.items_to_merch:
    #                         if item.item_name == cooldown_tuple[0]:
    #                             cooldown_tuple[3].update_number_available_to_buy(item.number_available_to_buy+cooldown_tuple[2])
    #                             runescape_window.pop_oldest_item_on_cooldown()
    #                             break
    #             total_profit += runescape_window.profit
    #         #if time.time()-time_of_last_update_check > 10:
    #         break_check = False
    #         for runescape_window in list_of_runescape_windows:
    #             for ge_slot in runescape_window.list_of_ge_slots:
    #                 if ge_slot.buy_or_sell != None:
    #                     check_for_in_progress_or_view_offer(ge_slot)
    #                     #print('Last screenshot of {} was taken {} seconds ago'.format(ge_slot.item.item_name, time.time()-ge_slot.time_of_last_screenshot))
    #                     if not (ge_slot.image_of_slot==numpy.array(pyautogui.screenshot(region=(ge_slot.top_left_corner[0], ge_slot.top_left_corner[1] + 90, 165, 10)))).all():
    #                         ge_slot.set_image_of_slot()
    #                     elif time.time() - ge_slot.time_of_last_screenshot > 1800 and not completed_offer_check and not empty_slot_check:
    #                         print('Image of {} has not been updated in 30 minutes so we are aborting the offer'.format(ge_slot.item.item_name))
    #                         # run cancel offer code
    #                         # first we cancel the offer
    #                         #print('We are about to cancel an offer that we believe to be in the window with coords {}, we are at line 287'.format(runescape_window.bottom_right_corner))
    #                         cancel_offer(ge_slot.top_left_corner, ge_slot.bottom_right_corner, runescape_window)
    #                         wait_for('Tools/screenshots/red_cancel_bar.png', runescape_window)
    #                         time.sleep(2+random.random())
    #                         print("Cancelled {} since the offer hasn't been updated in a while".format(ge_slot.item.item_name))
    #                         # then if the item was a buy we handle it
    #                         if ge_slot.buy_or_sell == 'buy':
    #                             handle_cancelling_buy(runescape_window, ge_slot, list_of_items_in_use)
    #                         elif ge_slot.buy_or_sell == 'sell':
    #                             handle_cancelling_sell(runescape_window, ge_slot, list_of_items_in_use)
    #                         # we check if any of the item  bought and if so try to sell it
    #                         # we could check the sale history to read the number of items bought and update accordingly
    #                         # then if it was a sell we handle it
    #                         # we would simply retrieve the items and money and update accordingly, then find the new sell price and sell
    #                         break_check = True
    #                     elif time.time() - ge_slot.time_of_last_screenshot > 3600 and ge_slot.buy_or_sell == 'sell':
    #                         print('Image of {} has not been updated in 1 hour so we are aborting the offer'.format(ge_slot.item.item_name))
    #                         # run cancel offer code
    #                         # first we cancel the offer
    #                         # print('We are about to cancel an offer that we believe to be in the window with coords {}, we are at line 287'.format(runescape_window.bottom_right_corner))
    #                         cancel_offer(ge_slot.top_left_corner, ge_slot.bottom_right_corner, runescape_window)
    #                         wait_for('Tools/screenshots/red_cancel_bar.png', runescape_window)
    #                         time.sleep(2+random.random())
    #                         # print("Cancelled {} since the offer hasn't been updated in a while".format(ge_slot.item.item_name))
    #                         handle_cancelling_sell(runescape_window, ge_slot, list_of_items_in_use)
    #                         # we check if any of the item  bought and if so try to sell it
    #                         # we could check the sale history to read the number of items bought and update accordingly
    #                         # then if it was a sell we handle it
    #                         # we would simply retrieve the items and money and update accordingly, then find the new sell price and sell
    #                         break_check = True
    #                     elif time.time() - ge_slot.time_of_last_screenshot > 5400 and ge_slot.buy_or_sell == 'buy':
    #                         print('Image of {} has not been updated in 1.5 hours so we are aborting the offer'.format(ge_slot.item.item_name))
    #                         # run cancel offer code
    #                         # first we cancel the offer
    #                         # print('We are about to cancel an offer that we believe to be in the window with coords {}, we are at line 287'.format(runescape_window.bottom_right_corner))
    #                         cancel_offer(ge_slot.top_left_corner, ge_slot.bottom_right_corner, runescape_window)
    #                         wait_for('Tools/screenshots/red_cancel_bar.png', runescape_window)
    #                         time.sleep(2+random.random())
    #                         # print("Cancelled {} since the offer hasn't been updated in a while".format(ge_slot.item.item_name))
    #                         handle_cancelling_buy(runescape_window, ge_slot, list_of_items_in_use)
    #                         # we check if any of the item  bought and if so try to sell it
    #                         # we could check the sale history to read the number of items bought and update accordingly
    #                         # then if it was a sell we handle it
    #                         # we would simply retrieve the items and money and update accordingly, then find the new sell price and sell
    #                         break_check = True
    #                 if break_check:
    #                     break
    #             if break_check:
    #                 break
    #             #time_of_last_update_check = time.time()
    #
    #         if time.time()-time_of_last_save > 60 or last_saved_list_of_runescape_windows != list_of_runescape_windows or last_saved_list_of_items_in_use != list_of_items_in_use or total_profit != previous_total_profit:
    #             previous_total_profit = total_profit
    #             last_saved_list_of_runescape_windows = list_of_runescape_windows
    #             last_saved_list_of_items_in_use = list_of_items_in_use
    #             time_of_last_save = time.time()
    #             with (open("list_of_items_in_use.txt", "wb")) as openfile:
    #                 pickle.dump(list_of_items_in_use,(openfile))
    #             with (open("list_of_runescape_windows.txt", "wb")) as openfile:
    #                 pickle.dump(list_of_runescape_windows,(openfile))
    #             with (open("list_of_item_names_with_scores.txt", "wb")) as openfile:
    #                 pickle.dump(list_of_item_names_with_scores,(openfile))
    #             with (open("time_of_last_save.txt", "wb")) as openfile:
    #                 pickle.dump(time_of_last_save,(openfile))
    #             print('State has now been saved, you may be able to close the script and return from this point later')
    #             print('Total profit made across all windows so far is {}. We have been running for {} minutes, this is a profit per hour of {}k per hour.'.format(total_profit, int((time.time()-start_time)/60), int(3.6*total_profit/(time.time()-start_time))))
    #             time_of_last_save = time.time()
    #             #print('Current scored item list {}'.format(list_of_item_names_with_scores))
    #         '''if total_profit != previous_total_profit:
    #             previous_total_profit = total_profit
    #             #label = myfont.render("Current Total Profit: {}".format(total_profit), 1, (255,255,0))
    #             #game_display.blit(label, (10, 10))
    #             #pygame.display.update()
    #             print('Total profit made across all windows so far is {}. We have been running for {} minutes, this is a profit per hour of {}k per hour.'.format(total_profit, int((time.time()-start_time)/60), int(3.6*total_profit/(time.time()-start_time))))'''
    # # if there are no completed orders then we need to
    # # check for empty ge slots and fill them with
    # # orders
    # # all orders should be unique, ie not buying coal on 2 windows at once, this would harm profit since they would be
    # # competing with eachother. Instead one window should buy it, then once it has sold the next window can start to buy