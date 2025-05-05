from tkinter import *

window = Tk()
window.geometry("500x400+500+100")

label1 = Label(text="label1",width=40, height=20, bg="#ff0000",fg="#fff")
label1.pack()
window.title("My Tkinter Label")
window.mainloop()