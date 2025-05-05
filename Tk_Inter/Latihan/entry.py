from tkinter import *

window = Tk()
window.geometry("500x400+500+100")

entry1 = Entry(window, bg="#ff0000",bd=10,cursor="clock", font=("Arial",9,"underline"),fg="#fff")
entry1.pack()
window.title("My Tkinter Label")
window.mainloop()