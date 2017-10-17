#!/usr/bin/env python

def do_something_with_args(*args):
    print(args)
    print(type(args))

    print(*args)

    return sum(args)


if __name__ == '__main__':

    print(do_something_with_args(1, 3, 7))
