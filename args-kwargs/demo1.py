#!/usr/bin/env python

def do_something_with_args(name, *args, show_args=False):

    print('Greetings, {}'.format(name))

    if show_args and args:
        print('Here are the args:')
        for arg in args:
            print(arg)
        print('\n')


def do_something_with_kwargs(name, show_args=False, **kwargs):

    print('Greetings, {}'.format(name))

    if show_args and kwargs:
        print('Here are the kwargs:')
        for key, value in kwargs.items():
            print('Key: {} Value: {}'.format(key, value))
        print('\n')


if __name__ == '__main__':
    
    # do_something_with_args('Dave')
    
    # do_something_with_args('Dave', show_args=True)
    
    """
    do_something_with_args(
        'Dave',
        'arg1',
        'arg2',
        'arg3',
        show_args=True,
    )
    """

    # do_something_with_kwargs('Dave')

    # do_something_with_kwargs('Dave', show_args=True)

    #"""
    do_something_with_kwargs(
        'Dave',
        show_args=True,
        arg1='arg1 value',
        arg2='arg2 value',
        arg3='arg3 value',
    )
    #"""
