#include <SoftwareSerial.h>
SoftwareSerial SSerial(3, 2); // RX, TX untuk SoftwareSerial (pin 3 RX, pin 2 TX)

void setup() {
  Serial.begin(9600);    // Serial bawaan untuk komunikasi dengan Python
  SSerial.begin(9600);   // SoftwareSerial untuk memonitor data
  Serial.println("Setup selesai. Siap menerima data..."); // Menambahkan pesan untuk konfirmasi
}

void loop() {
    if (Serial.available()) {
        String data_dari_python = Serial.readString();
        Serial.print("Data diterima: "); // Tambahkan ini untuk debug
        Serial.println(data_dari_python); // Untuk melihat data di Serial Monitor
    } else {
        Serial.println("Menunggu data..."); // Tambahkan ini untuk memberi tahu bahwa Arduino siap
    }
}

