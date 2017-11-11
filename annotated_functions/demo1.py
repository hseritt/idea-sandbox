#!/usr/bin/env python


class Thing(object):
    def __init__(self, name: str, num: int) -> None:
        assert isinstance(name, str), 'name must be of type str'
        assert isinstance(num, int), 'num must be of type int'
        self.name = name
        self.num = num

    def greet(self) -> str:
        greeting = f'Hello {self.name} it is nice to meet you! ' \
                   f'The number is {self.num}.'
        assert isinstance(greeting, str), 'greeting must be of type str'
        return greeting


if __name__ == '__main__':

    thing = Thing('You', 5)
    print(thing.greet())
