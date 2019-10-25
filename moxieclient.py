import paho.mqtt.client as mqtt
import time

broker_url = "pi-iot.local"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {rc}")

def on_disconnect(client, userdata, rc):
    print("Client got disconnected")

def on_button_message(client, userdata, message):
    print("Buttons!", message.payload.decode())

# def on_message(client, userdata, message):
#     print(message.payload.decode())

client = mqtt.Client("robotsinheels")
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe("BtnsOut", qos=1)
client.message_callback_add("BtnsOut", on_button_message)

client.loop_forever()
