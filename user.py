#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

import settings

import time

class UserThread(threading.Thread):
    def __init__(self, user_socket, server):
        threading.Thread.__init__(self)
        self.user_socket = user_socket
        self.server = server

    def run(self):
        connected = True

        text = self.receive()
        while connected:

            time.sleep(0.1)

            if text in ["\quit"]:
                self.send('you shall never be forgotten!')
                connected = False
                break
            elif self.is_name_command(text):
                self.update_name(text.split(" ")[1])
                self.send('you are now known as \'%s\'' % self.getName())
            else:
                self.broadcast('%s: %s' % (self.getName(), text))

            text = self.receive()

        self.kill_thread()

    def update_name(self, new_name):
        del self.server.users[self.getName()]

        self.setName(new_name)
        self.server.users[self.getName()] = self

    def send(self, text):
        text = text + "\n"
        self.user_socket.send(text.encode())

    def broadcast(self, text):
        for name in self.server.users.keys():
            if name != self.getName():
                self.server.users[name].send(text)
            #    print("%s is say to %s this message %s" % (self.getName(), name, text.strip()))

    # seppuku!
    def kill_thread(self):
        self.user_socket.close()
        del self.server.users[self.getName()]
        self._stop()

    # return utf-8 text!
    def receive(self):
        message = self.user_socket.recv(settings.SERVER.MAX_PACKAGE_SIZE)
        if not message:
            # Empty string is given on disconnect.
            self.kill_thread()
        else:
            return message.strip().decode('utf-8')

    @staticmethod
    def is_name_command(text):
        if text[:5] == "name ":
            return len(text.split(" ")[1]) > 0
        else:
            return False
