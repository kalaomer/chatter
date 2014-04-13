#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import socket


class UserList():

    # UserThread Objects
    list = {}

    def __init__(self):
        pass

    def create_user(self, client):
        """
        :type client: socket
        """

        pass

    def broadcast(self, message):
        """
        Message to all users.
        :type message: str
        """

        for user in self.users:
            user.send_text(message)
        pass

    def get_user(self, id):
        pass

    def kill_user(self):
        pass

users = UserList()