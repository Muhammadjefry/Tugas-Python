import time
from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
from playsound import playsound
import multiprocessing
from datetime import datetime
from threading import *


hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24']

minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59']

ringtones_list = ['Danger', 'Chiken', 'Danger_low', 'Slow', 'Bird', 'Mom_calling']

ringtones_path = {
    'Danger': 'C:\\xampp\\htdocs\\Python\\Alarm\\Ringtones/sound1.wav',
    'Chiken': 'C:\\xampp\\htdocs\\Python\\Alarm\\Ringtones/sound2.wav',
    'Danger_low': 'C:\\xampp\\htdocs\\Python\\Alarm\\Ringtones/sound3.wav',
    'Slow': 'C:\\xampp\\htdocs\\Python\\Alarm\\Ringtones/sound4.mp3',
    'Bird': 'C:\\xampp\\htdocs\\Python\\Alarm\\Ringtones/sound5.mp3',
    'Mom_calling': 'C:\\xampp\\htdocs\\Python\\Alarm\\Ringtones/sound6.mp3',
}

class AlarmClock:
    def __init__(self, root):
        
        self.window = root
        self.window.geometry("680x420+0+0")
        self.window.title("Alarm Tkinter")
        self.window.resizable(width = False, height = False)

        # Background image .
        self.bg_image = ImageTk.PhotoImage(file="C:\\xampp\\htdocs\\Python\\Alarm\\Images\\images_1.jpeg")
        self.background = Label(self.window, image=self.bg_image)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)

        # first window
        self.display = Label(self.window, font=('Helvetica', 34), 
        bg='black', fg = 'yellow')
        self.display.place(x=100,y=150)
        self.show_time()

        set_button = Button(self.window, text="Set Alarm", 
        font=('Helvetica',15), bg="red", fg="white", 
        command=self.set_alarm, cursor="hand2")
        set_button.place(x=270, y=220)
        
            # The Cancel Button: For cancel the alarm.
        cancel_button = Button(self.window, 
        text='Close', font=('Helvetica',15), bg="gray", 
        fg="white", cursor="hand2", command=self.window.destroy)
        cancel_button.place(x=285, y=270)
        
        # Show the current time 
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
        self.display.config(text = current_time)
        self.display.after(100, self.show_time)
        
    def set_alarm(self):
        self.alarm_window = Tk()
        self.alarm_window.title("Set Alarm")
        self.alarm_window.geometry("680x420+200+200")
        
        self.background = Label(self.alarm_window, fg="black", bg="black")
        # Hour Label
        hours_label = Label(self.alarm_window, text="Hours", 
        font=("helvetica",18), )
        hours_label.place(x=150, y=50)

        #  Minute Label
        minute_label = Label(self.alarm_window, text="Minutes", 
        font=("helvetica",18))
        minute_label.place(x=450, y=50)

        # Hour Combobox
        self.hour_var = StringVar()
        self.hour_combo = ttk.Combobox(self.alarm_window, 
        width=10, height=10, textvariable=self.hour_var, 
        font=("helvetica",15), )
        self.hour_combo['values'] = hours_list
        self.hour_combo.current(0)
        self.hour_combo.place(x=150,y=80)

        # Minute Combobox
        self.minute_var = StringVar()
        self.minute_combo = ttk.Combobox(self.alarm_window, 
        width=10, height=10, textvariable=self.minute_var, 
        font=("helvetica",15))
        self.minute_combo['values'] = minutes_list
        self.minute_combo.current(0)
        self.minute_combo.place(x=450,y=80)

        # Ringtone Label.
        ringtone_label = Label(self.alarm_window, text="Ringtones", 
        font=("helvetica",18))
        ringtone_label.place(x=150, y=130)

        # Ringtone Combobox(Choose the ringtone).
        self.ringtone_var = StringVar()
        self.ringtone_combo = ttk.Combobox(self.alarm_window, 
        width=15, height=10, textvariable=self.ringtone_var, 
        font=("helvetica",15), background="yellow",
        )
        self.ringtone_combo['values'] = ringtones_list
        self.ringtone_combo.current(0)
        self.ringtone_combo.place(x=150,y=160)

        # Create an entry for setting a message
        message_label = Label(self.alarm_window, text="Message", 
        font=("helvetica",18))
        message_label.place(x=150, y=210)

        self.message_var = StringVar()
        self.message_entry = Entry(self.alarm_window, 
        textvariable=self.message_var, font=("helvetica",14), width=30)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(x=150, y=240)

        # Test Button: For testing the ringtone music.
        test_button = Button(self.alarm_window, text='Test', 
        font=('Helvetica',15), bg="blue", fg="white", cursor="hand2", command=self.preview_alarm)
        test_button.place(x=150, y=300)

        # The Cancel Button: For cancel the alarm.
        cancel_button = Button(self.alarm_window, 
        text='Cancel', font=('Helvetica',15), bg="gray", 
        fg="white", cursor="hand2", command=self.alarm_window.destroy)
        cancel_button.place(x=390, y=300)

        # The Start Button: For set the alarm time
        start_button = Button(self.alarm_window, text='Start',
        font=('Helvetica',15), bg="green", fg="white", cursor="hand2", command=self._threading)
        start_button.place(x=490, y=300)

        self.alarm_window.mainloop()
        
    def preview_alarm(self):
        process = multiprocessing.Process(target=playsound, 
        args=(ringtones_path[self.ringtone_combo.get()],))
        process.start()
        messagebox.showinfo('Playing...', 'press ENTER to stop playing')
        process.terminate()

     # Method for creating a thread
    def _threading(self):
        x = Thread(target=self.save_alarm)
        x.start()
        
    #Looping Sound
    def save_alarm(self):
        alarm_time = f"{self.hour_combo.get()}:{self.minute_combo.get()}"
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        sound_name = self.ringtone_combo.get()
        message = self.message_entry.get()
        
        
        
        try:
            while True:
                # The current time is in 24 hour format
                current_time = datetime.now()
                # Converting the current time into hours and minutes
                current_time_format = current_time.strftime("%H:%M")
                if current_time_format == alarm_time:
                    process = multiprocessing.Process(target=playsound, 
                    args=(ringtones_path[sound_name],))
                    process.start()
                    
                    
                    while True:
                        if messagebox.showinfo("Alarm", f"{message}, It's {alarm_time}"):
                        # Stop the sound when "OK" is pressed
                            process.terminate()
                            break
                    break
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")
            

if __name__ == "__main__":
    root = Tk()
    obj = AlarmClock(root)
    root.mainloop()