#include <WiFi.h>

#define PIR_PIN 13
#define DOOR_PIN 12
#define BUZZER_PIN 14

void setup() {
  Serial.begin(115200);
  pinMode(PIR_PIN, INPUT);
  pinMode(DOOR_PIN, INPUT_PULLUP);
  pinMode(BUZZER_PIN, OUTPUT);
  Serial.println("IoT Home Security Started");
}

void loop() {
  int motion = digitalRead(PIR_PIN);
  int door = digitalRead(DOOR_PIN);

  if (motion == HIGH) {
    Serial.println("ALERT! Motion Detected!");
    digitalWrite(BUZZER_PIN, HIGH);
  }
  if (door == LOW) {
    Serial.println("ALERT! Door Opened!");
    digitalWrite(BUZZER_PIN, HIGH);
  }
  if (motion == LOW && door == HIGH) {
    digitalWrite(BUZZER_PIN, LOW);
    Serial.println("Status: SAFE");
  }
  delay(1000);
}
