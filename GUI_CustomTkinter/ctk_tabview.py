from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Tab View CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x300")

def clicker():
    my_button.configure(text="You clicked the tab button")

#create tab view
my_tab = customtkinter.CTkTabview(root,
    width=600,
    height=250,
    corner_radius=10,
    fg_color="silver",
    segmented_button_fg_color="red",
    segmented_button_selected_color="green",
    segmented_button_selected_hover_color="pink",
    segmented_button_unselected_hover_color="purple",
    segmented_button_unselected_color="yellow",
    text_color="red",
    state="normal",
    command=clicker,
    #anchor="w",
    )
my_tab.pack(pady=10)

#create tabs
tab_1 = my_tab.add("Tab 1")
tab_2 = my_tab.add("Tab 2")

#put stuff in tabs
my_button = customtkinter.CTkButton(tab_1, text="Click Me !")
my_button.pack(pady=40)

root.mainloop()