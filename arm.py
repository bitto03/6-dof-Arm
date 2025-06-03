import tkinter as tk
import serial
import time

# --- SERIAL CONNECTION SETUP ---
arduino = serial.Serial(port='COM9', baudrate=9600, timeout=1)  # Change COM port if needed
time.sleep(2)  

def send_angles(event=None):
    angles = [
        slider1.get(),
        slider2.get(),
        slider3.get(),
        slider4.get(),
        slider5.get(),
        slider6.get()
    ]
    
    # --- KINEMATIC SIMPLE CHECK
    if sum(angles) > 800:  # Example: total rotation shouldn't exceed 800°
        print("Warning: Overload risk! Adjust angles.")
        return

    angle_str = ",".join(str(a) for a in angles) + "\n"
    arduino.write(angle_str.encode('utf-8'))

#GUI 
root = tk.Tk()
root.title("6DOF Robotic Arm - Live Control Dashboard")

sliders = []

#6 SLIDERS
for i in range(6):
    slider = tk.Scale(root, from_=0, to=180, resolution=1, label=f"Servo {i+1}", orient=tk.HORIZONTAL, command=send_angles)
    slider.set(90)  # Start centered
    slider.pack(padx=10, pady=5)
    sliders.append(slider)

# Assign sliders to variables for easier access
slider1, slider2, slider3, slider4, slider5, slider6 = sliders

root.mainloop()
