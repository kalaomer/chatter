
import settings
import socket

class User():
    def __init__(self, client_socket):
        self.client_socket = client_socket

    # This function runs in thread
    def listen(self):
        while True:
            try:
                message = self.client_socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
            except socket.error:
                break