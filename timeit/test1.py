#!/usr/bin/env python

import timeit

with open('ipsum.txt', 'r') as f:
    lines = f.readlines()

def test_list():
    line_list = [line for line in lines]


if __name__ == '__main__':
    
    print(
        'Testing list: {} ms'.format(
            timeit.timeit(
                'test_list()', setup='from __main__ import test_list', number=10000
            )
        )
    )
