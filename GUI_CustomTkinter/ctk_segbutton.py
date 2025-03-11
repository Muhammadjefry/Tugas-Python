from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("SegButton CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x300")

def clicker(value):
    my_label.configure(text=f'Hello {value}')

#Our Button Values
my_values = ["Jhon", "April", "Wes"]
#Create the button
my_seg_button = customtkinter.CTkSegmentedButton(root, values=my_values, command=clicker,
    width=300,
    height=100,
    font=("helvetica", 18),
    corner_radius=3,
    border_width=3,
    fg_color="red",
    selected_color="green",
    selected_hover_color="purple",
    unselected_color="pink",
    unselected_hover_color="orange",
    text_color="yellow",
    state="normal",
    text_color_disabled="blue",
    dynamic_resizing=False,
    
    
    
    
    )

my_seg_button.pack(pady=40)

#set default selectoin
# my_seg_button.set("Jhon")

#Label
my_label = customtkinter.CTkLabel(root, text="", font=("helvetica", 18))
my_label.pack(pady=20)


root.mainloop()