#!/bin/sh

sleep 10

python manage.py flush --no-input
python manage.py makemigrations comments
python manage.py migrate

exec "$@"
