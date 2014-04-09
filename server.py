#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import logging
import settings
from user import UserThread

class Server():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def ready(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setblocking(False)
            self.socket.bind(settings.SERVER.HOST, settings.SERVER.PORT)
            self.socket.listen(settings.SERVER.LISTEN)

            logger.warning("Server is ready!")
        except:
            logger.error("Socket error!")

    def run(self):
        try:
            while True:
                try:
                    conn = self.socket.accept()[0]
                except socket.error:
                    break

                user_thread = UserThread(conn, users)
                users[user_thread.getName()] = user_thread
                user_thread.start()

                """
                If user_thread is died, then remove from user list.
                """
                for user in users:
                    if not user.isAlive():
                        del users[user.getName()]
        except KeyboardInterrupt:
            logger.warning("Press CTRL+C for exit!")

        self.socket.close()

if __name__ == "__main__":
    logger = logging.getLogger("main")
    logger.warning("Configuration")
    logger.warning(settings.SERVER)

    users = {}

    server = Server()
    server.ready()

    """
    RUN FOREST, RUN!
    DON'T LOOK YOUR BACK!
    """
    server.run()

