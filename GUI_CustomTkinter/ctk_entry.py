from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Entry CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("600x350")

def hello():
    my_label.configure(text=my_button.cget("text"))


my_label = customtkinter.CTkLabel(root, text="", font=("helvetica", 24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root, 
    placeholder_text="Enter your name",
    height=50,
    width=200,
    font=("helvetica", 18),
    corner_radius=50,
    text_color="green",
    placeholder_text_color="darkblue",
    fg_color=("blue", "lightblue"),
    state="normal")
my_entry.pack(pady=20)

def submit():   
    my_label.configure(text=f'Hello {my_entry.get()}')
    my_entry.configure(state="disabled")
def clear():
    my_entry.configure(state="normal")
    my_entry.delete(0, END)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)


root.mainloop()


