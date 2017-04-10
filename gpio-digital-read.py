"""
Simple GPIO digital read for RPi

Does digital read of physical pin 22 (GPIO pin 6)

Robert Zacharias 2-27-17

"""


import RPi.GPIO as G
import time

G.setmode(G.BOARD)

G.setup(22, G.IN)

while(True):
        if (G.input(22)):
                print("digital read 22 HIGH")
        else:
                print("digital read 22 LOW")
        time.sleep(1)


"""
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
