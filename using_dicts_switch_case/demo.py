#!/usr/bin/env python

def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

func = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


if __name__ == '__main__':

    print(func['+'](5, 4, 2))
    print(func['-'](5, 3, 1))
    print(func['*'](3, 2, 2))
    print(func['/'](24, 3, 2))
