import pyautogui
import RandTime
import random
import time
from time import sleep
from random import randint
import math

from autopy.mouse import (
    move, click, get_pos,
    LEFT_BUTTON,
    RIGHT_BUTTON,
    CENTER_BUTTON
)

def click():
    #autopy.mouse.click()
    # pyautogui.moveTo(100, 200)
    pyautogui.mouseDown(button='left')
    RandTime.randomTime(2, 7)
    # RandTime.randTime(0, 0, 0, 0, 0, 1)  # time between click
    pyautogui.mouseUp(button='left')

def right_click():
    #autopy.mouse.click()
    # pyautogui.moveTo(100, 200)
    pyautogui.mouseDown(button='right')
    RandTime.randomTime(2, 7)
    # RandTime.randTime(0, 0, 0, 0, 0, 1)  # time between click
    pyautogui.mouseUp(button='right')

def move_to_radius(coord):
    coord = list(coord)

    x = random.randint(coord[0]+6,coord[2]+coord[0]-6)
    y = random.randint(coord[1]+6,coord[3]+coord[1]-6)

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
    coord = list(coord)

    x = random.randint(coord[0]+6,coord[2]+coord[0]-6)
    y = random.randint(coord[1]+6,coord[3]+coord[1]-6)

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


def move_mouse_to_click(x, y):
    # takes current mouse location and stores it
    while(True):
        try:
            curr_x, curr_y = pyautogui.position()
            # calculates the distance from current position to target position
            distance = int(((x - curr_x)**2 + (y - curr_y)**2)**0.5)
            # calculates a random time to make the move take based on the distance
            duration_of_move = (distance * random.random() / 2000) + 0.5
            # move the mouse to our position and takes the time of our duration just
            # calculated
            pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)
            click()
            #pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeOutElastic)
            break
        except:
            print('paused for 10 seconds')
            time.sleep(10)

def move_mouse_to(x, y):
    # takes current mouse location and stores it
    while(True):
        try:
            curr_x, curr_y = pyautogui.position()
            # calculates the distance from current position to target position
            distance = int(((x - curr_x)**2 + (y - curr_y)**2)**0.5)
            # calculates a random time to make the move take based on the distance
            duration_of_move = (distance * random.random() / 2000) + 0.5
            # move the mouse to our position and takes the time of our duration just
            # calculated
            pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeInOutQuad)
            #pyautogui.moveTo(x, y, duration_of_move, pyautogui.easeOutElastic)
            break
        except:
            print('paused for 10 seconds')
            time.sleep(10)

import win32api
import win32con

def scroll(value= 100):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0 , value, 0)
        return


def random_point(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    point = (x,y)
    return(point)


#https:////github.com/mondeja/autopy_mouse.git
class HumanMouse:
    """
    Main class for human mouse performance.
    Before clicks moves to point.

    :param mouse_speed: Mouse velocity
        (optional, default == 18)
    :type mouse_speed: int/float

    :param gravity: If the number is larger,
        grater uniformity of movement
        (optional, default == 60)
    :type gravity: inf/float

    :param wind: aleatority of movement
        (optional, default == 60)
    :type wind: int/float

    :param target_error: Error in target
        objetive (optional, default == 500)s
        before achieve it without error
    :type target_error: int/float
    """

    def __init__(self, mouse_speed=18, gravity=60,
                 wind=60, target_error=500):
        self.mouseSpeed = mouse_speed
        self.gravity = gravity
        self.wind = wind
        self.targetError = target_error

    def move(self, x, y):
        """Human mouse movement """
        startCoords = get_pos()
        coordsAndDelay = self._calcCoordsAndDelay(startCoords,
                                                  (x, y))
        print coordsAndDelay
        print x,y
        for x, y, delay in coordsAndDelay:
            move(int(x), int(y))
            sleep(delay / 1000)
        move_mouse_to(x,y)


    def move_radius(self,coord):
        """Human mouse movement """
        x = random.randint(coord[0] + 6, coord[2] + coord[0] - 6)
        y = random.randint(coord[1] + 6, coord[3] + coord[1] - 6)

        print x,y
        startCoords = get_pos()
        coordsAndDelay = self._calcCoordsAndDelay(startCoords,
                                                  (x, y))
        for x, y, delay in coordsAndDelay:
            move(int(x), int(y))
            sleep(delay / 1000)
        move_mouse_to(x, y)

    def click(self, x, y, button=LEFT_BUTTON,
              clicks=1, interval=0):
        """Perform a number of clicks after
        human mouse movement

        :param button: Mouse button to use
            on the click. Valid types:
            (1, 2, 3, 'left', 'right', 'middle')
            (optional, default == 1)
        :type button: int/str

        :param clicks: Number of clicks
            (optional, default == 1)
        :type clicks: int

        :param interval: Time for sleep
            between clicks
            (optional, default == 0)
        :type interval: int/float
        """
        self.move(x, y)

        for c in range(clicks):
            click(button)
            if clicks > 1 and interval > 0:
                sleep(interval)

    def double_click(self, x, y, pause=.1, **kwargs):
        """Perform a classic double click
        after human mouse movement

        :param pause: Time to sleep between
            first and second click
            (optional, default == .1)
        :type pause: int/float
        """
        self.move(x, y)
        click(x, y, **kwargs)
        sleep(pause)
        click(x, y, **kwargs)

    def _calcCoordsAndDelay(self, startCoords, endCoords):
        """Internal function for calculate
        coordinates and delay to perform
        human mouse movement"""

        veloX, veloY = (0, 0)
        coordsAndDelay = []
        xs, ys = startCoords
        xe, ye = endCoords
        totalDist = math.hypot(xs - xe, ys - ye)

        self._windX = 0
        self._windY = 0

        while True:
            veloX, veloY = self._calcVelocity((xs, ys), (xe, ye), veloX, veloY, totalDist)
            xs += veloX
            ys += veloY

            w = round(max(randint(0, max(0, round(100 / self.mouseSpeed) - 1)) * 6, 5) * 0.9)
            coordsAndDelay.append((xs, ys, w))

            if math.hypot(xs - xe, ys - ye) < 1:
                break

        if round(xe) != round(xs) or round(ye) != round(ys):
            coordsAndDelay.append((round(xe), round(ye), 0))

        return coordsAndDelay

    def _calcVelocity(self, curCoords, endCoords, veloX, veloY, totalDist):
        xs, ys = curCoords
        xe, ye = endCoords
        dist = math.hypot(xs - xe, ys - ye)
        self.wind = max(min(self.wind, dist), 1)

        maxStep = None
        D = max(min(round(round(totalDist) * 0.3) / 7, 25), 5)
        rCnc = randint(0, 5)

        if rCnc == 1:
            D = 2

        if D <= round(dist):
            maxStep = D
        else:
            maxStep = round(dist)

        if dist >= self.targetError:
            self._windX = self._windX / math.sqrt(3) + (randint(0, round(self.wind) * 2) - self.wind) / math.sqrt(5)
            self._windY = self._windY / math.sqrt(3) + (randint(0, round(self.wind) * 2) - self.wind) / math.sqrt(5)
        else:
            self._windX = self._windX / math.sqrt(2)
            self._windY = self._windY / math.sqrt(2)

        veloX = veloX + self._windX
        veloY = veloY + self._windY

        if (dist != 0):
            veloX = veloX + self.gravity * (xe - xs) / dist
            veloY = veloY + self.gravity * (ye - ys) / dist

        if math.hypot(veloX, veloY) > maxStep:
            randomDist = maxStep / 2.0 + randint(0, math.floor(round(maxStep) / 2))
            veloMag = math.sqrt(veloX * veloX + veloY * veloY)
            veloX = (veloX / veloMag) * randomDist
            veloY = (veloY / veloMag) * randomDist

        return (veloX, veloY)




