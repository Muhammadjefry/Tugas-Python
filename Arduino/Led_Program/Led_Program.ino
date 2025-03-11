char userInput;

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
   if (Serial.available()>0){
    userInput = Serial.read();

    if(userInput == 'o'){
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.print("Lampu Nyala");
    }
    if(userInput == 'x'){
      digitalWrite(LED_BUILTIN, LOW);
      Serial.print("Lampu Mati");
    }
   }//Serial.available
}//Void
