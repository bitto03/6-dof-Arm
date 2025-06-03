#include <Servo.h>

Servo servo1, servo2, servo3, servo4, servo5, servo6;

void setup() {
  Serial.begin(9600);
  servo1.attach(2);
  servo2.attach(3);
  servo3.attach(4);
  servo4.attach(5);
  servo5.attach(6);
  servo6.attach(7);
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n'); // Read until newline
    input.trim();
    if (input.length() > 0) {
      int angles[6];
      int index = 0;
      char *token = strtok((char*)input.c_str(), ",");
      while (token != NULL && index < 6) {
        angles[index++] = atoi(token);
        token = strtok(NULL, ",");
      }
      
      if (index == 6) {
        // Smooth transition (optional: for very precision-sensitive projects)
        servo1.write(angles[0]);
        servo2.write(angles[1]);
        servo3.write(angles[2]);
        servo4.write(angles[3]);
        servo5.write(angles[4]);
        servo6.write(angles[5]);
      }
    }
  }
}
