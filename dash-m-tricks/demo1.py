#!/usr/bin/env python


def my_func(a, b=2):
    """
    >>> my_func(5)
    10
    >>> my_func(5, 3)
    15
    >>> my_func('Hello')
    'HelloHello'
    """
    return a * b
