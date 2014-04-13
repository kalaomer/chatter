__author__ = 'kalaomer'

from lib.users import users
from lib import lang

commands = {}


def broadcast(user, command, ignore=[]):

    for user in users.list:
        if user.name in ignore:
            user.send_text(command)

commands['broadcast'] = broadcast


def message(user, command):
    pass

commands['msg'] = message