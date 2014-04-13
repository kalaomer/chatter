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

        self.send_text(lang.get_welcome(self.nick))

    def run(self):
        connected = True

        text = self.receive()

        while connected:
            time.sleep(0.1)
            self.run_command(text)
            text = self.receive()

        users.kill_user(self.nick)

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
        self.user_socket.close()

    # return utf-8 text!
    def receive(self):
        message = self.user_socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
        if not message:
            # Empty string is given on disconnect.
            self.close()
        else:
            return message.strip().decode('utf-8', 'ignore')

    @staticmethod
    def is_name_command(text):
        if text[:5] == "name ":
            return len(text.split(" ")[1]) > 0
        else:
            return False
