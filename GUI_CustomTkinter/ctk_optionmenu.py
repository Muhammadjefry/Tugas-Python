from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Image CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x450")

#create function
def color_picker(choice):
    my_label.configure(text=choice, text_color=choice)

def color_picker2():
    my_label.configure(text=my_option.get(), text_color=my_option.get())

def yellow():
    my_option.set("Yellow")
    my_label.configure(text=my_option.get(), text_color=my_option.get())

#set the options for our menu
colors = ["Red", "Green", "Blue"]

#create option menu
my_option = customtkinter.CTkOptionMenu(root, values=colors,
     #command=color_picker
    height=50,
    width=200,
    font=("helvetica", 18),
    fg_color="white",
    dropdown_font=("helvetica", 18),
    corner_radius=50,
    button_color="red",
    button_hover_color="green",
    dropdown_hover_color="green",
    dropdown_fg_color="blue",
    dropdown_text_color="orange",
    text_color="red",
    hover=True,
    anchor="center", #n-s-w-e-center
    state="normal",
    text_color_disabled="black",
    dynamic_resizing=False,)
my_option.pack(pady=40)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)

pick_button = customtkinter.CTkButton(root, text="Make Choiche", command=color_picker2)
pick_button.pack(pady=10)

yellow_button = customtkinter.CTkButton(root, text="Pick Yellow", command=yellow)
yellow_button.pack(pady=10)

root.mainloop()