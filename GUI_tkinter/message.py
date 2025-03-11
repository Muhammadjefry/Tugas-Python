from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message GUI")
# root.iconbitmap('c:/Users/acer/Downloads/python.ico')

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
   response = messagebox.askyesno("This is a Popup", "Hello World!")
   Label(root, text=response).pack()
#    if response == 1:
#       Label(root, text="You clicked Yes!").pack()
#    else:
#       Label(root, text="You clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()


