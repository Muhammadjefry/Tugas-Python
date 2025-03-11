from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Custom CustomTKinter")
root.iconbitmap('icon.ico')
root.geometry("600x350")

def hello():
    my_label.configure(text=my_button.cget("text"))

my_button = customtkinter.CTkButton(root, text="Hello World",
    command=hello,
    height=100,
    width=200,
    font=("helvetica", 24),
    text_color="white",
    fg_color="red",
    hover_color="blue",
    corner_radius=50,
    bg_color="black",
    border_width=10,
    border_color="yellow",
    state="normal")

my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)


root.mainloop()


