#!/usr/bin/env python

from collections import namedtuple

Person = namedtuple('Person', 'name age hair_color')
me = Person('Harlin', 48, 'brown')

print(me.name, me.age, me.hair_color)

john = Person('John', 25, 'black')
print(john.name, john.age, john.hair_color)

"""
See https://www.zipinfo.com/products/z5/z5.htm#preferred
"""

Place = namedtuple(
    'Place', 'city state zipcode'
)

places = []

for line in open('places.txt', 'r').readlines():
    city, state, zipcode = [
        item for item in line.rstrip().split(',')
    ]

    places.append(Place(city, state, zipcode))

for place in places:
    print(place)
