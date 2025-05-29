#include <Arduino.h>
void setup() {
 
  Serial.begin(9600);
}

void loop() {
 
  if (Serial.available() > 0) {
    
    char receivedChar = Serial.read();
    Serial.write("Read column ");
    Serial.print(receivedChar);
    
  }
}