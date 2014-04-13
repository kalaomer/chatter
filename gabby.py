#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib.server import Server


class Gabby(Server):
    VERSION = "0.0.1"
    pass

if __name__ == "__main__":

    # Create Gabby.
    gabby = Gabby()

    """
    RUN FOREST, RUN!
    DON'T LOOK YOUR BACK!
    """
    gabby.run()
