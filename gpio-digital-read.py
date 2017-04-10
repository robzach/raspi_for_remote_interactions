"""
Simple GPIO digital read for RPi

Does digital read of physical pin 22 (GPIO pin 6)
and writes value to physical pin 16 (GPIO pin 4)

not currently reading keyboard input; getch doesn't seem to be working.

Robert Zacharias 4-10-17

"""


import RPi.GPIO as G
import time
import getch

G.setmode(G.BOARD)

G.setup(16, G.OUT)
G.setup(22, G.IN)

while(True):
        if (G.input(22)):
                G.output(16, True)
                print("digital read 22 HIGH")
        else:
                G.output(16, False)
                print("digital read 22 LOW")
        char = getch.getch()
        if char == "q":
                print("quitting and resetting pins")
                G.cleanup()
                exit()
        time.sleep(0.1)
