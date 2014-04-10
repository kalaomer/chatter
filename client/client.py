__author__ = 'kalaomer'

import threading
import time
import socket

class Listener(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):

        while True:
            time.sleep(0.1)

            message = self.receive()

            if message:
                print(message)

    def receive(self):
        result = self.client.recv(settings.SERVER.MAX_PACKAGE_SIZE)
        if result:
            result = result.strip()
        return result


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.create_connection(("localhost", 8088), 0)
try:
    pass
except Exception as err:
    print(err)
    exit()

listener = Listener(client)
listener.run()

while True:
    message = input()
    client.send(message)

    if message == "gg":
        client.close()
        exit()
    pass