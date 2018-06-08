import pyautogui
import sys
sys.path.append(r"C:\Users\PPC\git\RS_BOT_2.0\core")
import Screenshot
import time
import cv2
import numpy
import os
import re
import items_to_merch_module
import GameConstants as GC
import Mouse
import RSTools
import RandTime

def detect_runescape_windows():  # this function will detect how many runescape windows are present and where they are
    list_of_runescape_windows = []
    # for i in pyautogui.locateAllOnScreen('Tools/screenshots/collect_all_buttons.png'):
    for i in pyautogui.locateAllOnScreen(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\Rune_Lite.png'):
        list_of_runescape_windows.append(
            runescape_instance((i[0], i[1] + i[3])))
    return(list_of_runescape_windows)

def members_status_check(top_left_corner, bottom_right_corner):
    width = bottom_right_corner[0] - top_left_corner[0]
    height = bottom_right_corner[1] - top_left_corner[1]
    if len(list(pyautogui.locateAllOnScreen(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\non_member_slot.png',
                             region=(top_left_corner[0], top_left_corner[1], width, height)))) != 0:
        return(False)
    else:
        return(True)

def empty_ge_slot_check(list_of_ge_slots):
    number_of_ge_slots_open = 0
    for slot in list_of_ge_slots:
        if slot.buy_or_sell == None:
            number_of_ge_slots_open += 1
    return(number_of_ge_slots_open)

def initialise_ge_slots(top_left_corner, bottom_right_corner):
    ge_slots = []
    for i in count_ge_slots(top_left_corner, bottom_right_corner):
        ge_slots.append(ge_slot(((i[0], i[1]), (i[0] + i[2], i[1] + i[3]))))
    return(ge_slots)

def count_ge_slots(top_left_corner, bottom_right_corner):
    # Screenshot.save("bpang.png",[top_left_corner[0],top_left_corner[1],bottom_right_corner[0],bottom_right_corner[1]])
    width = bottom_right_corner[0] - top_left_corner[0]
    height = bottom_right_corner[1] - top_left_corner[1]
    list_of_ge_slots = list(pyautogui.locateAllOnScreen(os.path.join(GC.anchor_path,"member_slot2.png"), region=(top_left_corner[0], top_left_corner[1], width, height)))
    print list_of_ge_slots
    return(list_of_ge_slots)

def check_if_image_exists(item_name):
    file_name = r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\items\regular/' + item_name.replace(' ', '_') + '.png'
    if os.path.isfile(file_name):
        return(file_name)
    else:
        print "missing %s image" %item_name

def items_to_merch(member_status):
    if member_status:
        items_to_merch = []
        # below is a list of members items to merch
        list_of_items = items_to_merch_module.p2p_items()
        # list_of_item_limits = gelimitfinder.find_ge_limit(list_of_items)
        list_of_item_limits = items_to_merch_module.p2p_items_limit()
        for i in range(len(list_of_item_limits)):
            list_of_item_limits[i] -= 1
        for i in range(len(list_of_items)):
            items_to_merch.append(item(list_of_items[i], list_of_item_limits[i]))
        # we are a member so initialise a members item list
    else:
        items_to_merch = []
        # below is a list of f2p items to merch
        list_of_items = items_to_merch_module.f2p_items()
        # list_of_item_limits = gelimitfinder.find_ge_limit(list_of_items)
        list_of_item_limits =  items_to_merch_module.f2p_items_limit()
        for i in range(len(list_of_item_limits)):
            list_of_item_limits[i] -= 1
        for i in range(len(list_of_items)):
            items_to_merch.append(item(list_of_items[i], list_of_item_limits[i]))
        # we are f2p so initialise a f2p item list
    return(items_to_merch)

def detect_money(top_left_corner, bottom_right_corner):
    RSTools.wait_for_w_coord(os.path.join(GC.anchor_path, "main_ge_anchor.png"), top_left_corner,bottom_right_corner)
    coords_of_item = (
        top_left_corner[0] + 690, top_left_corner[1] + 433, 20, 15)

    Mouse.move_to_radius(coords_of_item)
    Mouse.right_click()

    image = os.path.join(GC.anchor_path, "examine_coins.png")
    image_loc = pyautogui.locateOnScreen(image, region=(top_left_corner[0], top_left_corner[1], bottom_right_corner[0]-top_left_corner[0], bottom_right_corner[1]-top_left_corner[1]))
    while(image_loc == None):
        image_loc = pyautogui.locateOnScreen(image, region=(top_left_corner[0], top_left_corner[1], bottom_right_corner[0]-top_left_corner[0], bottom_right_corner[1]-top_left_corner[1]))
    print image_loc
    Mouse.click_radius(image_loc)
    RandTime.randomTime(1000, 1500)
    money_val = check_total_coins(top_left_corner, bottom_right_corner)
    print "Wallet", money_val
    return(money_val)

def check_total_coins(top_left_corner, bottom_right_corner):
    off_set = [6,440,-200,-47]
    loc_of_price = (top_left_corner[0] +off_set[0], top_left_corner[1]+off_set[1],
        bottom_right_corner[0] +off_set[2], bottom_right_corner[1]+off_set[3])
    im = Screenshot.this(list(loc_of_price))
    cv2.imwrite("basdf.png",im)
    raw_string = RSTools.read_total_coins(im)
    print raw_string

    raw_string = raw_string.replace(",","")
    my_regex = re.compile("^(\d+)")
    price = int(re.search(my_regex, raw_string).group(1))
    # print price
    return price


class runescape_instance():

    def __init__(self, position):
        off_set = [8,0,769,499]
        # Screenshot.save("blahblah.png", [position[0]+off_set[0],position[1],position[0]+off_set[2],position[1]+off_set[3]])
        self.top_left_corner = (position[0]+off_set[0],position[1])
        self.bottom_right_corner = (position[0]+off_set[2],position[1]+off_set[3])

        self.member_status = members_status_check(self.top_left_corner, self.bottom_right_corner)
        self.list_of_ge_slots = initialise_ge_slots(self.top_left_corner, self.bottom_right_corner)

        self.money = 0
        self.money = detect_money(self.top_left_corner, self.bottom_right_corner)
        self.profit = 0
        self.last_action_time = time.time()
        # examines money to make the above line accurate
        # examine_money(position)
        self.items_to_merch = items_to_merch(self.member_status)
        self.list_of_items_on_cooldown = []
        self.number_of_empty_ge_slots = empty_ge_slot_check(self.list_of_ge_slots)
        # print('Initialised a window with {}Kgp and {} ge slots'.format(int(self.money/1000), self.number_of_empty_ge_slots))
        if self.member_status:
            if self.number_of_empty_ge_slots != 8:
                input("Missing 8 Slots for members.")
        elif not self.member_status:
            if self.number_of_empty_ge_slots != 3:
                input("Missing 3 Slots for none members.")
                # print ("Missing 3 Slots for none members.")

    def update_profit(self, number):
        self.profit = self.profit+number

    # def pop_oldest_item_on_cooldown(self):
    #     self.list_of_items_on_cooldown.pop(0)

    def check_for_empty_ge_slots(self):
        self.number_of_empty_ge_slots = empty_ge_slot_check(self.list_of_ge_slots)

    def set_time_of_last_action(self):
        self.last_action_time = time.time()

    def add_single_item_to_cooldown(self, item):
        self.list_of_items_on_cooldown.append((item.item_name, time.time(), 1, item))

    def add_to_items_on_cooldown(self, item):
        self.list_of_items_on_cooldown.append((item.item_name, time.time(), item.quantity_to_buy, item))

    # def add_single_item_to_cooldown(self, item):
    #     self.list_of_items_on_cooldown.append((item.item_name, time.time(), 1, item))


    def update_money(self, number):
        self.money = number

class ge_slot():

    def __init__(self, position):
        self.top_left_corner = position[0]
        self.bottom_right_corner = position[1]
        self.buy_or_sell = None
        self.item = None

    def update_buy_or_sell_state(self, state):
        self.buy_or_sell = state

    def set_item_in_ge_slot(self, item):
        self.item = item

    def set_time_of_last_screenshot(self):
        self.time_of_last_screenshot = time.time()

    def set_image_of_slot(self):
        self.image_of_slot = numpy.array(pyautogui.screenshot(region=(self.top_left_corner[0], self.top_left_corner[1] + 90, 165, 10)))
        self.set_time_of_last_screenshot()
        print('Image of {} has been updated'.format(self.item.item_name))

class item():

    def __init__(self, name, limit):
        self.item_name = name
        self.limit = limit
        self.number_available_to_buy = 50
        self.image_in_ge_search = check_if_image_exists(name)
        self.price_instant_bought_at = None
        self.price_instant_sold_at = None
        self.current_state = None # this will track if the item is currently being bought, sold or neither (None)
        self.quantity_to_buy = None

    def set_score_valid(self):
        self.is_score_valid = True

    def set_score_invalid(self):
        self.is_score_valid = False

    def set_time_item_buy_was_placed(self):
        self.time_buy_order_placed = time.time()

    def update_number_available_to_buy(self, number):
        self.number_available_to_buy = number

    def set_time_of_last_pc(self):
        self.time_of_last_pc = time.time()

    def set_price_instant_bought_at(self, price):
        self.price_instant_bought_at = price

    def set_price_instant_sold_at(self, price):
        self.price_instant_sold_at = price

    def set_quantity_to_buy(self, number):
        self.quantity_to_buy = number

    def set_current_state(self, state):
        self.current_state = state

