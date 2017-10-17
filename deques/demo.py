#!/usr/bin/env python

from collections import deque

my_deque = deque('long')
print(type(my_deque))
print(my_deque)

####

my_deque.append('d')
my_deque.appendleft('s')

my_deque.append('e')
my_deque.appendleft('i')

my_deque.append('q')
my_deque.appendleft('h')

my_deque.append('u')
my_deque.appendleft('t')

my_deque.append('e')
print(my_deque)

####

deque_copy = my_deque.copy()
print(deque_copy)

####

deque_copy.clear()
print(deque_copy)

####

print(my_deque.count('e'))

###

deque_copy = my_deque.copy()
deque_copy.extend('right')

print(deque_copy)

deque_copy.extendleft('left')

print(deque_copy)

####

print(deque_copy.index('o'))

try:
	print(deque_copy.index('b'))
except ValueError as err:
	print(repr(err))

####

print(deque_copy)

deque_copy.insert(5, 'z')
print(deque_copy)

print(len(deque_copy))

deque_copy.insert(50, 'X')
print(deque_copy)

####

new_deque = deque('abcde', 5)
print(new_deque)

new_deque.append('f')
print(new_deque)

new_deque.appendleft('a')
print(new_deque)

####

popped = new_deque.pop()
print(popped)
print(new_deque)

popped = new_deque.popleft()
print(popped)
print(new_deque)

new_deque.remove('c')
print(new_deque)

try:
	new_deque.remove('a')
except ValueError as err:
	print(repr(err))

####

new_deque = deque('abcde')
print(new_deque)
new_deque.reverse()
print(new_deque)

new_deque.reverse()

for i in range(len(new_deque)):
	new_deque.rotate(1)
	print(new_deque)

###

limited_deque = deque('abcde', 5)
print(limited_deque.maxlen)
print(new_deque.maxlen)








































