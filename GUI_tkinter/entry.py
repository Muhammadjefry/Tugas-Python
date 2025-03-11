from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    mylabel1 = Label(root, text="hello" + e.get())
    mylabel1.pack()

myButton = Button(root, text="clik me!", command=myClick, fg="blue")

myButton.pack()

root.mainloop()


