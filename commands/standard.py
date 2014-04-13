__author__ = 'kalaomer'

from lib import lang

commands = {}


def broadcast(user, command, ignore=None, send_user=False):
    from lib.users import users

    if ignore is None:
        ignore = []

    if send_user is False:
        ignore.append(user.nick)

    for _nick in users.list:
        if not _nick in ignore:
            users.list[_nick].send_text(lang.create_clause('broadcast', user.nick, command))

broadcast.info = """Broadcast function is for send message to anyone.

Exp: /broadcast Hi!
"""

commands['broadcast'] = broadcast


# This command send text to another person, not for anyone
def message(user, command):
    pass

message.info = """

"""

commands['msg'] = message


# This function name is _help, because help is used.
def _help(user, command):
    from commands.manager import command_manager

    if command == "":
        return user.send_text(_help.info)

    if command_manager.is_command(command) is True:
        command_function = command_manager.commands[command]

        if hasattr(command_function, 'info'):
            user.send_text(lang.create_clause('help_command_info', command, command_function.info))
        else:
            user.send_text(lang.create_clause('help_command_info_not_set', command))
    else:
        user.send_text(lang.create_clause('wrong_command_name', command))

_help.info = """
Welcome to Gabby! This tool is for communication.

You can get command list with '/commands' clause!
"""

commands['help'] = _help


def command_list(user, command):
    from commands.manager import command_manager
    user.send_text(lang.create_clause('command_list', '\n'.join(command_manager.commands)))

command_list.info = """
List all Commands!
"""

commands['commands'] = command_list


def change_user_name(user, command):
    from lib.users import users
    import re

    pattern = re.compile('^(?P<nick>[a-z0-9\-_]+)$')

    result = pattern.match(command)

    try:

        nick = result.group('nick')

        if len(nick) > 12:
            raise Exception()

        if nick in users.list.keys():
            return user.send_text(lang.create_clause('Wrong_nick_being_used'))

        del users.list[user.nick]

        users.list[nick] = user
        user.nick = nick

        user.send_text(lang.create_clause('new_user_name', nick))
    except:
        return user.send_text(lang.create_clause('wrong_nick_change'))

commands['change-name'] = change_user_name