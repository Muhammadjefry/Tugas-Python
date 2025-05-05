from tkinter import *

window = Tk()
window.geometry("500x400+500+100")

def btnclick1():
    print("Button Di Klik")

def btnclick2():
    btn1.invoke()
    
btn1 = Button(window,text="button 1" ,activebackground="#ff0000" ,activeforeground="#fff",command=btnclick1)
btn1.pack()
btn2 = Button(window,text="button 2" ,activebackground="#ff0000" ,activeforeground="#fff",command=btnclick2)
btn2.pack()
window.title("My Tkinter Lyout BTN")
window.mainloop()