from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Font CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("400x200")

def change():
    my_font.configure(underline=False, overstrike=False, size=22, slant="roman")
    
my_font = customtkinter.CTkFont(family="Helvetica", size=20,
    weight="bold", slant="italic", underline=True, overstrike=True) #weight bold/normal

my_label = customtkinter.CTkLabel(root, text="This is text", font=my_font)
my_label.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Click Me!", command=change)
my_button.pack(pady=10)

root.mainloop()