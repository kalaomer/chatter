#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import logging

from settings import SERVER


logger = logging.getLogger("main")
logger.warning("Configuration")
logger.warning(SERVER)

clients = {}

server = Server()

print("Server is ready!")

