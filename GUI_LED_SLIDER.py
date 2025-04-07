import RPi.GPIO as GPIO
import tkinter as tk

# GPIO setup
# LED Pins: Red = GPIO 17, Green = GPIO 27, Yellow = GPIO 22
LED_PINS = [17, 27, 22]
GPIO.setmode(GPIO.BCM)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

# Setup PWM for each LED at 1000Hz
pwm = [GPIO.PWM(pin, 1000) for pin in LED_PINS]
for p in pwm:
    p.start(0)  # Start with 0% duty cycle

# GUI Setup
def update_led(index, value):
    pwm[index].ChangeDutyCycle(float(value))

root = tk.Tk()
root.title("LED Brightness Control")

# Create sliders with updated labels
led_colors = ["Red", "Green", "Yellow"]  # updated from "Blue" to "Yellow"

for i in range(3):
    scale = tk.Scale(
        root,
        from_=0,
        to=100,
        orient='horizontal',
        label=f'{led_colors[i]} LED Brightness',
        command=lambda val, i=i: update_led(i, val)
    )
    scale.pack()

# Exit and cleanup
def on_closing():
    for p in pwm:
        p.stop()
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
