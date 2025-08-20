# openloop_suntracking_Instrument
Open-loop sun tracking platform using Raspberry Pi Pico (MicroPython) and Arduino Uno (C++). Calculates sun position via GPS and astronomical algorithms for automated sun-photometer alignment. Includes code, wiring, and sensor integration.



# Open-Loop Sun Tracking Instrument

This project implements an open-loop sun tracking platform using Raspberry Pi Pico (MicroPython) and Arduino Uno (C++). It automatically calculates and aligns a sun-photometer to the sun for atmospheric or AOD studies.

## Features

- **Real-time sun position calculation** using GPS data and astronomic algorithms
- **Dual microcontroller architecture**: Pico handles GPS and sun position; Arduino manages motion and stabilization
- **Servo motor control** for pan/tilt alignment
- **IMU feedback** for basic correction (open-loop)

## Hardware

- Raspberry Pi Pico (RP2040)
- Arduino Uno
- GPS module (NEO-6M / 7m /8m)
- IMU sensor (MPU6050)
- Servo motors (e.g., MG995)
- Power: 5V regulated (e.g., LM2596, 10,000mAh Li-ion packs)

## Code Structure

- `pico_gps_suntracker.py` — MicroPython program for Pico
- `arduino_suntracker.ino` — Arduino code for Uno

## Wiring

- Pico UART TX/RX <-> Arduino UART RX/TX (with proper voltage matching if needed)
- GPS to Pico UART1
- MPU6050 to Arduino (I2C)
- Servos to Arduino PWM pins

## Usage

1. Upload each code file to its respective platform.
2. Assemble hardware per schematic in documentation.
3. On power-up, system will auto-align to the sun based on GPS and real-time computation.

---

**For circuit diagrams, theory, and advanced notes, refer to the `Design-and-development-of-openloop-suntracking-instrument.pdf` file in this repo.**
