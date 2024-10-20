#!/bin/bash
echo "BUILD START"
python3.9 -m pip install --upgrade pip  # Ensure pip is up-to-date
python3.9 -m pip install -r requirements.txt  # Install requirements
python3.9 manage.py collectstatic --noinput --clear  # Collect static files
echo "BUILD END"
