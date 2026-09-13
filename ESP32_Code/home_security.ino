// IoT Home Security System
// Made by Adishree Chavan - 1st Year Project
// Components: ESP32, PIR sensor, Door sensor, Buzzer

int pirPin = 13;      // PIR sensor pin
int doorPin = 12;     // door sensor pin  
int buzzerPin = 14;   // buzzer pin

void setup() {
  Serial.begin(115200);
  pinMode(pirPin, INPUT);
  pinMode(doorPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  
  Serial.println("System Started...");
  Serial.println("Home Security Active");
}

void loop() {
  int motion = digitalRead(pirPin);
  int doorStatus = digitalRead(doorPin);

  // check motion
  if(motion == 1) {
    Serial.println("Motion Detected! Alert!");
    digitalWrite(buzzerPin, HIGH);
    delay(500);
  }
  
  // check door
  if(doorStatus == 0) {
    Serial.println("Door Opened! Alert!");
    digitalWrite(buzzerPin, HIGH);
    delay(500);
  }

  // if everything ok
  if(motion == 0 && doorStatus == 1) {
    Serial.println("All Safe");
    digitalWrite(buzzerPin, LOW);
  }

  delay(1000); // wait 1 sec
}
