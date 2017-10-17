#!/usr/bin/env python

from collections import deque
import timeit

with open('ipsum.txt', 'r') as f:
    lines = f.readlines()

def test_list():
    line_list = [line for line in lines] 

def test_tuple():
    line_list = [line for line in tuple(lines)]

def test_deque():
    line_list = [line for line in deque(lines)]


if __name__ == '__main__':
    
    print(
        'Testing list: {} ms'.format(
            timeit.timeit(
                'test_list()', setup='from __main__ import test_list', number=10000
            )
        )
    )

    print(
        'Testing tuple: {} ms'.format(
            timeit.timeit(
                'test_tuple()', setup='from __main__ import test_tuple', number=10000
            )
        )
    )

    print(
        'Testing deque: {} ms'.format(
            timeit.timeit(
                'test_deque()', setup='from __main__ import test_deque', number=10000
            )
        )
    )
