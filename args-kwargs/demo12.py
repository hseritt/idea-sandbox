#!/usr/bin/env python

def do_something_with_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

    print(*kwargs)


if __name__ == '__main__':

    do_something_with_kwargs(name='Bill', age=30)
