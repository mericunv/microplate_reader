String interval;
String count;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.println("Initializing");
pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    Serial.println("Recieved:");
    digitalWrite(LED_BUILTIN, LOW);
    interval = Serial.readStringUntil("\n");
    count = Serial.readStringUntil("\n");
    Serial.println(interval.toInt());
    Serial.println(count.toInt());

    delay(3500);
    blink();

  }
}
void blink() {

  for(int i=0; i<=count.toInt(); i++){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(interval.toInt());
      digitalWrite(LED_BUILTIN, LOW);
      delay(interval.toInt());
  }

}

void test(){

for(int i=0; i <= 5; i++){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);}
}