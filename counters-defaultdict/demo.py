#!/usr/bin/env python

from collections import Counter


my_file = 'gettysburg_address.txt'

words = [ word.lower() for word in open(my_file, 'r').read().split() if '-' not in word ]

print(type(words))

word_counter = Counter(words)

for k, v in word_counter.items():
	print(k, v)

for each in word_counter.most_common()[:10]:
	k, v = each
	print('Word: {} | {}'.format(k, v))

c = Counter('abcd')
print(c['e'])

c = Counter(a=1, b=2, c=3, d=4, e=5)
print(c)

elements = c.elements()
for element in elements:
	print(element)

d = Counter(a=0, b=1, c=2, d=3, e=4)
c.subtract(d)
print(c)

from collections import defaultdict

s = [('yours', 1), ('mine', 2), ('yours', 3), ('mine', 4), ('yours', 1)]
d = defaultdict(list)
for k, v in s:
     d[k].append(v)

sorted(d.items())

print(d)
