
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() >= 7) { 
    String input = Serial.readStringUntil('\n');
    
   
    float values[6];
    for (int i = 0; i < 6; i++) {
      if (input[i] == '1') {
        values[i] = random(0,100); 
      } else {
        values[i] = 0.0;
      }
    }
    
   
    for (int i = 0; i < 6; i++) {
      Serial.print(values[i]);
      if (i < 5) Serial.print(",");
    }
    Serial.println();
  }
}