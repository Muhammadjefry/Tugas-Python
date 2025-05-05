from tkinter import *

window = Tk()
window.geometry("500x400+500+100")

def btnClicked():
    #myEntry.delete(0,END)
    #print(myEntry.get())
    #myEntry.icursor(4)
    #print(myEntry.index(INSERT))
    #myEntry.insert(END,"Tambahan ")
    #myEntry.select_adjust(5)
    #myEntry.select_clear()
    #myEntry.select_from(0)
    #myEntry.select_to(5)
    #myEntry.select_clear()
    myEntry.select_range(0,5)

myEntry = Entry(window)
myEntry.pack()

myBtn = Button(text="My Button", command=btnClicked)
myBtn.pack()

window.title("My Tkinter EntryMethod")
window.mainloop()