from escpos import *
import requests
#from StringIO import StringIO
import os, sys
#import Image

## THIS IS THE VERSION MODIFIED TO RUN ON MY MAC, NOT ACTUALLY WORKING AS IT'S SUPPOSED TO
## USE THE FIRST DEFINITION OF p AND FIRST DEFINITION OF img TO RUN ON THE PI

p = printer.Serial(devfile=u'/dev/ttyUSB0', baudrate=38400, bytesize=8, timeout=1,\
                      parity='N', stopbits=1, xonxoff=False, dsrdtr=True)

##p = printer.Serial(devfile=u'/dev/cu.usbserial', baudrate=38400, bytesize=8, timeout=1,\
##                      parity='N', stopbits=1, xonxoff=False, dsrdtr=True)

p.open()

#response = requests.get('http://www.rzach.me/picture.jpg')
#localpic = Image.open('/home/pi/Desktop/picture.jpg')
#localpic = open('/home/pi/Desktop/picture.jpg')
p.set(flip=True)
img = '/home/pi/Desktop/picture.jpg'
#img = '/Users/rz/Desktop/picture.jpg'
p.image(img, impl='graphics')
p.text('600x489 picture, takes a bit to transmit the data, but works best in graphics mode\n')
#localpic.close()

p.cut()
p.close()



"""
p.set(align='left')
p.text("here's text that's left-aligned\n")
p.set(align='right')
p.text("here's text that's right-aligned\n\n")

call = "I am writing something to you on this keyboard and hoping that you'll see it.\n"
response = "Yeah, that's looking pretty good to me. I am responding in a way that I think will be good.\n"

p.set(align='left')
p.block_text(call,columns=20)
p.set(align='right')
p.block_text(response,columns=20)
"""


program = """
from escpos import *

p = printer.Serial(devfile=u'/dev/ttyUSB0', baudrate=38400, bytesize=8, timeout=1,\
                      parity='N', stopbits=1, xonxoff=False, dsrdtr=True)

p.open()
p.text("here's how to do this:\n\n\n" + program)
#p.image("logo.gif")
p.qr("http://www.rzach.me/blog is a great address you might want to enter")
p.cut()
p.close()

"""

#p.image("logo.gif")
#p.qr("http://www.rzach.me/blog is a great address you might want to enter")
