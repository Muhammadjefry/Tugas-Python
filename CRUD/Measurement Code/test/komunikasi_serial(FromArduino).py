import serial
import serial.tools.list_ports

# Menampilkan semua port yang tersedia
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

# Membuka port COM6 (pastikan ini port yang benar)
try:
    ser = serial.Serial('COM6', 9600, timeout=1)
    data = ''
    old_data = ''

    while True:
        if ser.in_waiting > 0:
            try:
                # Membaca data dari Arduino
                data = ser.readline().decode('ascii').strip()
                if data != old_data:
                    print(f'Data dari Arduino: {data}')
                    old_data = data

            except Exception as e:
                # Mencetak error jika ada masalah decoding atau serial
                print(f'Error saat membaca data: {e}')
                
finally:
    # Memastikan port ditutup setelah selesai
    if ser.is_open:
        ser.close()
        print("Port serial ditutup.")
