#!/bin/bash

# collect static files and migrate
python manage.py collectstatic --noinput
#python manage.py migrate

# start gunicorn server
gunicorn devskills.wsgi:application --bind 0.0.0.0:8000 --workers 3
