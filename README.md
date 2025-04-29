🌟 SmartLight Scheduler
A creative IoT dashboard that allows users to schedule ON and OFF times for a light, simulating a smart home lighting system using HTML/CSS/JavaScript, WebSocket, MQTT, and Arduino.

🎯 Project Objective
Simulate a real-world IoT dashboard to schedule a light using a graphical interface and network communication:

Frontend: HTML/CSS/JS interface to set ON/OFF times.

WebSocket Server: Sends schedule to an MQTT broker.

MQTT Subscriber (Python): Listens to MQTT topic and relays serial commands to an Arduino.

Arduino: Acts on 1 (ON) or 0 (OFF) serial input to trigger a relay.

## 💡 Features
- Real-time light scheduling
- WebSocket-MQTT bridge
- Live status updates
- Arduino-controlled relay via serial

## 🚀 Setup
1. Run `websocket_server.py`
2. Open `index.html` in browser
3. Run `subscriber.py`
4. Ensure Arduino is connected on COM13 and running serial relay script

## 📸 Screenshot

