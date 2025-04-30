import asyncio
import websockets
import json
import paho.mqtt.publish as publish

async def handle_connection(websocket):
    print(f"New client connected: {websocket.remote_address}")
    async for message in websocket:
        print(f"Received message: {message}")
        try:
            schedule = json.loads(message)
            on_time = schedule['onTime']
            off_time = schedule['offTime']
            print(f"Publishing to MQTT: ON={on_time}, OFF={off_time}")
            publish.single("light/schedule", f"{on_time},{off_time}", hostname="localhost", port=1883)
            await websocket.send('Schedule received and published to MQTT')
            print("Sent confirmation to client")
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            await websocket.send(f'Error: Invalid JSON format')
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send(f'Error: {str(e)}')

async def main():
    print("Starting WebSocket server on ws://localhost:8765")
    async with websockets.serve(handle_connection, 'localhost', 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
