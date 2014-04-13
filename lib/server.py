#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import logging
import time

import settings
from lib import lang
from lib.user import UserThread


class Server():

    users = {}

    def __init__(self):

        logging.warning("Server just start building!")

        self.logger = logging.getLogger("server")
        self.logger.warning('Configuration: ' + str(settings.SERVER))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setblocking(False)
            self.socket.bind((settings.SERVER.HOST, settings.SERVER.PORT))
            self.socket.listen(settings.SERVER.MAX_CONNECTION)

            self.logger.warning("Server is ready!")
        except Exception as err:
            self.logger.error(err)

    def run(self):
        try:
            while True:

                time.sleep(0.1)

                try:
                    conn = self.socket.accept()[0]
                except Exception as err:
                    continue

                user_thread = UserThread(conn, self)
            #    user_thread.setName(os.urandom(8))
                user_thread.setName('user_%s' % (len(self.users) + 1))
                user_thread.start()
                user_thread.send_text(lang.get_welcome(user_thread.getName()))
            #    user_thread.send_text('>> Your current name is \'%s\'' % user_thread.getName())
                self.users[user_thread.getName()] = user_thread

            #    self.users.update({user_thread.getName(): user_thread})

                self.logger.warning("New user connected!")
                self.logger.warning("User list!")
                self.logger.warning(repr(self.users))

                """
                If user_thread is died, then remove from user list.
                """
                """
                for user in self.users:
                    if not user.isAlive():
                        del self.users[user.getName()]
                """
        except KeyboardInterrupt:
            self.logger.warning("Press CTRL+C for exit!")

        except Exception as err:
            self.logger.error(err)
            raise err

        self.socket.close()
        self.logger.warning("Server is closed.")
