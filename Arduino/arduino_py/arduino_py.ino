int cnt;
char penampung[10];

void setup() {
  Serial.begin(9600);
}

void loop() {
  sprintf(penampung, "%d", cnt);
  Serial.println(penampung);
  cnt++;
  delay(1000);
}
