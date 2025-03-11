import sqlite3

def create_table():
    conn = sqlite3.connect('measurements.db')
    cur = conn.cursor()
    cur.execute('''  
        CREATE TABLE IF NOT EXISTS measurements (  
            id TEXT PRIMARY KEY,  
            volt TEXT,  
            ampere TEXT,  
            time TEXT  
            )''')  
    conn.commit()  
    conn.close()  

def fetch_measurements():
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('SELECT * FROM measurements')  
    measurements = cur.fetchall()  
    conn.close()  
    return measurements  

def insert_measurements(id, volt, ampere, time):  
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('INSERT INTO measurements (id, volt, ampere, time) VALUES (?, ?, ?, ?)',  
                (id, volt, ampere, time)) 
    conn.commit()  
    conn.close()  

def delete_measurements(id):  
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('DELETE FROM measurements WHERE id=?', (id,))  
    conn.commit()  
    conn.close()  

def update_measurements(new_volt, new_ampere, new_time, id):  
    conn = sqlite3.connect('measurements.db')  
    cur = conn.cursor()  
    cur.execute('UPDATE measurements SET volt=?, ampere=?, time=? WHERE id=?', 
                (new_volt, new_ampere, new_time, id))  
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
