# 6-dof-Arm
6 DOF Robotic Arm 
This project features a 6 Degrees of Freedom (DOF) robotic arm built using 3D-printed parts, servo motors, and controlled via an Arduino Uno and a Python GUI interface.

The robotic arm can be controlled in real-time through a desktop interface built with Tkinter, which sends servo angle values via serial communication to the Arduino.

# Hardware Components
Arduino Uno (or compatible),
6x Servo Motors,
Expansion shield (optional but recommended),
Jumper wires (Male-Female),
USB cable for Arduino-PC connection.


# Wiring / Connection
---Servo	Arduino Pin---
Servo 1-	D2
Servo 2-	D3
Servo 3-	D4
Servo 4-	D5
Servo 5-	D6
Servo 6-	D7

💻 Software Setup
Arduino
Language: Arduino C++
Library Required:
#include <Servo.h>
Upload the Arduino code provided (.ino) to your Arduino Uno.

Python (PC Side)
Language: Python 3.x
GUI: Tkinter (standard in Python)
Serial Communication: PySerial

Required Python Packages:
pip install pyserial

Python GUI Features:
Real-time angle control for each servo via sliders.
Automatically sends updated angles via serial.
Kinematic limit (example threshold: total rotation ≤ 800°) to prevent overloading servos.

⚙️ How It Works
Python GUI reads values from sliders for all 6 servos.
The values are sent as a comma-separated string over serial (e.g., 90,120,85,90,100,95\n).
Arduino reads this string, parses it, and rotates each servo accordingly using Servo.write().
