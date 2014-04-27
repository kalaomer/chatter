__author__ = 'kalaomer'


class Command():

    arguments = []

    name = "command"

    command_manager = ""

    def __init__(self, command_manager):
        self.command_manager = command_manager
        pass

    def active(self):
        self.command_manager.add_command(self)
        pass

    def passive(self):
        pass

    def run(self, command_clause):
        pass