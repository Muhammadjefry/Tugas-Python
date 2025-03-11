from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("The Switch widget CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x300")

# Create function
def switcher():
    my_label.configure(text=switch_var.get())


def clicker():
    #my_switch.deselect()
    #my_switch.select()
    my_switch.toggle()

#create a StringVar
switch_var = StringVar(value="on")
#create switch
my_switch = customtkinter.CTkSwitch(root, text="Switch", command=switcher,
    variable=switch_var, onvalue="on", offvalue="off",
    #width=200,
    #height=100,
    switch_height=25,
    switch_width=200,
    #corner_radius=10,
    border_color="orange",
    border_width=5,
    fg_color="red",
    progress_color="green",
    button_color="pink",
    button_hover_color="yellow",
    font=("helvetica", 18),
    text_color="blue",
    state="normal",
    
    )
my_switch.pack(pady=40)

#create label
my_label = Label(root, text="")
my_label.pack(pady=10)

#Create a Button
my_button = customtkinter.CTkButton(root, text="Click Me !", command=clicker)
my_button.pack(pady=20)

root.mainloop()