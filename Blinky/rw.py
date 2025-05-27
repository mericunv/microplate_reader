import serial
import time
import re


def Data(interval, count):
    sp = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    time.sleep(3)
    while sp.in_waiting > 0: ##dont progress until setup is complete
        buffer = sp.readline()
        print(buffer.decode())
        time.sleep(0.2)

    for i in interval:
     
        sp.write(i.encode())
    sp.write('\n'.encode()) #finish the sent data with linebreak
    time.sleep(1)
    for i in count:

        sp.write(i.encode()) 
    sp.write('\n'.encode())#finish the sent data with linebreak

    print("Sending ", interval, count)

    time.sleep(3) #im sure we dont need to wait for this long

    while sp.in_waiting > 0: ##loop to read stuff
        buffer = sp.readline()
        print(buffer.decode())
        time.sleep(0.2)
