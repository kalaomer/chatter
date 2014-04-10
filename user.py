#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

import settings

import time

class UserThread(threading.Thread):
    def __init__(self, user_socket, server):
        threading.Thread.__init__(self)
        self.user_socket = user_socket
        self.name = None
        self.server = server

    def run(self):
        connected = True

        text = self.receive()
        while connected:

            time.sleep(0.1)

            if text in ["quit", "bye"]:
                self.send('you shall never be forgotten!')
                connected = False
            elif self.is_name_command(text):
                self.name = text.split(" ")[1]
                self.send("you are now known as '%s'" % self.name)
            else:
                name = "" if not self.name else self.name
                self.send_all("%s: %s" % (name, text))

            text = self.receive()

        self.user_socket.close()

    def send(self, text):
        self.user_socket.send(text.strip() + "\n")

    def send_all(self, text):
        for name in self.server.users.keys():
            if name != self.getName():
                self.server.users[name].send(text.strip() + "\n")

    def receive(self):
        result = self.user_socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
        if result:
            result = result.strip()
        return result

    @staticmethod
    def is_name_command(text):
        if text > 5 and text[:5] == "name ":
            return len(text.split(" ")[1]) > 0
        else:
            return False
