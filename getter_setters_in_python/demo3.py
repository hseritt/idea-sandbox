#!/usr/bin/env python

class Thing(object):

    def __init__(self, x):
        self.__x = x 

    @property
    def x(self):
        return self.__x

    # This will only work with a private member.
    # Otherwise, we will see a recursion error.
    @x.setter
    def x(self, x):
        if x % 2 == 1:
            x += 1
        self.__x = x


if __name__ == '__main__':

    thing = Thing(42)
    print(thing.x)
    thing.x = 25
    print(thing.x)
