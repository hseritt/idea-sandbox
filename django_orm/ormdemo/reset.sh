#!/usr/bin/env bash

rm -rf db.sqlite3
rm -rf demoapp/__py_cache__
rm -rf demoapp/migrations
rm -rf ormdemo/__py_cache__

./manage.py makemigrations demoapp
./manage.py migrate
./manage.py createsuperuser --noinput --username admin --email admin@localhost

./add_cars.py
