#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # Use netcat to wait for PostgreSQL to be ready
    # netcat-openbsd is already installed in the Dockerfile
    while ! nc -z $SQL_HOST $SQL_PORT; do
      echo "PostgreSQL is unavailable - sleeping for 1 second"
      sleep 1
    done

    echo "PostgreSQL started"
    
    # Additional wait to ensure database is fully ready
    sleep 2
fi

# Don't run migrations here - they will be run in the main command
# python manage.py migrate

exec "$@"
