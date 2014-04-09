__author__ = 'kalaomer'

# Server kodları.

from threading import Thread
import socket
import logging
from config import config

# Logger
logger = logging.getLogger("main")

# Configration'ı yayınla
logger.warning("Configration")
logger.warning(config())

class Client():
    def __init__(self, clientSocket):
        self.clientSocket = clientSocket

    def listen(self):
        while True:
            try:
                message = self.clientSocket.recv(MAX_PACKAGE_SIZE)
            except socket.error:
                break

class Server():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def ready(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(False)
        self.socket.bind(HOST, PORT)
        self.socket.listen(LISTEN)

        print("Server is ready!")

    def listen(self):
        while True:
            try:
                message = self.socket.recv(MAX_PACKAGE_SIZE)
            except socket.error:
                break

    """Server'a giriş işlemi yapılıyor"""
    def makeLogin(self):
        pass


clients = {}

server = Server()

print("Server is ready!")

