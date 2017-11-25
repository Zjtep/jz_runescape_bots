import pyautogui
import time
import random
print "Randomized Mouse Started."
destx = 444;
desty = 631;
x, y = pyautogui.position() # Current Position
moves = random.randint(2,4)
pixelsx = destx-x
pixelsy = desty-y
if moves >= 4:
        moves = random.randint(2,4)
avgpixelsx = pixelsx/moves
avgpixelsy = pixelsy/moves
print "Pixels to be moved X: ", pixelsx," Y: ",pixelsy, "Number of mouse movements: ", moves, "Avg Move X: ", avgpixelsx, " Y: ", avgpixelsy

while moves > 0:
        offsetx = (avgpixelsx+random.randint(-8, random.randint(5,10)));
        offsety = (avgpixelsy+random.randint(-8, random.randint(5,10)));
        print x + offsetx, y + offsety, moves
        pyautogui.moveTo(x + offsetx, y + offsety, duration=0.2)
        moves = moves-1
        avgpixelsx = pixelsx / moves
        avgpixelsy = pixelsy / moves