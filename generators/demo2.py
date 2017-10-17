#!/usr/bin/env python

def big_range(n):
    num = 0
    while num < n:
        yield num
        num += 1


if __name__ == '__main__':

    s = sum(big_range(100000000))
