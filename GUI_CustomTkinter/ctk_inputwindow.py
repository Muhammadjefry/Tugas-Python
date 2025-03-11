from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Text Box CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x300")

def input():
    dialog = customtkinter.CTkInputDialog(text="What is your name?", title="Hello There",
    fg_color="white",
    button_fg_color="red",
    button_hover_color="blue",
    button_text_color="green",
    entry_fg_color="red",
    entry_border_color="blue",
    entry_text_color="black"
    )
    thing = dialog.get_input()
    if thing:
        my_label.configure(text=f"Hello {thing} !")
    else:
        my_label.configure(text="You Forgot to type Anything !")

# Create a Button
my_button = customtkinter.CTkButton(root, text="Click Me !", command=input)
my_button.pack(pady=20)


#create a label
my_label = Label(root, text="")
my_label.pack(pady=10)

root.mainloop()