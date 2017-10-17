#!/usr/bin/env python

def multiply(multiplier=2):
    def decorator(func):
        def wrapper(num1, num2):
            print('Before ...')
            print('Calculating ...')
            d = func(num1, num2) * multiplier
            print('After ...')
            return d
            
        return wrapper
    return decorator

@multiply(3)
def addnums(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    print(addnums(3, 5))
