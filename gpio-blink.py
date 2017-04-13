"""
Simple GPIO test for RPi

Uses two LEDs, one on physical pin 16 and one on physical pin 18

Robert Zacharias 2-27-17

"""


import RPi.GPIO as G
import time
import getch

G.setmode(G.BOARD)

G.setup(16, G.OUT)
G.setup(18, G.OUT)

while(True):
        print("16 on\t18 off")
        G.output(16, True)
        G.output(18, False)
        time.sleep(.05)

        print("16 off\t18 on")
        G.output(18, True)
        G.output(16, False)
        time.sleep(.05)

"""
while(True):
	char = getch.getch()
	# print(char)
	if char == "q":
		print("quitting and resetting pins")
		G.cleanup()
		exit()
	if char != "o":
		print("lights in one state")
		G.output(16, True)
		G.output(18, False)
	else:
		print("lights in the other state")
		G.output(18, True)
		G.output(16, False)

while(True):
	key = ord(getch())
	if key != 0:
		G.output(16, True)
		G.output(18, False)
	else:
		G.output(18, True)
		G.output(16, False)


while(True):
	G.output(16, True)
	G.output(18, False)
	time.sleep(1)
	G.output(18, True)
	G.output(16, False)
	time.sleep(1)
"""
