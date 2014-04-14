#!/usr/bin/python
# -*- coding: utf-8 -*-

import settings

# Out templates
templates = {

    # When user connect server!
    'welcome':
        """
===============================================

Welcome to {0},
Please ENJOY!
Your current name is '{1}'

If you want to help, please tell me /help

================================================
        """,

    # When user change own name.
    'new_user_name':
        """
>>Your name has been changed!
>>Your current name is '{0}'.
        """,

    # Online user count.
    'online_user_count':
        """
{0} people online now!
        """,

    'message':
        '@{0}: {1}',

    'broadcast':
        '{0}: {1}',

    'disconnect_message':
        '<{0} is disconnected.>',

    'connected_message':
        '<{0} is connected>',

    'wrong_command_clause':
        '<Wrong Command Clause! Clause: \'{0}\'>',

    'wrong_command_name':
        '<Wrong Command Name! Command: \'{0}\'>',

    'random_user_name':
        'user_{0}',

    'help_command_doc':
        """
<Command help for \'{}\'>
{}
        """,

    'help_command_doc_not_set':
        '<Command help for \'{}\' info is None>',

    'command_list':
        """
<Command list>
{}
        """,

    'wrong_nick_change':
        '<Wrong nick! Nick name can only have a-z, 0-9, -, _ and max 12 char!>',

    'wrong_nick_being_used':
        '<Nick can\'t change, because it is being used! Tyr another one.>',

    'quit':
    """
Goodbye {}, we shall never forget you!
    """

}


def create_clause(template_name, *args):
    """
    :type template_name: str
    """
    if template_name in templates.keys():
        return (templates[template_name].format(*args)).strip()

    raise Exception("Unknown template!")


def get_welcome(user_name):
    return create_clause('welcome', settings.SERVER.NAME, user_name)
