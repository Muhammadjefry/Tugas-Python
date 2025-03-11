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

app = customtkinter.CTk()
app.title("RESISTIVITY MONITORING")
app.geometry("860x480")
app.configure(bg='#161C25')
app.resizable(False, False)

font1 = ("Arial", 20, "bold")
font2 = ("Arial", 12, "bold")

def add_to_treeview():
    tree.delete(*tree.get_children())
    measurements = database.fetch_measurements()
    print("Data terbaru:", measurements)
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
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"ID: {id}, Volt: {volt}, Ampere: {ampere}, Time: {time}")  # Debug
        
        if not (id and volt and ampere):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        database.update_measurements(volt, ampere, time, id)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success", "Data has been updated")

def insert():
    id = id_entry.get()
    volt = volt_entry.get()
    ampere = ampere_entry.get()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    if not (id and volt and ampere ):
        messagebox.showerror("Error", "Enter  are fields")
    elif database.id_exists(id):
        messagebox.showerror("Error", "NO already exists")
        clear()
    else:
        database.insert_measurements(id, volt, ampere, time)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success", "Data has been inserted")

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
    pdf.cell(30, 10, 'Time', 1)
    pdf.ln()

    # Menambahkan data
    for measurement in measurements:
        pdf.cell(30, 10, measurement[0], 1)
        pdf.cell(50, 10, measurement[1], 1)
        pdf.cell(40, 10, measurement[2], 1)
        pdf.cell(30, 10, measurement[3], 1)
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
    with open('database.csv', mode='w', newline='') as file:  
        writer = csv.writer(file)  
        writer.writerow(['No', 'Volt', 'Ampere', 'Time'])  # Tulis header CSV  
        writer.writerows(measurements)  # Tulis data karyawan ke CSV

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

add_button = customtkinter.CTkButton(app, command=insert, font=font1, text_color="#fff", text="Add Measurement",  fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
add_button.place(x=20, y=360)

clear_button = customtkinter.CTkButton(app, command=lambda:clear(True), font=font1, text_color="#fff", text="New Measurement",  fg_color="#161C25", hover_color="#FF5002", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=260)
clear_button.place(x=20, y=420)

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