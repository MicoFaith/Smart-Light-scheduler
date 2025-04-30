# 🌟 SmartLight Scheduler

A creative IoT dashboard that allows users to schedule ON and OFF times for a light—simulating a smart home lighting system using **HTML/CSS/JavaScript**, **WebSocket**, **MQTT**, and **Arduino**.

---

## 🎯 Project Objective

Simulate a real-world IoT dashboard to control a light through an intuitive interface and robust communication pipeline:

- **Frontend**: Clean and responsive UI for scheduling ON/OFF times.
- **WebSocket Server (Python)**: Receives schedule and publishes to MQTT broker.
- **MQTT Subscriber (Python)**: Listens to schedule updates and sends serial commands to Arduino.
- **Arduino**: Reads serial input and toggles a relay based on `1` (ON) or `0` (OFF).

---

## 💡 Features

- ✅ Real-time scheduling with WebSocket  
- ✅ WebSocket to MQTT communication bridge  
- ✅ Serial interface with Arduino  
- ✅ Clean, user-friendly interface  
- ✅ Live feedback/status messages to the user  

---

## 🚀 Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/your-username/smartlight-scheduler.git
cd smartlight-scheduler
2. Start the WebSocket Server
bash
Copy
Edit
python websocket_server.py
3. Open the Dashboard
Open index.html in your browser (double-click or right-click > Open with Chrome)

4. Start the MQTT Subscriber
bash
Copy
Edit
python subscriber.py
⚠️ Make sure your Arduino is connected and uses the correct COM port (default: COM3). Update subscriber.py if needed.

🖼️ Screenshots
WebSocket Server
server.png
MQTT Subscriber
subscriber.png
