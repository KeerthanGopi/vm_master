import paho.mqtt.client as mqtt

def setup(queue):
    global pinged
    client = mqtt.Client("ms")
    client.connect("127.0.0.1", 1883)
    pinged = False
    main(client, queue, pinged)


def main(client, queue, pinged):
    if not queue.empty():
        pinged = queue.get()
        print(pinged)
    if not pinged:
        recieve = input("Enter: ")
    else:
        recieve = ""
    if recieve != "" and recieve != "n":
        client.publish("Ping-Pong", (recieve + ".master"))
        if recieve != "ping":
            pinged = False
        else:
            pinged = True
    if recieve != "n":
        main(client, queue, pinged)
