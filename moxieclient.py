# https://mntolia.com/mqtt-python-with-paho-mqtt-client/ was very helpful

import paho.mqtt.client as mqtt
import time


broker_url = "pi-iot.local"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {rc}")

def on_disconnect(client, userdata, rc):
    print("Client got disconnected")
    # client.loop_stop()

def on_button_message(client, userdata, message):
    buttons = message.payload.decode()
    print("Buttons!", buttons)
     
def on_message(client, userdata, message):
    values = message.payload.decode()
    print(message.payload.decode())

client = mqtt.Client("robotsinheels")
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# client.on_message = on_message
client.connect(broker_url, broker_port)
client.loop_start()
client.subscribe("BtnsOut", qos=1)

while True:
    # client.message_callback_add("BtnsOut", on_button_message)
    client.on_message = on_message
# client.loop_forever()
