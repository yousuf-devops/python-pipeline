#!/bin/bash
cd /home/ubuntu/flask-cicd-app
source venv/bin/activate
gunicorn --bind 0.0.0.0:5000 --workers 3 --daemon app:app
echo "Application started with Gunicorn"
