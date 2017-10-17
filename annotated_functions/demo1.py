#!/usr/bin/env python


def general_func(num1: int, num2: str) -> str:
    assert isinstance(num1, int), 'num1 not an integer'
    assert isinstance(num2, str), 'num2 not a string'

    ret_val = '{}{}'.format(num1, num2)
    assert isinstance(ret_val, str), 'ret_val not a string'

    return ret_val


class MyClass(object):

    def __init__(self, data: str):
        self.data = data

    def do_something_with_data(self) -> None:
        self.data = self.data[::-1]
        self.data = self.data[:-1]

    def get_data(self) -> str:
        return self.data


if __name__ == '__main__':

    print(general_func('5', '5'))

    myclass = MyClass('blahblah')
    myclass.do_something_with_data()
    print(myclass.get_data())

    myclass = MyClass(789)
    print(myclass.get_data())

