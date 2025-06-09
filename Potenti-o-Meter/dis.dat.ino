void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    int pot = analogRead(A0);
    int pot2 = pot*2;
    Serial.print(pot);
    Serial.println(pot2);
    Serial.read();

  }
}
