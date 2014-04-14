#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

import settings

import time

from lib import lang

from commands.manager import command_manager


class UserThread(threading.Thread):

    # User nick.
    nick = ''

    # User current data for commands!
    data = {}

    def __init__(self, user_socket):
        threading.Thread.__init__(self)
        self.user_socket = user_socket

    def run(self):
        connected = True

        self.send_text(lang.get_welcome(self.nick))

        while connected:
            time.sleep(0.1)
            text = self.receive()
            self.run_command(text)

    def run_command(self, command_text):
        return command_manager.execute(self, command_text)

    def send(self, bytes):
        """
        :type bytes: bytearray
        """
        self.user_socket.sendall(bytes)

    def send_text(self, text):
        """
        :type text: str
        """
        text += "\n"
        self.user_socket.send(text.encode(errors='ignore'))

    # seppuku!
    def close(self):
        from lib.users import users
        users.kill_user(self.nick)

    # return utf-8 text!
    def receive(self):
        message = self.user_socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
        if not message:
            # Empty string is given on disconnect.
            self.close()
        else:
            return message.strip().decode('utf-8', 'ignore')
