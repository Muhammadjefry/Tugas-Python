from tkinter import *

root = Tk()

def myClick():
    mylabel1 = Label(root, text="Look! I clicked a button")
    mylabel1.pack()

myButton = Button(root, text="clik me!", command=myClick, fg="blue", bg="red")

myButton.pack()

root.mainloop()


