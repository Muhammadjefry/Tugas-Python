from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title("Checkbox CustomTKinter")
root.iconbitmap("C:\\xampp\\htdocs\\Python\\GUI_CustomTkinter\\icon.ico")
root.geometry("700x350")

def cliker():
    my_progressbar.step()
    my_label.configure(text= (int(my_progressbar.get()*100)))

def start():
    my_progressbar.start()
    
def stop():
    my_progressbar.stop()

my_progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal",
    width=300,
    height=50,
    corner_radius=20,
    border_width=2,
    border_color="red",
    fg_color="green",
    progress_color="blue",
    mode="determinate",
    determinate_speed=5,
    indeterminate_speed=.5,                                          
                                              
                                              
    )
my_progressbar.pack(pady=40)

#set the default prograeesbar
my_progressbar.set(0)


my_button = customtkinter.CTkButton(root, text="Click Me!", command=cliker)
my_button.pack(pady=10)

start_button = customtkinter.CTkButton(root, text="Start", command=start)
start_button.pack(pady=10)

stop_button = customtkinter.CTkButton(root, text="Stop", command=stop)
stop_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="", font=("helvetica", 18))
my_label.pack(pady=10)

root.mainloop()


