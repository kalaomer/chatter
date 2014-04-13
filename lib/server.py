#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

import settings
from lib.users import users
from lib.logger import logger


class Server():

    users = {}

    def __init__(self):

        logger.warning('Configuration: ' + str(settings.SERVER))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setblocking(False)
            self.socket.bind((settings.SERVER.HOST, settings.SERVER.PORT))
            self.socket.listen(settings.SERVER.MAX_CONNECTION)

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

                users.create_user(conn)

            #    self.users.update({user_thread.getName(): user_thread})

                logger.warning("New user connected!")
                logger.warning("User list!")
                logger.warning(repr(self.users))

                """
                If user_thread is died, then remove from user list.
                """
                """
                for user in self.users:
                    if not user.isAlive():
                        del self.users[user.getName()]
                """
        except KeyboardInterrupt:
            logger.warning("Press CTRL+C for exit!")

        except Exception as err:
            logger.error(err)
            raise err

        self.socket.close()
        logger.warning("Server is closed.")
