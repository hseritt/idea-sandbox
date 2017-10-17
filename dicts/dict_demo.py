#!/usr/bin/env python

person_a = {
	'Name': 'John Doe',
	'Age': 30,
	'Hair color': 'brown',
}

person_b = {
	'Nationality': 'American',
	'Education level': 'BS - Computer Science',
}

person = {**person_a, **person_b}

for k, v in person.items():
	print('{}: {}'.format(k, v))

# for Python 2.7:

person = dict(person_a, **person_b)

for k, v in person.items():
	print('{}: {}'.format(k, v))


scores = {
	'Mike': 75,
	'Phil': 90,
	'Bill': 85,
	'Larry': 71,
	'Glenn': 99,
	'Maria': 80,
	'Rosa': 77,
}

import operator

score_list = sorted(scores.items(), key=operator.itemgetter(1))

for k, v in score_list:
	print(k, v)

score_list.reverse()

for k, v in score_list:
	print(k, v)
