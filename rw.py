import serial
import time
import re


def Data(interval, count):

    #sp = serial.Serial('COM1', baudrate=9600, timeout=1)
    #sp.write(interval.encode() + "\n")
    #sp.write(count.encode() + "\n") 
    #time.sleep(0.2)
    print(interval, count)

##while True:
##    buffer = sp.readline()
##    print(buffer.decode())