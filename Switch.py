import sys
import paho.mqtt.client as mqtt
topic = "id/taewoo/relay/cmd"
server = "54.234.134.141"
#server = "52.78.220.207"

# def on_connect(client, userdata, flags, rc):
#     print("Connected with RC : " + str(rc))
#     client.subscribe(topic)

# def on_message(client, userdata, msg):
#     who, m = msg.payload.decode('UTF-8').split(" : ")
#     if who != sys.argv[1]:
#         print(msg.payload.decode('UTF-8'))



client = mqtt.Client()
client.connect(server, 1883, 60)
#client.on_connect = on_connect
#client.on_message = on_message

client.loop_start()

for line in sys.stdin:
    client.publish(topic,(str(line.strip()).encode('UTF-8')))
