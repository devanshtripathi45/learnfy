#!/bin/bash

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server
gunicorn learnify.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
