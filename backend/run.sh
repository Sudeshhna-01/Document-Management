#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server on port 8001
python manage.py runserver 8001 