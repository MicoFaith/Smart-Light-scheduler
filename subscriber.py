import paho.mqtt.client as mqtt

# MQTT settings
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'light_control'

# Create and open the relay_cmd.txt file to log commands
relay_cmd_file = open("relay_cmd.txt", "a")

# Callback when a message is received
def on_message(client, userdata, message):
    command = message.payload.decode('utf-8')
    print(f"Received message: {command}")

    # Log the command to the relay_cmd.txt file to simulate sending the command to Arduino
    relay_cmd_file.write(f"Simulated Command: {command}\n")
    relay_cmd_file.flush()  # Ensure data is written to the file immediately

    # Simulate sending the command to Arduino
    if command == '1':
        print("Simulating '1' to Arduino: Turning light ON")
    elif command == '0':
        print("Simulating '0' to Arduino: Turning light OFF")

# Setup MQTT client and connect
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Subscribe to the topic
client.subscribe(MQTT_TOPIC)

# Start the MQTT client loop to listen for messages
client.loop_start()

try:
    while True:
        pass  # Keeps the script running
except KeyboardInterrupt:
    print("Exiting...")
    relay_cmd_file.close()  # Close the file when exiting
    client.loop_stop()  # Stop the MQTT client loop
