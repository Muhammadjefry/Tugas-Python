from tkinter import *

window = Tk()
window.geometry("500x400+500+100")
# option : x, y, height, width, relx, rely, relwidth, anchor, bordermode, 
# anchor : Atas : N, bawah : S, Kiri : W, Kanan : E. NE, NW, SE, or SW
# nordermode : INSIDE, OUTSIDE

btn = Button(text="My Button")
#btn.place(x=100, y=0, width="100", height="100")
#btn.place(anchor=W,y=100 ,width="100", height="100")
btn.place( relwidth=0.2, relheight=0.1, relx=0.5, rely=0.5)


window.title("My Tkinter Lyout BTN")
window.mainloop()