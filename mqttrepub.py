#!/usr/bin/python
#import mosquitto
import paho.mqtt.client as mqtt
import sys
import time
topic = "test"
sbroker = "192.168.1.1"
dbroker = "192.168.1.2"

def on_connect(mosq,obj,rc):
    mosq.subscribe(topic, 0)

def on_message(mosq,obj,msg):
   message= msg.payload
   mqtt2 = mqtt.Client()
   mqtt2.connect(dbroker, 1883, 60)
   mqtt2.publish(topic, message)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(sbroker, 1883, 60)


mqttc.loop_forever()

