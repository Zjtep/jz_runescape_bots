import os
import cv2

#GameConstants.py
KEY_Q = 81
KEY_E = 69
KEY_W = 87
KEY_R = 82

KEY_F = 70
KEY_G = 71
KEY_T = 84

KEY_NUM9 = 105
KEY_F1 = 112
KEY_F8 = 119
KEY_F9 = 120

MEMBEER_STATUS = False

bag_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\bag_icon.png', 0)

exchange_history_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\exchange_history_icon.png', 0)
exchange_offer_page_dimensions = [483,303]
# http://mirametrics.com/help/mira_pro_script_7/source/getkeystate.htm
#pvp_macos

status_buy_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\status_buy_icon.png', 0)
status_sell_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\status_sell_icon.png', 0)
status_empty_icon = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\status_empty_icon.png', 0)

status_buy_button = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\status_buy_button.png', 0)
height, width = status_buy_button.shape
status_buy_button_dimensions = [int(height),int(width)]


offer_increase = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\offer_increase.png', 0)
offer_decrease = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\offer_decrease.png', 0)
offer_button_dimensions = [35,25]

offer_confirm = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\offer_confirm.png', 0)


chat_window_dimensions = [519,142]
chat_buy_anchor = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\lib\merchant_bot\anchor\chat_buy_anchor02.png', 0)