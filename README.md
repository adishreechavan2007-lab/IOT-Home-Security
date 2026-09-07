# IOT-Home-Security

#  IoT-Based Home Security System
> "Enhancing safety with smart tech"

A smart, affordable, and user-friendly IoT-based home security solution with real-time monitoring, instant alerts, and remote control via mobile app.

This project was built as part of my 1st Year exploration in IoT and Embedded Systems.

---

###  Problem Statement
Need for a smart, affordable, user-friendly IoT-Based Home Security Project with real-time monitoring, alerts and remote control for motion sensor based security.

###  Key Features (As per Design)
1.  **Smart Door Lock** - Controlled via mobile app with OTP & fingerprint access
2.  **Motion Detection System** - Using PIR sensors that send instant alerts to owner
3.  **Cloud Based Data Storage** - For storing video footage and activity logs
4.  **Gas, Leakage & Smoke Detection** - Integrated with security system
5.  **Mobile App Dashboard** - Showing live-status of all home security devices
6.  **Smart CCTV Camera** - With live video streaming and night vision

###  Prototype - Real World Solution
For the prototype, we focused on core functionality: motion detection and alert notification.

**Hardware Used:**
*   ESP32 / Arduino Board
*   PIR Motion Sensor
*   Buzzer & LED Indicators
*   WiFi Module for Mobile Alerts

**Architecture:**
*   **Edge Hub:** Acts as local coordinator, runs signed firmware, supports Wi-Fi/Ethernet, stores encrypted clips on local SSD.
*   **Low-power Sensors:** Battery-efficient with tamper detection and secure pairing via QR + ephemeral token.
*   **Smart Camera:** On-device person detection, local clip encryption and selective cloud upload for verified events only.

###  Security Architecture & Privacy
*   End-to-End Encryption (Device → Hub → App)
*   Hardware-backed key storage on hub
*   Per-device access policies & minimal data retention
*   User can choose **Local-Only Mode** or **Encrypted Cloud Backup**
*   Mobile App with MFA (Multi-Factor Authentication)

`Sensor → Encrypted Local Hub → Encrypted Cloud Backup → Mobile App (MFA)`

###  Future Enhancements (Green Hat Ideas)
*   AI-based Face Recognition for smarter detection
*   Integration with Alexa / Google Assistant
*   Voice Alert System inside the house

###  Six Hat Analysis
*   **White (Facts):** IoT connects devices for remote monitoring, sensors are widely used.
*   **Red (Feelings):** Gives peace of mind and security, but concerns about privacy.
*   **Black (Risk):** Risk of hacking, internet dependency, initial cost.
*   **Yellow (Benefits):** Improves safety, real-time monitoring from anywhere, quick emergency response.

###  Real-World Benefits
*   **Homeowner:** Peace of mind, actionable alerts, privacy choices.
*   **Product:** Lower incident churn, monetisable cloud features, secure posture.

###  Software Application (Dashboard Code)
Basic working model of the mobile app dashboard built using Python Flask:

```python
# app.py - IoT Dashboard
from flask import Flask
app = Flask(__name__)

@app.route('/')
def status():
    # In real project, fetch data from ESP32 via MQTT/Firebase
    motion_detected = check_pir_sensor() 
    if motion_detected:
        send_telegram_alert("Alert! Motion Detected at Home!")
    return f"System Armed | Motion: {motion_detected}"

# Hardware code (ESP32) sends sensor data to this API
