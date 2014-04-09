#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

import settings


class User():
    def __init__(self, user_socket):
        self.user_socket = user_socket


    def listen(self):
        """
        This function runs in a thread
        """
        while True:
            try:
                message = self.user_socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
            except socket.error:
                break