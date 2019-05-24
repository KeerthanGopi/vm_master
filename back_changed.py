import paho.mqtt.client as mqtt

def message(client, userdata, message):
    global undone, pinged, queue
    message_recieved = str(message.payload.decode("utf-8")).split(".")
    client1 = message_recieved[1].lower()
    message1= message_recieved[0].lower()
    if client1 == "master":
        if message1 == "ping":
            pinged = True
            queue.put(pinged)
    elif client1 == "slave":
        if pinged == False:
            if message1 == "ping":
                client.publish("Ping-Pong", "pong.master")
        elif pinged ==  True:
            if message1 == "ping":
                undone += 1
                client.publish("Ping-Pong", "Awaiting Response")
            elif message1 == "pong":
                pinged = False
                queue.put(pinged)
                for i in range(0, undone):
                    client.publish("Ping-Pong", "pong.master")
                undone = 0

def setup(Queue):
    global pinged, undone, queue
    queue = Queue
    pinged = False
    undone = 0
    client = mqtt.Client("mr")
    client.connect("127.0.0.1", 1883)
    client.subscribe("Ping-Pong")
    main(client)

def main(client):
    client.on_message = message
    client.loop_forever()

