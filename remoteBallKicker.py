"""
Skeleton of the operating loop of the two-station remote interaction system

needs to properly use requests with GET and POST messages to the remote
server to actually work right

4-13-17 first version

"""

import requests
import RPi.GPIO as G
import time
import threading

diagnostic = True

solenoidPin = 16
lightGatePin = 18

lastReceive = 0.0
lastTransmit = 0.0
ballwait = 0.5

# use these two lines from Larryville
GETurl = http://appname.heroku.com/whiteoakstatus
POSTurl = http://appname.heroku.com/larryvillepost

# use these two lines from White Oak
##GETurl = http://appname.heroku.com/larryvillestatus
##POSTurl = http://appname.heroku.com/whiteoakpost

G.setmode(G.BOARD)
G.setup(solenoidPin, G.OUT)
G.output(solenoidPin, False) # be sure it's off
G.setup(lightGatePin, G.IN)

if(diagnostic):
    print("G.setmode = G.BOARD")
    print("solenoidPin = ", solenoidPin)
    print("lightGatePin = ", lightGatePin)

def ballKicker():
    if(time.time() - lastReceive > ballwait):
        remoteMessage = requests.get(GETurl) # message should be a 0 or 1
        if(remoteMessage):
            G.output(solenoidPin, True)
            time.sleep(0.1)
            G.output(solenoidPin, False)

while(True):
    if (G.input(lightGatePin) and (time.time() - lastTransmit > 0.5):
        POSTmessage = requests.post(POSTurl, data = "1")
        lastTransmit = time.time()
    ballKicker()
