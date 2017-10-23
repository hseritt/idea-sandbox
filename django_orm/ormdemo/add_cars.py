#!/usr/bin/env python

import os
import sys
import django


sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ormdemo.settings'
django.setup()

from django.contrib.auth.models import User
from demoapp.models import Car

if __name__ == '__main__':

    user = User.objects.get(username='admin')
    user.set_password('admin')
    user.save()

    car_list = [
        {
            'cmake': 'Hyundai',
            'cmodel': 'Excel',
            'trim': 'SE',
            'year': 1989,
            'price': 2000.00,
        },
        {
            'cmake': 'Hyundai',
            'cmodel': 'Excel',
            'trim': 'SE',
            'year': 1987,
            'price': 1500.00,
        },
        {
            'cmake': 'Pontiac',
            'cmodel': 'Sunbird',
            'trim': 'SE',
            'year': 1994,
            'price': 12000.00,
        },
        {
            'cmake': 'Pontiac',
            'cmodel': 'Grand AM',
            'trim': 'LX',
            'year': 1996,
            'price': 14500.00,
        },
        {
            'cmake': 'Hyundai',
            'cmodel': 'Excel',
            'trim': 'SE',
            'year': 1990,
            'price': 1200.00,
        },
        {
            'cmake': 'Mercury',
            'cmodel': 'Villager',
            'trim': 'LS',
            'year': 2003,
            'price': 11000.00,
        },
        {
            'cmake': 'Ford',
            'cmodel': 'Focus',
            'trim': 'S',
            'year': 2004,
            'price': 10000.00,
        },
        {
            'cmake': 'Honda',
            'cmodel': 'Accord',
            'trim': 'EX-L V6',
            'year': 2001,
            'price': 6500.00,
        },
        {
            'cmake': 'Toyota',
            'cmodel': 'Tacoma',
            'trim': 'TRD',
            'year': 2004,
            'price': 25000.00,
        },
        {
            'cmake': 'Jeep',
            'cmodel': 'Cherokee',
            'trim': 'Overland',
            'year': 2005,
            'price': 6500.00,
        },
        {
            'cmake': 'Toyota',
            'cmodel': '4Runner',
            'trim': 'SR5',
            'year': 2001,
            'price': 8000.00,
        },
    ]

    for car in car_list:
        c = Car()
        for k, v in car.items():
            setattr(c, k, v)
        print(f'Adding {c} ...')
        c.save()

    print('Done.')
