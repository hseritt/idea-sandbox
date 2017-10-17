#!/usr/bin/env python

class Thing(object):

    def __init__(self, x):
        self.__x = x

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x


if __name__ == '__main__':

    thing = Thing(42)
    print(thing.get_x())

    thing.set_x(25)
    print(thing.get_x())
