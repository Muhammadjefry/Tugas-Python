import sqlite3

def create_table():
    conn = sqlite3.connect('measurements.db')
    cur = conn.cursor()
    cur.execute('''  
        CREATE TABLE IF NOT EXISTS measurements (  
            id TEXT,   
            volt TEXT,  
            ampere TEXT,  
            time_stamp TEXT  
            )''')  
    
    # Tabel kedua: measurement_info
    cur.execute('''
        CREATE TABLE IF NOT EXISTS measurement_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operator TEXT,
            lokasi TEXT,
            lintasan TEXT,
            panjang_lintasan TEXT,
            spasi TEXT,
            jumlah_chanel TEXT,
            kordinat_awal TEXT,
            kordinat_akhir TEXT,
            elevasi TEXT,
            asisten TEXT,
            tanggal TEXT,
            waktu TEXT,
            cuaca TEXT,
            keterangan TEXT
        )
    ''')
    
    conn.commit()  
    conn.close()  

# def save_info(data):
#     # Fungsi untuk menyimpan atau mengupdate data di tabel measurement_info
#     conn = sqlite3.connect('measurements.db')
#     cursor = conn.cursor()
    
#     print("Data yang akan disimpan:", data) 
    
#     try:
#         # Periksa apakah data sudah ada (hanya simpan satu baris data)
#         cursor.execute("SELECT id FROM measurement_info LIMIT 1")
#         result = cursor.fetchone()

#         if result:
#             # Jika data ada, lakukan update
#             cursor.execute('''
#                 UPDATE measurement_info SET
#                     operator = :operator,
#                     lokasi = :lokasi,
#                     lintasan = :lintasan,
#                     panjang_lintasan = :panjang_lintasan,
#                     spasi = :spasi,
#                     jumlah_chanel = :jumlah_chanel,
#                     kordinat_awal = :kordinat_awal,
#                     kordinat_akhir = :kordinat_akhir,
#                     elevasi = :elevasi,
#                     asisten = :asisten,
#                     tanggal = :tanggal,
#                     waktu = :waktu,
#                     cuaca = :cuaca,
#                     keterangan = :keterangan
#                 WHERE id = :id
#             ''', {**data, "id": result[0]})
#         else:
#             # Jika tidak ada, lakukan insert
#             cursor.execute('''INSERT INTO measurement_info (operator, lokasi, lintasan, panjang_lintasan, spasi, jumlah_chanel,
#                             kordinat_awal, kordinat_akhir, elevasi, asisten, tanggal, waktu,
#                             cuaca, keterangan) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', (data['operator'], data['lokasi'], data['lintasan'], data['panjang_lintasan'], data['spasi'],
#       data['jumlah_chanel'], data['kordinat_awal'], data['kordinat_akhir'], data['elevasi'],
#       data['asisten'], data['tanggal'], data['waktu'], data['cuaca'], data['keterangan']))

#         conn.commit()
#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
#     finally:
#         conn.close()

def update_info(data):
    # Fungsi untuk menyimpan atau mengupdate data di tabel measurement_info
    conn = sqlite3.connect('measurements.db')
    cursor = conn.cursor()

    try:
        # Periksa apakah data sudah ada (hanya simpan satu baris data berdasarkan ID)
        cursor.execute("SELECT id FROM measurement_info LIMIT 1")
        result = cursor.fetchone()
        print("Data yang akan disimpan:", data)

            # Jika data ada, lakukan update
        cursor.execute('''
                UPDATE measurement_info SET
                    operator = :operator,
                    lokasi = :lokasi,
                    lintasan = :lintasan,
                    panjang_lintasan = :panjang_lintasan,
                    spasi = :spasi,
                    jumlah_chanel = :jumlah_chanel,
                    kordinat_awal = :kordinat_awal,
                    kordinat_akhir = :kordinat_akhir,
                    elevasi = :elevasi,
                    asisten = :asisten,
                    tanggal = :tanggal,
                    waktu = :waktu,
                    cuaca = :cuaca,
                    keterangan = :keterangan
                WHERE id = :id
            ''', {**data, "id": result[0]})
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        
def save_info(data):
    # Fungsi untuk menyimpan atau mengupdate data di tabel measurement_info
    conn = sqlite3.connect('measurements.db')
    cursor = conn.cursor()

    try:
        print("Data yang akan disimpan:", data)

        cursor.execute('''INSERT INTO measurement_info (operator, lokasi, lintasan, panjang_lintasan, spasi, jumlah_chanel,
                            kordinat_awal, kordinat_akhir, elevasi, asisten, tanggal, waktu,
                            cuaca, keterangan) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (data['operator'], data['lokasi'], data['lintasan'], data['panjang_lintasan'], data['spasi'],
                  data['jumlah_chanel'], data['kordinat_awal'], data['kordinat_akhir'], data['elevasi'],
                  data['asisten'], data['tanggal'], data['waktu'], data['cuaca'], data['keterangan']))

        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

def fetch_measurements():
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('SELECT * FROM measurements')  
    measurements = cur.fetchall()  
    conn.close()  
    return measurements  

def fetch_measurementsInfo():
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('SELECT * FROM measurement_info')  
    measurements = cur.fetchall()  
    conn.close()  
    print(measurements)
    return measurements  


def insert_measurements(id, volt, ampere, time_stamp):  
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('INSERT INTO measurements (id, volt, ampere, time_stamp) VALUES (?, ?, ?, ?)',  
                (id, volt, ampere, time_stamp)) 
    conn.commit()  
    conn.close()  

def delete_measurements(id):  
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('DELETE FROM measurements WHERE id=?', (id,))  
    conn.commit()  
    conn.close()  

def update_measurements(new_volt, new_ampere, new_time_stamp, id):  
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('UPDATE measurements SET volt=?, ampere=?, time_stamp=? WHERE id=?', 
                (new_volt, new_ampere, new_time_stamp, id))  
    conn.commit()  
    conn.close()  

def id_exists(id):  
    conn = sqlite3.connect('measurements.db')  
    cursor = conn.cursor()  
    cursor.execute('SELECT COUNT(*) FROM measurements WHERE id=?', (id,))  
    result = cursor.fetchone()  
    conn.close()  
    return result[0] > 0  

# Memanggil fungsi create_table saat skrip dijalankan
create_table()
