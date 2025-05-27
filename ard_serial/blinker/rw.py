import serial
import time
import re


def Data(interval, count):

    sp = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
    for i in interval:
        sp.write(i.encode() + "\n")
    for i in count:
        sp.write(count.encode() + "\n") 
    time.sleep(0.2)
    print(interval, count)
