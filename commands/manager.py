#!/usr/bin/python
# -*- coding: utf-8 -*-

#from lib.user import UserThread
from lib import lang
import re

from commands import standard
from lib.logger import logger


class CommandManager():

    commands = {}

    def __init__(self):
        self.load_commands()

    # Load commands from command folder.
    def load_commands(self):
        for command in standard.commands:
            self.add_command(command, standard.commands[command])

    def add_command(self, command_name, function):
        if command_name in self.commands.keys():
            raise Exception('Command was loaded!', {'command': command_name})

        self.commands[command_name] = function

    # Run command!
    def execute(self, user, command_clause):
        """
        :param command_clause: Command Bytes!
        :param user: Command sender
        :type command_clause: str
        :type user: UserThread
        """

        command_template = self.parse_command_clause(command_clause)

        if command_template is False:
            command_template = ['broadcast', command_clause]
            #return self.send_error(user, 'wrong_command_clause', command_clause)

        if self.is_command(command_template[0]) is False:
            return self.send_error(user, 'wrong_command_name', command_template[0])

        return self.run(user, command_template[0], command_template[1])

    def run(self, user, command_name, command_text):
        return self.commands[command_name](user, command_text)

    def is_command(self, command):
        """
        Is this command?
        """
        return command in self.commands

    @staticmethod
    def send_error(user, template, *args, **kwargs):
        """
        :type template: str
        :type user: UserThread
        """

        error_clause = lang.create_clause(template, *args)
        """
        if 'log' in kwargs:
            if kwargs['log'] is True:
                gabby.logger.warning(error_clause)
        """
        user.send_text(error_clause)

    # noinspection PyBroadException
    @staticmethod
    def parse_command_clause(command) -> [] or False:
        """
        :type command: str
        """

        pattern = re.compile('^/(?P<command>[a-zA-Z0-9\-_]+)\s?(?P<end>.*)?')

        parse = pattern.match(command)

        try:
            return [parse.group('command'), parse.group('end')]
        except:
            return False


command_manager = CommandManager()
