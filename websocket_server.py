import asyncio
import websockets
import subprocess

async def handle_client(websocket):
    print("🌐 Browser connected")
    async for message in websocket:
        print(f"📩 Received from browser: {message}")
        command = '1' if message.lower() == 'on' else '0'
        subprocess.run(['mosquitto_pub', '-t', 'light/schedule', '-m', command])
        print(f"📡 Published to MQTT: {command}")

async def main():
    server = await websockets.serve(handle_client, "localhost", 6789)
    print("✅ WebSocket server running on ws://localhost:6789")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
