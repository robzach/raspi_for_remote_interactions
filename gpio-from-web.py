"""
Simple GPIO test for RPi from web data

Uses two LEDs, one on physical pin 16 and one on physical pin 18

Robert Zacharias 2-27-17

Having some trouble: even though I've updated the webpage value, and 
even though the "requests" module isn't supposed to do any caching,
it keeps retreiving the same value from the remote site (incorrectly).

"""

import RPi.GPIO as G
import time
import getch
import requests

G.setmode(G.BOARD)

G.setup(16, G.OUT)
G.setup(18, G.OUT)

r = requests.get('http://www.rzach.me/15.txt') # this page only contains a single number
num = int(r.text)
print "num retrieved =", num

# blinks the leds based on the value retrieved from the remote page
for i in range(num):
	G.output(16, True)
	G.output(18, False)
	time.sleep(0.1)
	G.output(16, False)
	G.output(18, True)
	time.sleep(0.1)

print("quitting and resetting pins")
G.cleanup()
exit()