#!/usr/bin/env python


def subtract(num1, num2):
    return num1 - num2


func = {
    '-': subtract,
}


if __name__ == '__main__':

    diff = func['-'](6, 3)

    print(diff)
