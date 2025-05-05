from tkinter import *

window = Tk()
window.geometry("500x500+600+400")
#option : Sticky, colunm, row, columnspan, rowspan, padx, pady, ipadx, ipady
#sticky : Atas : n, bawah : s, Kiri : w, Kanan : e


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)

window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)

btn1 = Button(text="Button1")
btn2 = Button(text="Button2")
btn3 = Button(text="Button3")
btn4 = Button(text="Button4")

btn1.grid(column=0,row=0, sticky="wens")
btn2.grid(column=1,row=0, sticky="wens")
btn3.grid(column=2,row=0, columnspan=3, sticky="wens")
btn4.grid(column=0,row=1, columnspan=5, sticky="wens")

window.title("My Tkinter Lyout")
window.mainloop()