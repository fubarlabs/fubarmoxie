import paho.mqtt.client as mqtt

broker_url = "pi-iot.local"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
       print("Connected With Result Code: {}".format(rc))

def on_disconnect(client, userdata, rc):
   print("Client Got Disconnected")

def on_message_from_moxieboard(client, userdata, message):
       print("Message Recieved from Moxie Board: "+message.payload.decode())

def on_message(client, userdata, message):
       print("Message Recieved from Others: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_message = on_message

client.connect(broker_url, broker_port)
client.subscribe("BtnsOut", qos=0)

client.message_callback_add("BtnsOut", on_message_from_moxieboard)
client.loop_forever()
