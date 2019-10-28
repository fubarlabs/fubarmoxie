# Fubar Moxie 

## Functioning Bits:

Just be a client for the Moxie Board information:

Just be a client:

`python moxieclient.py`

Log all the button events and save to file:

```
cd moxielogger
python moxielogger
```

Shows the team rankings:

`python moxieserver.py`

### * Not working yet

Resources:

Simulate the messages:
Paho Mqtt Publish:

Docker Broker: 

https://tewarid.github.io/2019/04/03/installing-and-configuring-the-mosquitto-mqtt-broker.html

Find your broker ip from docker:

`docker ps`

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id`

