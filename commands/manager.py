#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib.user import UserThread
import re


class CommandManager():

    commands = {}

    # Load commans from command folder.
    def load_commands(self):
        pass

    # Run command!
    def run(self, command_clause, user):
        """
        :param command_clause: Command Bytes!
        :param user: Command sender
        :type command_clause: str
        :type user: UserThread
        """

        command_template = self.parse_command_clause(command_clause)

        if False == command_template:
            self.error(user, 'wrong_clause', Exception(command_clause))
            command_template = ['error', 'wrong_clause']

        if False == CommandManager.is_command(command_template[0]):
            command_template = ['error', 'wrong_command', command_template[0]]

        CommandManager.commands[command_template[0]](user, command_template[0])

    def is_command(command):
        """
        Is this command?
        """
        return command in CommandManager.commands

    def error(self, user, template, Exc):
        """
        :type template: str
        :type Exc: Exception
        """

        Exception("asd")

    @staticmethod
    def parse_command_clause(command):
        """
        :type command: str
        """
    #    command = command_binary.decode('utf-8', 'ignore')

        pattern = re.compile('^\/(?P<command>\w+)\s(?P<end>.*)')

        parse = pattern.match(command)

        try:
            return [parse.group('command'), parse.group('end')]
        except:
            return False