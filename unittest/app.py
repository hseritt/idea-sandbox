#!/usr/bin/env python
"""
A simple greeting app as a module.
"""

GREETING_TEXT = 'Hi, what is your name? '
FINAL_GREETING = 'Hello {}, it is nice to meet you!'

class Greeter(object):
    """
    A Greeter class. Takes input as the user's name
    and sends a greeting back to the user.
    """

    greeted = []
    """ Storage for user's names who have been greeted. """
    
    def get_name_text(self):
        """
        Returns a string that is a request for the user's name.
        """
        return GREETING_TEXT

    def get_name(self):
        """
        Gets the name of the user via console input and 
        returns as a string.
        """
        name = input(self.get_name_text())
        return name

    def get_greeting(self, name):
        """
        Returns a greeting to the user with a greeting string
        and user's name added.
        """
        self.greeted.append(name)
        return FINAL_GREETING.format(name)

    def is_greeted(self, name):
        """
        Returns a boolean that affirms if the user has 
        been greeted before.
        """
        return name in self.greeted

    def run(self):
        print(self.get_greeting(self.get_name()))


if __name__ == '__main__':

    greeter = Greeter()
    greeter.run()
