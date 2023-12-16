#!/bin/sh
echo "Connection to DB..."
while ! nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
  sleep .2s
done
echo "Connected!"
python ./films/manage.py makemigrations
python ./films/manage.py makemigrations filmsai_rest
python ./films/manage.py migrate
python ./films/manage.py migrate auth
python ./films/manage.py migrate filmsai_rest
python ./films/manage.py runserver 0.0.0.0:$SERVER_PORT
