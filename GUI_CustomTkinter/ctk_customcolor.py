from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("red.json")  # Themes: blue (default), dark-blue, green

#Turn of scalling
customtkinter.deactivate_automatic_dpi_awareness()
#Scale Window
customtkinter.set_window_scaling(1.5)
#Scale Widget
customtkinter.set_widget_scaling(1.5)


# root = Tk()
root = customtkinter.CTk()

root.title("Ligh Dark CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x450")

mode = "dark"
def change_colors(choice):
    customtkinter.set_default_color_theme(choice)
def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        #clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "This is Light mode")
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
        #clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "This is Dark mode")

my_text = customtkinter.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Change light/dark", command=change)
my_button.pack(pady=20)

colors = ["blue", "dark-blue", "green"]

my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_colors)
my_option.pack(pady=10)

my_progress = customtkinter.CTkProgressBar(root, orientation="horizontal",)
my_progress.pack(pady=20 )

root.mainloop()