#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import logging
from user import UserThread

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
                conn = self.socket.accept()[0]
            except socket.error:
                break

            user_thread = UserThread(conn)
            users[user_thread.getName()] = user_thread
            user_thread.start()

            """
            If user_thread is died, then remove from user list.
            """
            for user in users:
                if not user.isAlive():
                    del users[user.getName()]


if __name__ == "__main__":
    logger = logging.getLogger("main")
    logger.warning("Configuration")
    logger.warning(settings.SERVER)

    users = {}

    server = Server()

    print("Server is ready!")

