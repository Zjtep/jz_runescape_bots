import pyautogui
# from core import RandTime
import RandTime
import random
import win32api, win32con
import time

def click():
    #autopy.mouse.click()
    # pyautogui.moveTo(100, 200)
    pyautogui.mouseDown(button='left')
    RandTime.randTime(0,1,0,0,2,9)#time between click
    # RandTime.randTime(0, 0, 0, 0, 0, 1)  # time between click
    pyautogui.mouseUp(button='left')

def moveTo(x,y,**kwargs):
    # if duration:

    if ("speed" in kwargs):
        speed = kwargs['speed']

    speed = 0.5
        # duration_of_move=duration
    # print x,y
    curr_x, curr_y = pyautogui.position()
    # calculates the distance from current position to target position
    distance = int(((x - curr_x) ** 2 + (y - curr_y) ** 2) ** speed)
    # calculates a random time to make the move take based on the distance
    duration_of_move = (distance * random.random() / 2000) + speed
    # move the mouse to our position and takes the time of our duration just
    # calculated
    pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)
    # pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeOutElastic)

def quickMoveTo(x,y,speed):
    # if duration:

        # duration_of_move=duration
    # print x,y
    curr_x, curr_y = pyautogui.position()
    # calculates the distance from current position to target position
    distance = int(((x - curr_x) ** 2 + (y - curr_y) ** 2) ** speed)
    # calculates a random time to make the move take based on the distance
    duration_of_move = (distance * random.random() / 2000) + speed
    # move the mouse to our position and takes the time of our duration just
    # calculated
    pyautogui.moveTo(x, y, duration_of_move)
    # pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeOutElastic)


def moveToRadius(coord):
    x = random.randint(coord[0],coord[2])
    y= random.randint(coord[1],coord[3])

    speed = 0.5
        # duration_of_move=duration
    # print x,y
    curr_x, curr_y = pyautogui.position()
    # calculates the distance from current position to target position
    distance = int(((x - curr_x) ** 2 + (y - curr_y) ** 2) ** speed)
    # calculates a random time to make the move take based on the distance
    duration_of_move = (distance * random.random() / 2000) + speed
    # move the mouse to our position and takes the time of our duration just
    # calculated
    pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)

def clickRadius(coord):
    x = random.randint(coord[0]+6,coord[2]-6)
    y= random.randint(coord[1]+6,coord[3]-6)

    speed = 0.5
        # duration_of_move=duration
    # print x,y
    curr_x, curr_y = pyautogui.position()
    # calculates the distance from current position to target position
    distance = int(((x - curr_x) ** 2 + (y - curr_y) ** 2) ** speed)
    # calculates a random time to make the move take based on the distance
    duration_of_move = (distance * random.random() / 2000) + speed
    # move the mouse to our position and takes the time of our duration just
    # calculated
    pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)
    click()


def win32Click(x,y):
    print x, y
    win32api.SetCursorPos((x,y))
    RandTime.randTime(0, 0, 0, 0, 0, 28)  # time between click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    RandTime.randTime(0, 0, 0, 0, 0,28)  # time between click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def win32MoveTo(x,y):
    print x, y
    win32api.SetCursorPos((x, y))

def win32MoveToRadius(coord):
    x = random.randint(coord[0],coord[2])
    y= random.randint(coord[1],coord[3])
    # print coord
    # print x,y
    win32api.SetCursorPos((x, y))

def win32ClickRadius(coord):
    x = random.randint(coord[0],coord[2])
    y= random.randint(coord[1],coord[3])
    # print coord
    # print x,y
    win32api.SetCursorPos((x, y))
    RandTime.randTime(0, 0, 0, 0, 0, 28)  # time between click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    RandTime.randTime(0, 0, 0, 0, 0,28)  # time between click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def randCoord(x):
    # item = 36
    return(random.randint(10, x))
