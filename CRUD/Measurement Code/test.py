import serial
from tkinter import *
import tkinter as tk

# coomPort = 'COM6'
ser = serial.Serial('COM6', baudrate = 9600, timeout = 1)

def turnOnLED():
    ser.write(b'o')
    
def turnOffLED():
    ser.write(b'x')
    
root = tk.Tk()
root.title('LED Control')

btn_on = tk.Button(root, text='TURN ON', width=10, command=turnOnLED)
btn_on.grid(row=0, column=0)
btn_off = tk.Button(root, text='TURN OFF', width=10, command=turnOffLED)
btn_off.grid(row=1, column=0)


root.geometry("350x350")
root.mainloop()
