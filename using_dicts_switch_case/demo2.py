#!/usr/bin/env python


def double(num):
    return num * 2


def triple(num):
    return num * 3


def add(*args, f=None):
    if f:
        return f(sum(args))
    else:
        return sum(args)


if __name__ == '__main__':
    print(add(5, 3, 2, 1))
    print(add(5, 3, 2, 1, f=double))
    print(add(5, 3, 2, 1, f=triple))
