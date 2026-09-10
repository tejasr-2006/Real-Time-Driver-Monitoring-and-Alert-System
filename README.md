# 🚗 Real-Time Driver Monitoring and Alert System

> An AI-powered driver monitoring system that detects distracted driving behaviors in real time using **YOLOv8**, **OpenCV**, and **Python**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📖 Overview

Road accidents caused by driver distraction are a major safety concern. This project uses **Computer Vision** and **Deep Learning** to monitor a driver's behavior in real time.

The system detects:

- 📱 Mobile phone usage
- 👤 Driver presence
- 👀 Driver attention
- ⚠️ Distracted driving
- 🔊 Real-time alerts

When unsafe behavior is detected, the system immediately generates warnings to help improve road safety.

---

## ✨ Features

- ✅ Real-time webcam monitoring
- ✅ YOLOv8 object detection
- ✅ Mobile phone detection
- ✅ Driver distraction detection
- ✅ Head direction monitoring
- ✅ Audio alert system
- ✅ Fast and lightweight implementation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Image Processing |
| YOLOv8 | Object Detection |
| NumPy | Numerical Operations |

---

## 📂 Project Structure

```
Real-Time-Driver-Monitoring-and-Alert-System
│
├── alert.py
├── decision.py
├── detection.py
├── focus.py
├── gui.py
├── main.py
├── yolov8n.pt
├── sounds/
│   └── beep.wav
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/tejasr-2006/Real-Time-Driver-Monitoring-and-Alert-System.git
```

### Navigate to the project folder

```bash
cd Real-Time-Driver-Monitoring-and-Alert-System
```

### Install dependencies

```bash
pip install opencv-python ultralytics numpy
```

### Run the project

```bash
python main.py
```

---

## ⚙️ How It Works

1. Captures live video from the webcam.
2. Detects the driver using YOLOv8.
3. Detects mobile phone usage.
4. Analyzes driver attention.
5. Generates audio alerts when distracted driving is detected.

---

## 🎯 Applications

- Smart Vehicles
- Driver Assistance Systems
- Fleet Monitoring
- Road Safety
- AI Surveillance
- Automotive Research

---

## 📸 Demo

### Driver Monitoring

```
<img width="542" height="334" alt="image" src="https://github.com/user-attachments/assets/c83679c5-5523-49cb-bbf0-2c5700f6949e" />

```

---

## 🔮 Future Improvements

- 😴 Drowsiness Detection
- 👁️ Eye Blink Detection
- 🚗 Seat Belt Detection
- 📊 Driver Analytics Dashboard
- ☁️ Cloud Data Logging
- 📱 Mobile App Integration

---

## 👨‍💻 Author

**Tejas R**

- GitHub: https://github.com/tejasr-2006
- LinkedIn: https://www.linkedin.com/in/tejas-r-545b00318/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
