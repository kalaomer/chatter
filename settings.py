#!/usr/bin/python
# -*- coding: utf-8 -*-


class ServerConfiguration:
    HOST = ''
    PORT = 8088
    MAX_CONNECTION = 4
    MAX_PACKAGE_SIZE = 1024
    NAME = "Socivy"

    def __init__(self):
        pass

    def __str__(self):
        template = "[HOST:PORT] {0}:{1} LISTEN: {2} MAX_PACKAGE_SIZE:{3}"
        return template.format(self.HOST,
                               self.PORT,
                               self.MAX_CONNECTION,
                               self.MAX_PACKAGE_SIZE)


SERVER = ServerConfiguration()