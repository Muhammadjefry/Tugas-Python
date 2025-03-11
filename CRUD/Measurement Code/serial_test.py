import serial
import time

ser = serial.Serial('COM6', 9600, timeout=1)

for i in range(0, 1001, 2):
    
    data = f"{i},{i+1}"
    ser.write(data.encode())  
    print(f"Data: {data}")    
    time.sleep(1)             
