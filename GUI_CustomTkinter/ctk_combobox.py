from tkinter import *
import customtkinter
import ttkbootstrap as ttk

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("ComboBox CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x450")


def color_picker(choice):    
    output_label.configure(text=choice, text_color=choice)

def color_picker2():    
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


def color_picker_yellow(): 
    my_combo.set("Yellow")   
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


my_label = customtkinter.CTkLabel(root, text="Pick A Color", font=("helvetica", 18))
my_label.pack(pady=40)

#set the optiont our combobox
colors = ["Red", "Green", "Blue"]
#create combo box
my_combo = customtkinter.CTkComboBox(root, values=colors,
    height=50,
    width=200,
    font=("helvetica", 18),
    dropdown_font=("helvetica", 18),
    corner_radius=50,
    border_width=2,
    border_color="red",
    button_color="red",
    button_hover_color="green",
    dropdown_hover_color="green",
    dropdown_fg_color="blue",
    dropdown_text_color="orange",
    text_color="silver",
    hover=True,
    justify="center",
    state="normal",
    )
my_combo.pack(pady=0)



#create A Button 
my_button = customtkinter.CTkButton(root, text="Pick A Color", command=color_picker2)
my_button.pack(pady=10)

#Yellow Button
yellow_button = customtkinter.CTkButton(root, text="Yellow", command=color_picker_yellow)
yellow_button.pack(pady=10)

#create output label
output_label = customtkinter.CTkLabel(root, text="hello worl", font=("helvetica", 18))
output_label.pack(pady=10)
root.mainloop()


