#!/usr/bin/env sh

python manage.py collectstatic
python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT
