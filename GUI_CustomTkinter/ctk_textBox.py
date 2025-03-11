from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Text Box CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x300")

thing = ''

def delete():
    my_text.delete('0.0', END)

def copy():
    global thing
    thing = my_text.get('0.0', END)

def paste():
    if thing:
        my_text.insert('end', thing)
    else:
        my_text.insert('end', 'There is nothing to paste!')

my_text = customtkinter.CTkTextbox(root)
my_text.pack(pady=20)

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_frame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_frame, text="Paste", command=paste)

delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1, padx=20)
paste_button.grid(row=0, column=2)

root.mainloop()