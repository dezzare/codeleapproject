#!/bin/bash
set -e

echo "Running tests"
python manage.py test
echo "===========End Tests=============="

echo "Create Migrations"
python manage.py makemigrations codeleapapp
echo "=================================="

echo "Migrate"
python manage.py migrate
echo "=================================="

echo "Starting Server"
python manage.py runserver 0.0.0.0:8000