#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Trying to connect to the db..."
  sleep 0.1
done
echo "Connected to the db"

cd src/
alembic upgrade head

exec "$@"