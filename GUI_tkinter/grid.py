from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello, World!")
myLabel2 = Label(root, text="My Name is Jefry")
myLabel3 = Label(root, text="My Hobi Is ngoding")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=0, column=1)


root.mainloop()


