String data;
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    data = Serial.readStringUntil('\n');  // Membaca hingga newline
    Serial.println("Data received from Python: " + data);  // Mencetak data yang diterima
  }
}