#simple serial printline test

import serial

with serial.Serial('/dev/ttyUSB0', 38400, timeout=1) as ser:
    ser.write(b'text')
    ser.write(b'10')
    ser.write('text no b')
    ser.write('10')


"""
ser = serial.Serial('/dev/ttyUSB0')
print(ser.name)
ser.write(10)
ser.write(b'hello')
ser.write(10)
ser.close()

"""
