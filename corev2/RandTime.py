import random
import time

#milsecionds
def randomTime(start,end):
    seconds = float(random.randint(start,end))/1000
    # print "Delay %s seconds" % seconds
    time.sleep(seconds)