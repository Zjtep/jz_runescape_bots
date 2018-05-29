import pyautogui
import RandTime
import random


def click():
    #autopy.mouse.click()
    # pyautogui.moveTo(100, 200)
    pyautogui.mouseDown(button='left')
    RandTime.randomTime(2, 7)
    # RandTime.randTime(0, 0, 0, 0, 0, 1)  # time between click
    pyautogui.mouseUp(button='left')

def move_to_radius(coord):
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

def click_radius(coord):
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
