#!/usr/bin/python
# -*- coding: utf-8 -*-

import settings

# Out templates
templates = {

    # When user connect server!
    'welcome':
        """
Welcome to %s,
Please ENJOY!
Your current name is '%s'

If you want to help, please tell me /help
""",

    # When user change own name.
    'new_user_name':
        """
Your name has been changed!
Your current name is '%s'.
""",

    # Online user count.
    'online_user_count':
        """
%d people online now!
""",

    # Message from someone for everyone!
    'message':
        '%s: %s',

    # Private message.
    'private_message':
        '%s>> %s',

    'disconnet_message':
        '<%s is disconnected.>',

    'connected_message':
        '<%s is connected>',

    'wrong_command':
        '<Wrong Command! Command: \'%s\''

}


def create_clause(template_name, *args):
    """
    :type template_name: str
    """
    if template_name in templates:
        return templates[template_name] % args

    raise Exception("Unknown template!")


def get_welcome(user_name):
    return create_clause('welcome', settings.SERVER.NAME, user_name)
