import serial
import time
from time import sleep

ser = serial.Serial('COM6', 9600, timeout=1)

col_data = input("Enter the column number: ")
ser.write(col_data.encode())
sleep(1) 
print("Data sent to Arduino:", col_data)
read_data = ser.readline().decode()
print("Data received from Arduino:", read_data.strip())