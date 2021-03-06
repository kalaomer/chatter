#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

from socket import socket
from lib.user import UserThread
from lib import lang


class UserList():

    # UserThread Objects
    list = {}

    # For generate random nick
    _last_id = 0

    def __init__(self):
        pass

    def create_user(self, sck):
        """
        :type sck: socket
        """

        user = UserThread(sck)

        nick = user.nick = self.generate_random_nick()

        self.list[nick] = user

        user.setDaemon(True)

        user.start()

    def kill_user(self, user_nick):
        """
        :type user_nick: str
        """

        # TODO A bug is here! When user quit, then an error here!
        if self.is_user(user_nick):
            self.list[user_nick].user_socket.close()
            self.list[user_nick].keep_running = False
        #   self.list[user_nick].join()
            del self.list[user_nick]

    def is_user(self, user_nick):
        return user_nick in self.list

    def generate_random_nick(self):

        self._last_id += 1
        last_id = self._last_id
        user_name = lang.create_clause('random_user_name', last_id)

        while user_name in self.list:
            self._last_id += 1
            last_id = self._last_id
            user_name = lang.create_clause('random_user_name', last_id)

        return user_name

    def broadcast(self, message):
        """
        Message to all users.
        :type message: str
        """

        for user in self.list:
            user.send_text(message)
        pass

users = UserList()