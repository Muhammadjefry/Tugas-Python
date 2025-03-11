import time
from tkinter import *
from PIL import ImageTk
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

        # Background 
        self.bg_image = ImageTk.PhotoImage(file="C:\\xampp\\htdocs\\Python\\Alarm\\Images\\images_2.jpeg")
        self.background = Label(self.window, image=self.bg_image)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)

        # Display Label shows 
        self.display = Label(self.window, font=('Helvetica', 34), 
        bg='black', fg = 'yellow', borderwidth=3, relief="solid")
        self.display.place(x=100,y=150)

        self.show_time()
                
        #  show the current time in the first window
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
        self.display.config(text = current_time)
        self.display.after(100, self.show_time)
            

if __name__ == "__main__":
    root = Tk()
    obj = AlarmClock(root)
    root.mainloop()