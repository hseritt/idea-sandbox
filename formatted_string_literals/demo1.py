#!/usr/bin/env python

# Old Style

my_str = 'This is a %s sentence.' % ('short',)
print(my_str)

my_str = 'This is a {} sentence too.'.format('short')
print(my_str)

my_str = 'This string has two values to show: {0} and {1}.'.format('short', 'long')
print(my_str)

my_str = 'We can also rearrange {1} and {0} and keep them ' \
    'in the same order in the format function.'.format('short', 'long')
print(my_str)

num1 = 10
num2 = 5
my_str = f'We can use named substitions too like these: {num1} and {num2}.'
print(my_str)



my_str = 'This is {name}. He is {age} years old. He stands {height}'
print(my_str.format(
        name='Bob',
        age=30,
        height='5 ft 8 inches',
    )
)

person = {
    'name': 'Bob',
    'age': 30,
    'height': '5 ft 8 inches',
}

print(my_str.format(**person))

my_str = 'This is {p[name]}. He is {p[age]} years old. He stands {p[height]}'
print(my_str.format(p=person))
