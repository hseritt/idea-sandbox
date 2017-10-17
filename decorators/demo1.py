#!/usr/bin/env python

def multiply(func):
    def wrapper(num1, num2):
        print('Before ...')
        print('Calculating ...')
        d = func(num1, num2) * 2
        print('After ...')
        return d

    return wrapper

@multiply
def addnums(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    print(addnums(3, 5))
