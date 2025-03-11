import customtkinter as ctk

def on_combobox_select(event):
    # Ambil nilai yang dipilih dari combobox
    selected_value = operator_combobox.get()
    print(f"Value Selected: {selected_value}")  # Debugging output
    # Set nilai tersebut ke dalam entry
    result_entry.delete(0, ctk.END)  # Hapus isi entry sebelumnya
    result_entry.insert(0, selected_value)  # Masukkan nilai ke dalam entry

# Membuat jendela utama
app = ctk.CTk()
app.title("Combobox to Entry Example")
app.geometry("300x200")

# Label untuk dropdown
label = ctk.CTkLabel(app, text="Pilih Operator:", font=("Arial", 14))
label.pack(pady=20)

# Dropdown combobox menggunakan customtkinter
values = ["Operator 1", "Operator 2", "Operator 3", "Operator 4"]
operator_combobox = ctk.CTkComboBox(app, values=values, font=("Arial", 14), width=200)
operator_combobox.pack(pady=10)

# Entry untuk menampilkan pilihan
result_entry = ctk.CTkEntry(app, font=("Arial", 14), width=200)
result_entry.pack(pady=10)

# Bind event untuk combobox, agar ketika dipilih langsung tampil di entry
operator_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

# Menjalankan aplikasi
app.mainloop()
