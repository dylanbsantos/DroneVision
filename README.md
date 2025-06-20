# DroneVision – Facial Tracking & Keyboard-Controlled Drone

DroneVision is a Python-based drone control project developed as part of an A-Level coursework. It allows a Tello drone to either follow a human face in real-time using computer vision or be controlled manually via keyboard input.

## Features

- **Facial Tracking Mode** – Uses OpenCV to detect and follow faces in real time.
- **Manual Control Mode** – Allows directional control via keyboard inputs using an intuitive layout.
- **Live Video Feed** – Real-time camera streaming from the Tello drone.
- **Emergency Landing** – Quickly land the drone with a single keypress.
- **Image Capture** – Snap photos directly from the feed.
- **Modular Structure** – Organized Python files for tracking, movement, keypresses, etc.
- [NOTE: TOGGLE BUTTON TO CHANGE FROM FACIAL TRACKING TO MANUAL CONTROL WAS NOT ADDED]

## Tech Stack

- Python
- OpenCV
- djitellopy
- Pygame

## Setup

1. Install dependencies:
   ```bash
   pip install opencv-python djitellopy pygame
   ```

2. Run the desired Python script:
   ```bash
   python Project-keyboardControlImageCapture.py
   ```

> ⚠️ This project was designed using the Ryze Tello drone. Make sure your system has access to its WiFi network and required permissions.

## Report

For full implementation details, design decisions, and testing process, please refer to the included PDF report: `DroneVision_Report.pdf`

## Author

**Dylan Santos**  
[Portfolio Website](https://dylansantos.xyz)  
[GitHub](https://github.com/dylanbsantos)

---

© 2025 Dylan Santos. All rights reserved.
