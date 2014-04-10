#!/usr/bin/python
# -*- coding: utf-8 -*-

class SERVER:
    HOST = 'localhost'
    PORT = 8088
    LISTEN = 4
    MAX_PACKAGE_SIZE = 1024

    def __init__(self):
        pass

    def __str__(self):
        template = "{0}:{1} LISTEN: {2} MAX_PACKAGE_SIZE:{3}"
        return template.format(self.HOST,
                               self.PORT,
                               self.LISTEN,
                               self.MAX_PACKAGE_SIZE)

