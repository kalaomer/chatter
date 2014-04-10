#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import logging
import settings
import time
from user import UserThread

logger = logging.getLogger("main")
logger.warning("Configuration")
logger.warning(settings.SERVER.__str__(settings.SERVER))

class Server():
    users = {}
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def ready(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setblocking(False)
            self.socket.bind((settings.SERVER.HOST, settings.SERVER.PORT))
            self.socket.listen(settings.SERVER.LISTEN)

            logger.warning("Server is ready!")
        except Exception as err:
            logger.error(err)

    def run(self):
        try:
            while True:

                time.sleep(0.1)

                try:
                    conn = self.socket.accept()[0]
                except Exception as err:
                    continue

                user_thread = UserThread(conn, self)
                self.users[user_thread.getName()] = user_thread
                user_thread.start()

                """
                If user_thread is died, then remove from user list.
                """
                for user in self.users:
                    if not user.is_alive():
                        del self.users[user.getName()]
                        
        except KeyboardInterrupt:
            logger.warning("Press CTRL+C for exit!")

        except Exception as err:
            logger.error(err)

        self.socket.close()
        logger.warning("Server is closed.")

if __name__ == "__main__":

    server = Server()
    server.ready()

    """
    RUN FOREST, RUN!
    DON'T LOOK YOUR BACK!
    """
    server.run()