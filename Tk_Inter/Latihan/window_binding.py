from tkinter import *


# window = Tk()
# def eventButton(event):
#     print(event)
    
window = Tk()
def eventKey(event):
    print(event)

window.bind("<Key>", eventKey)
# window.bind("<Buttton>", eventButton)
window.title("My Tkinter Window")

window.mainloop()