#!/bin/bash
poetry shell
export $(grep -v '^#' .env | xargs)

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py test

gunicorn mypeeps.wsgi -b 0.0.0.0