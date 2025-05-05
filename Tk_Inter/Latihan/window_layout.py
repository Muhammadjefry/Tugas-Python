from tkinter import *

window = Tk()
window.geometry("500x500+600+400")
#side : TOP (default), Bottom, Left, or Right.
#fill : NONE : (default), X (fiil horizontaly), Y (fiil vertically), BOTH,
#expand : YES(center) NO
#padx . pady , ipadx, ipady

btn1 = Button(text="Button1")
btn1.pack(expand=YES, fill = BOTH, padx = 50, pady = 50)

window.title("My Tkinter Layout")

window.mainloop()