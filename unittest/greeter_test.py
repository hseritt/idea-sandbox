#!/usr/bin/env python

import unittest
from app import Greeter, FINAL_GREETING, GREETING_TEXT


class GreeterTest(unittest.TestCase):
    """
    A test case for testing the Greeter class in app.py
    """

    def test_get_name_text(self):
        """
        Test that Greeter().get_name_text() returns the text 
        from Greeter().GREETER_TEXT.
        """
        greeter = Greeter()
        text = greeter.get_name_text()
        self.assertEqual(text, GREETING_TEXT)

    def test_get_name(self):
        """
        Test that Greeter().get_name() returns a string that 
        could read as a person's name.
        """
        greeter = Greeter()
        name = greeter.get_name()
        """ Enter Bob """
        self.assertEqual(name, 'Bob')

    def test_get_greeting(self):
        """
        Test that Greeter().get_greeting() returns a greeting with
        Greeter().FINAL_GREETING and the name in it.
        """
        greeter = Greeter()
        name = greeter.get_name()
        """ Enter Bob """
        greeting = greeter.get_greeting(name)
        self.assertEqual(
            greeting, FINAL_GREETING.format(name)
        )

    def test_is_greeted(self):
        """
        Test that the user's name was stored as one who was greeted.
        """
        greeter = Greeter()
        name = greeter.get_name()
        """ Enter Bob """
        greeting = greeter.get_greeting(name)
        self.assertTrue(greeter.is_greeted(name))


if __name__ == '__main__':
    unittest.main()
