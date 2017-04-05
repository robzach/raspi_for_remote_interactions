from escpos import *

p = printer.Serial(devfile=u'/dev/ttyUSB0', baudrate=38400, bytesize=8, timeout=1,\
                      parity='N', stopbits=1, xonxoff=False, dsrdtr=True)

p.open()
p.set(align='left')
p.text("here's text that's left-aligned\n")
p.set(align='right')
p.text("here's text that's right-aligned\n\n")

call = "I am writing something to you on this keyboard and hoping that you'll see it.\n\n\n"
response = "Yeah, that's looking pretty good to me. I am responding in a way that I think will be good.\n\n\n"

p.set(align='left')
p.block_text(call,columns=20)
p.set(align='right')
p.block_text(response,columns=20)
p.cut()
p.close()


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
