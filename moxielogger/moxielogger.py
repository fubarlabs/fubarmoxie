# https://mntolia.com/mqtt-python-with-paho-mqtt-client/ was very helpful
# I'm tired, so you're not getting great documentation here right now

import paho.mqtt.client as mqtt
import datetime

# Support for changing the filename each time it runs. Should probably hardcode a name before an actual race
filename = f'files/moxielogger-{input("filename? >>> ")}.csv'

# update header with actual team names, create file, write header to file
# numbers start in top left and go across before going down
#  1  |  2
#  3  |  4
#  5  |  6
# and so on...

header = "times,fubar1,fubar2,fubar3,fubar4,fubar5,fubar6,fubar7,fubar8,fubar9,fubar10,fubar11,fubar12,fubar12,fubar14,fubar15,fubar16,fubar17,fubar18,fubar19,fubar20"
with open(filename, 'w') as f:
    f.write(header + '\n')

# mqtt configuration
broker_url = "pi-iot.local"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {rc}")

def on_disconnect(client, userdata, rc):
    print("Client got disconnected")
    # client.loop_stop()

# def on_button_message(client, userdata, message):
#     buttons = message.payload.decode()
#     print("Buttons!", buttons)
     
def on_message(client, userdata, message):
    values = message.payload.decode()
    print(values)
    with open(filename, 'a') as buttonfile:
        buttonfile.write(values + '\n')

client = mqtt.Client("robotsinheels")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(broker_url, broker_port)
client.loop_start()
client.subscribe("BtnsOut", qos=1)

while True:
    client.on_message = on_message
