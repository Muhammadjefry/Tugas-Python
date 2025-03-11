import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database
import pandas as pd
from fpdf import FPDF
from datetime import datetime
import csv
import time
import serial
import threading  
app = customtkinter.CTk()
app.title("RESISTIVITY MONITORING")
app.geometry("800x620")
app.configure(bg='#161C25')
app.resizable(False, False)

font1 = ("Arial", 20, "bold")
font2 = ("Arial", 12, "bold")

# Setup serial connection
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
no_counter = 1

# Input counter untuk Automatic dan Manual mode
current_input = IntVar(value=1)
target_input = IntVar(value=10)  # Default target untuk Automatic loop

def on_closing():
    if ser.is_open:
        ser.close()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

def serial_loop(count):
    global no_counter
    for i in range(count):
        volt = i * 2
        ampere = i * 2 + 1
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        data = f"{volt},{ampere}"
        ser.write(data.encode())
        print(f"Data sent: {data}")

        tree.insert("", END, values=(no_counter, volt, ampere, time_stamp))
        no_counter += 1
        time.sleep(1)

def clear_data():
    # Hapus semua data dari tree
    for item in tree.get_children():
        tree.delete(item)

def start_measurement():
    count = target_input.get()
    clear_data()  # Hapus hasil sebelumnya
    global no_counter
    no_counter = 1  # Reset nomor counter
    threading.Thread(target=serial_loop, args=(count,), daemon=True).start()

def auto_measurement():
    start_measurement()  # Panggil fungsi untuk memulai ulang pengukuran otomatis

def manual_measurement():
    global no_counter
    target_value = target_input.get()

    if no_counter > target_value:
        no_counter = 1  # Reset nomor counter ke 1
        manual_button.configure(state='normal')  # Aktifkan kembali tombol Manual
        clear_data()  # Hapus hasil sebelumnya
        
        return
    # Kirim data untuk current_input
    volt = no_counter * 2
    ampere = no_counter * 2 + 1
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Kirim data serial
    data = f"{volt},{ampere}"
    ser.write(data.encode())
    print(f"Data sent: {data}")

    # Tambah data ke tree
    tree.insert("", END, values=(no_counter, volt, ampere, time_stamp))
    no_counter += 1  # Tambah nomor counter

def update_target_input(step):
    # Update nilai target_input langsung dari tombol Next/Prev
    new_value = target_input.get() + step
    if new_value >= 1:
        target_input.set(new_value)
# Insert function to handle GUI interaction
# def insert():
#     id = id_entry.get()
#     volt = volt_entry.get()
#     ampere = ampere_entry.get()
#     time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     if not (id and volt and ampere):
#         messagebox.showerror("Error", "Enter all fields")
#     elif database.id_exists(id):
#         messagebox.showerror("Error", "ID already exists")
#         clear()
#     else:
#         database.insert_measurements(id, volt, ampere, time_stamp)
#         add_to_treeview()
#         clear()
        

def add_to_treeview():
    measurements = database.fetch_measurements()
    tree.delete(*tree.get_children())

    for measurement in measurements:
        tree.insert("", END, values=measurement)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0, END)
    volt_entry.delete(0, END)
    ampere_entry.delete(0, END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)["values"]
        clear()
        id_entry.insert(0, row[0])
        volt_entry.insert(0, row[1])
        ampere_entry.insert(0, row[2])
    else:
        pass


def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "Choose an measurement to delete")
    else:
        id = id_entry.get()
        database.delete_measurements(id)
        
        add_to_treeview()
        clear()
        messagebox.showinfo("Success", "Data has been deleted")

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "Choose a measurement to update")
    else:
        id = id_entry.get()
        volt = volt_entry.get()
        ampere = ampere_entry.get()
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        database.update_measurements(volt, ampere, time_stamp, id)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success", "Data has been updated")

def export_to_excel():
    measurements = database.fetch_measurements()
    df = pd.DataFrame(measurements, columns=['No', 'Volt', 'Ampere', 'Time'])
    file_name = f'measurement_{datetime.now().strftime("%Y-%m-%d_%H.%M.%S")}.xlsx'
    df.to_excel(file_name, index=False)
    print(f"Data exported to {file_name}")
    messagebox.showinfo("Export Successful", f"Data exported to {file_name}")

def export_to_pdf():
    measurements = database.fetch_measurements()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Menambahkan judul
    pdf.cell(200, 10, txt=f"Measurement Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
    
    # Menambahkan header
    pdf.cell(30, 10, 'No', 1)
    pdf.cell(50, 10, 'Volt', 1)
    pdf.cell(40, 10, 'Ampere', 1)
    pdf.cell(70, 10, 'Time', 1)
    pdf.ln()

    # Menambahkan data
    for measurement in measurements:
        pdf.cell(30, 10, measurement[0], 1)
        pdf.cell(50, 10, measurement[1], 1)
        pdf.cell(40, 10, measurement[2], 1)
        pdf.cell(70, 10, measurement[3], 1)
        pdf.ln()

    file_name = f'measurements_{datetime.now().strftime("%Y-%m-%d_%H.%M.%S")}.pdf'
    pdf.output(file_name)
    print(f"Data exported to {file_name}")
    messagebox.showinfo("Export Successful", f"Data exported to {file_name}")

# Fungsi untuk menampilkan waktu sekarang
def show_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
    time_label.configure(text=f"{current_time}")
    app.after(1000, show_current_time)


def export_to_csv():  
    measurements = database.fetch_measurements()
    with open('measurement.csv', mode='w', newline='') as file:  
        writer = csv.writer(file)  
        writer.writerow(['No', 'Volt', 'Ampere', 'Time'])  # Tulis header CSV  
        writer.writerows(measurements)  # Tulis data karyawan ke CSV
    messagebox.showinfo("Export Successful", "Data exported to measurement.csv")
# Tambahkan label untuk menampilkan jam dan tanggal
time_label = customtkinter.CTkLabel(app, font=font1, text="", text_color="#fff",  width=300, height=30)
time_label.place(x=380, y=7)

id_label = customtkinter.CTkLabel(app, font=font1,  text="No:", text_color="#fff")
id_label.place(x=20, y=50)

id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color="#0C9295", border_width=2, width=180)
id_entry.place(x=100, y=50)

volt_label = customtkinter.CTkLabel(app, font=font1,  text="Volt:", text_color="#fff")
volt_label.place(x=20, y=100)

volt_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color="#0C9295", border_width=2, width=180)
volt_entry.place(x=100, y=100)

ampere_label = customtkinter.CTkLabel(app, font=font1,  text="Ampere:", text_color="#fff")
ampere_label.place(x=20, y=150)

ampere_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color="#0C9295", border_width=2, width=180)
ampere_entry.place(x=100, y=150)

csv_button = customtkinter.CTkButton(app, command=export_to_csv, font=font1, text_color="#fff", text="Export to CSV", fg_color="#4F75FF", hover_color="#6439FF", cursor="hand2", corner_radius=15,  width=260)
csv_button.place(x=20, y=210)

pdf_button = customtkinter.CTkButton(app, command=export_to_pdf, font=font1, text_color="#fff", text="Export to PDF", fg_color="#E40404", hover_color="#AE0000", cursor="hand2", corner_radius=15,  width=260)
pdf_button.place(x=20, y=260)

excel_button = customtkinter.CTkButton(app, command=export_to_excel, font=font1, text_color="#fff", text="Export to Excel", fg_color="#054312", hover_color="#00850B", cursor="hand2", corner_radius=15,  width=260)
excel_button.place(x=20, y=310)


# Button start measurement
start_button = customtkinter.CTkButton(app, command=start_measurement, font=font1, text_color="#fff", text="Start Measurement", fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
start_button.place(x=20, y=360)

# Pengaturan tombol dan entri input
prev_button = customtkinter.CTkButton(app, command=lambda: update_target_input(-1), text="Prev", font=font1, fg_color="#4F75FF", hover_color="#6439FF", corner_radius=15, width=70)
prev_button.place(x=20, y=420)

target_input_entry = customtkinter.CTkEntry(app, textvariable=target_input, font=font1, fg_color="#161C25", border_color="#F15704", border_width=2, corner_radius=15, width=100)
target_input_entry.place(x=100, y=420)

next_button = customtkinter.CTkButton(app, command=lambda: update_target_input(1), text="Next", font=font1, fg_color="#4F75FF", hover_color="#6439FF", corner_radius=15, width=70)
next_button.place(x=210, y=420)

auto_button = customtkinter.CTkButton(app, command=auto_measurement, font=font1, text_color="#fff", text="Automatic Measurement", fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
auto_button.place(x=20, y=480)

manual_button = customtkinter.CTkButton(app, command=manual_measurement, font=font1, text_color="#fff", text="Manual Measurement", fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
manual_button.place(x=20, y=540)

# target_input_label = customtkinter.CTkLabel(app, text="Input:", font=font1)
# target_input_label.place(x=25, y=420)




# current_input_label = customtkinter.CTkLabel(app, text="Current:", font=font1)
# current_input_label.place(x=20, y=550)

# current_input_display = customtkinter.CTkLabel(app, textvariable=current_input, font=font1)
# current_input_display.place(x=20, y=460)


# clear_button = customtkinter.CTkButton(app, command=lambda:clear(True), font=font1, text_color="#fff", text="New Measurement",  fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
# clear_button.place(x=20, y=420)

update_button = customtkinter.CTkButton(app, command=update, font=font1, text_color="#fff", text="Update Measurement",  fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
update_button.place(x=300, y=420)

delete_button = customtkinter.CTkButton(app, command=delete, font=font1, text_color="#fff", text="Delete Measurement",  fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
delete_button.place(x=580, y=420)

style = ttk.Style(app)

style.theme_use("clam")
style.configure("Treeview.Heading", font=font2, )
# foreground="#fff",  background="#000", fieldbackground="#313837"
style.map("Treeview", background=[("selected", "#1A8F2D")])


tree = ttk.Treeview(app, height=16)
tree["columns"] = ("No", "Volt", "Ampere", "Time")

tree.column("#0", width=0, stretch=tk.NO)
tree.column("No", anchor=tk.CENTER, width=120)
tree.column("Volt", anchor=tk.CENTER, width=120)
tree.column("Ampere", anchor=tk.CENTER, width=120)
tree.column("Time", anchor=tk.CENTER, width=170)

tree.heading("No", text="No")
tree.heading("Volt", text="Volt")
tree.heading("Ampere", text="Ampere")
tree.heading("Time", text="Time")

tree.place(x=300, y=40)

tree.bind("<ButtonRelease>", display_data)

show_current_time()
add_to_treeview()

app.mainloop()