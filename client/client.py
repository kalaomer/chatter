__author__ = 'kalaomer'

import sys
sys.path.append('..')

import threading
import time
import socket

import settings

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
        result = self.socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)

        if result is None:
            self.kill_thread()
            print('Connection lost!')
        else:
            result = result.strip().decode()
        return result

    def kill_thread(self):
        self.socket.close()
        self._stop()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((settings.SERVER.HOST, settings.SERVER.PORT))

listener = Listener(client)
listener.run()

try:
    while True:
        message = input()
        client.sendall(message)

        if message == "\quit":
            client.close()
            exit()
        pass
except KeyboardInterrupt as err:
    raise err

except Exception as err:
    raise err