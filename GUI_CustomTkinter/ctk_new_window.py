from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Text Box CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("400x200")

def new():
    new_window = customtkinter.CTkToplevel(root, fg_color="white")
    new_window.title("This is a New Window")
    new_window.geometry("400x200")
    new_window.resizable(False, True) # width, height

    def close():
        new_window.destroy()
        new_window.update()
    
    #close teh wondow
    new_button = customtkinter.CTkButton(new_window, text="Close window", command=close)    
    new_button.pack(pady=20)
    
my_button = customtkinter.CTkButton(root, text="Open New window!", command=new)
my_button.pack(pady=20)

root.mainloop()