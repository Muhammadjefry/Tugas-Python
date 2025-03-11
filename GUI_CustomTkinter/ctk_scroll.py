from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Scrool CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x300")

#create a scollable frame
my_frame = customtkinter.CTkScrollableFrame(root,
    orientation="vertical",
    width=300,
    height=200,
    label_text="Scrollable Frame",
    label_font=("helvetica", 18),
    label_fg_color="yellow",
    label_text_color="red",
    label_anchor="center",
    border_width=3,
    border_color="green",
    fg_color="red",
    scrollbar_fg_color="blue",
    scrollbar_button_color="pink",
    scrollbar_button_hover_color="yellow",
    corner_radius=20,
    )
my_frame.pack(pady=40)


for x in range(20):
    customtkinter.CTkButton(my_frame, text="This is a Button", font=("helvetica", 18)).pack(pady=10)

root.mainloop()