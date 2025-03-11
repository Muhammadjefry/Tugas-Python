import serial
import time
import serial.tools.list_ports

# Cek port COM yang tersedia
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

# Ganti 'COM6' dengan port yang sesuai
ser = serial.Serial('COM6', 9600, timeout=1)

try:
    # Mengirimkan beberapa data ke Arduino
    for i in range(5):
        angka = str(i)  # Mengubah angka menjadi string
        ser.write(angka.encode())  # Kirim angka yang dimasukkan ke Arduino
        print(f'Angka yang dikirim: {angka}')
        time.sleep(1)  # Tunggu 1 detik untuk memberikan waktu kepada Arduino

    ser.write(b'Program selesai.\n')  # Kirim pesan akhir
    print("Program selesai.")
finally:
    # Tutup port setelah selesai mengirim data
    ser.close()
    print("Port serial ditutup. Anda bisa membuka Serial Monitor di Arduino IDE.")
