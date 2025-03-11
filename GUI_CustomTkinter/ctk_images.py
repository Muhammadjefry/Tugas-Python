from tkinter import *
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Image CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("400x550")

my_image = customtkinter.CTkImage(light_image=Image.open("paw1.png"),
    dark_image=Image.open("paw1.png"),
    size=(200, 200)) #width, height

my_label = customtkinter.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=20)

root.mainloop()