# Task 5.2C – LED Brightness Control GUI (SIT210)

This project is part of SIT210: Embedded Systems Development – Task 5.2C. The goal is to design a graphical user interface (GUI) on a Raspberry Pi that allows a user to control the brightness of three LEDs using Pulse Width Modulation (PWM).

## 🎯 Task Objective

To build a Python-based GUI using Tkinter that features three sliders. Each slider corresponds to one LED (Red, Green, Yellow) and controls its brightness level in real time through PWM on the Raspberry Pi GPIO pins.

---

## 🛠️ Hardware Used

- Raspberry Pi (any model with GPIO)
- Breadboard
- 3x LEDs (Red, Green, Yellow)
- 3x 220Ω Resistors
- Jumper wires

---

## 🔌 Wiring Diagram

| LED Color | GPIO Pin | Physical Pin |
|-----------|----------|---------------|
| Red       | GPIO 17  | Pin 11        |
| Green     | GPIO 27  | Pin 13        |
| Yellow    | GPIO 22  | Pin 15        |
| Ground    | GND      | Pin 6         |

Each LED’s cathode is connected through a 220Ω resistor to the ground rail (yellow rail on breadboard), which is connected back to the Pi’s GND pin.

---

## 💻 Software Requirements

- Python 3
- RPi.GPIO (installed by default on Raspberry Pi OS)
- Tkinter (also preinstalled)

---

## 🚀 How to Run

1. Clone or download this repository on your Raspberry Pi.
2. Navigate to the project directory:
   ```bash
   cd Task5.2GUI
