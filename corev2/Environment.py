import pyautogui
import sys
sys.path.append(r"C:\Users\PPC\git\RS_BOT_2.0\core")
import Screenshot
import time
import cv2
import numpy
import os


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
    list_of_ge_slots = list(pyautogui.locateAllOnScreen(
        r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor/status_buy_button.png', region=(top_left_corner[0], top_left_corner[1], width, height)))
    return(list_of_ge_slots)

def check_if_image_exists(item_name):
    file_name = r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\items\regular/' + item_name.replace(' ', '_') + '.png'
    if os.path.isfile(file_name):
        return(file_name)
    else:
        print "missing %s image" %item_name


class runescape_instance():

    def __init__(self, position):
        off_set = [8,0,769,499]
        # Screenshot.save("blahblah.png", [position[0]+off_set[0],position[1],position[0]+off_set[2],position[1]+off_set[3]])
        self.top_left_corner = (position[0]+off_set[0],position[1])
        self.bottom_right_corner = (position[0]+off_set[2],position[1]+off_set[3])

        self.member_status = members_status_check(self.top_left_corner, self.bottom_right_corner)
        self.list_of_ge_slots = initialise_ge_slots(self.top_left_corner, self.bottom_right_corner)

        self.money = 0
        self.profit = 0
        self.last_action_time = time.time()
        # examines money to make the above line accurate
        # examine_money(position)
        # self.items_to_merch = items_to_merch(self.member_status)
        # self.list_of_items_on_cooldown = []
        self.number_of_empty_ge_slots = empty_ge_slot_check(self.list_of_ge_slots)
        # print('Initialised a window with {}Kgp and {} ge slots'.format(int(self.money/1000), self.number_of_empty_ge_slots))
        if self.member_status:
            if self.number_of_empty_ge_slots != 8:
                input("Missing 8 Slots for members.")
        elif not self.member_status:
            if self.number_of_empty_ge_slots != 3:
                input("Missing 3 Slots for none members.")

    def update_profit(self, number):
        self.profit = self.profit+number

    # def pop_oldest_item_on_cooldown(self):
    #     self.list_of_items_on_cooldown.pop(0)

    def check_for_empty_ge_slots(self):
        self.number_of_empty_ge_slots = empty_ge_slot_check(self.list_of_ge_slots)

    def set_time_of_last_action(self):
        self.last_action_time = time.time()

    # def add_to_items_on_cooldown(self, item):
    #     self.list_of_items_on_cooldown.append((item.item_name, time.time(), item.quantity_to_buy, item))

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
        self.number_available_to_buy = limit
        self.image_in_ge_search = check_if_image_exists(name)
        self.price_instant_bought_at = None
        self.price_instant_sold_at = None
        self.current_state = None # this will track if the item is currently being bought, sold or neither (None)

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

