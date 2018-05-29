import win32api
import time
# from core import RS
# from core import RSv2
from corev2 import Environment
import pyautogui
import cv2
from core import Screenshot
from core import Mouse
from core import Match
from core import RandTime
from core import Keyboard

# def buy_item(runescape_window, ge_slot):
#     # click the correct buy bag
#     move_mouse_to_image_within_region('Tools/screenshots/buy_bag.png', ge_slot)
#     pyautogui.click()
#     wait_for('Tools/screenshots/quantity_box.png', runescape_window)
#     # click search box
#     move_mouse_to_image_within_region('Tools/screenshots/search_box.png', runescape_window)
#     pyautogui.click()
#     # type in item
#     random_typer(str(ge_slot.item.item_name))
#     wait_for(ge_slot.item.image_in_ge_search, runescape_window)
#     # click item
#     move_mouse_to_image_within_region(ge_slot.item.image_in_ge_search, runescape_window)
#     pyautogui.click()
#     # click price box
#     coords_of_price_box = pointfrombox.random_point((runescape_window.bottom_right_corner[0]-384, runescape_window.bottom_right_corner[1]-272),
#         (runescape_window.bottom_right_corner[0]-291, runescape_window.bottom_right_corner[1]-259))
#     realmouse.move_mouse_to(coords_of_price_box[0], coords_of_price_box[1])
#     pyautogui.click()
#     time.sleep(random.random()+1)
#     # type in correct price and hit enter
#     random_typer(str(ge_slot.item.price_instant_sold_at))
#     pyautogui.press('enter')
#     # click quantity box
#     move_mouse_to_image_within_region("Tools/screenshots/quantity_box.png", runescape_window)
#     pyautogui.click()
#     time.sleep(random.random()+2)
#     # type in correct quantity and hit enter
#     print('Min afunc is using values of {} and {}'.format(ge_slot.item.number_available_to_buy-2, (runescape_window.money/ge_slot.item.price_instant_sold_at)/runescape_window.number_of_empty_ge_slots))
#     ge_slot.item.set_quantity_to_buy(int(min(ge_slot.item.number_available_to_buy-2, (runescape_window.money/ge_slot.item.price_instant_sold_at)/runescape_window.number_of_empty_ge_slots)))
#     runescape_window.update_money(runescape_window.money - (ge_slot.item.quantity_to_buy*ge_slot.item.price_instant_sold_at))
#     random_typer(str(ge_slot.item.quantity_to_buy))
#     time.sleep(random.random())
#     pyautogui.press('enter')
#     # click confirm off
#     move_mouse_to_image_within_region("Tools/screenshots/confirm_offer_button.png", runescape_window)
#     pyautogui.click()
#     ge_slot.item.set_time_item_buy_was_placed()
#     wait_for('Tools/screenshots/lent_item_box.png', runescape_window)
#     # update states accordingly
#     runescape_window.set_time_of_last_action()
#     ge_slot.update_buy_or_sell_state('buy')
#     runescape_window.check_for_empty_ge_slots()
#     print('Placed a buy order for {} {} at {} each'.format(ge_slot.item.quantity_to_buy, ge_slot.item.item_name, ge_slot.item.price_instant_sold_at))
#     time.sleep(2+random.random())
#     ge_slot.set_image_of_slot()

def move_mouse_to_image_within_region(image, region): # region takes in an object
    image_loc = pyautogui.locateOnScreen(image, region=(region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0]-region.top_left_corner[0], region.bottom_right_corner[1]-region.top_left_corner[1]))
    while(image_loc == None):
        image_loc = pyautogui.locateOnScreen(image, region=(region.top_left_corner[0], region.top_left_corner[1], region.bottom_right_corner[0]-region.top_left_corner[0], region.bottom_right_corner[1]-region.top_left_corner[1]))
    # point_to_click = pointfrombox.random_point((image_loc[0], image_loc[1]), (image_loc[0]+image_loc[2], image_loc[1]+image_loc[3]))
    # realmouse.move_mouse_to(point_to_click[0], point_to_click[1])

if __name__ == '__main__':
    list_of_runescape_windows = Environment.detect_runescape_windows()
    for runescape_window in list_of_runescape_windows:
        for ge_slot in runescape_window.list_of_ge_slots:
            print ge_slot.buy_or_sell