from time import sleep
from picamera import PiCamera
from datetime import datetime

cam = PiCamera()
cam.start_preview(fullscreen=False,window=(40,40,320,240))
sleep(2)

for filename in cam.capture_continuous('/home/pi/Desktop/snow/img{timestamp:%Y%m%d-%H%M%S}.jpg'):
    print('captured %s' % filename)
    sleep(30)
