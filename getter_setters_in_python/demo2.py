#!/usr/bin/env python

class Thing(object):

    def __init__(self, x):
        self.x = x

if __name__ == '__main__':

    thing = Thing(42)
    print(thing.x)

    thing.x = 25
    print(thing.x)
