#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import logging

import settings


class Server():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def ready(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(False)
        self.socket.bind(settings.SERVER.HOST, settings.SERVER.PORT)
        self.socket.listen(settings.SERVER.LISTEN)

        print("Server is ready!")

    def listen(self):
        while True:
            try:
                message = self.socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
            except socket.error:
                break

    def make_login(self):
        """Logging on Server"""
        pass


if __name__ == "__main__":
    logger = logging.getLogger("main")
    logger.warning("Configuration")
    logger.warning(settings.SERVER)

    clients = {}

    server = Server()

    print("Server is ready!")

