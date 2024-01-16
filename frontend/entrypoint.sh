#!/bin/bash
set -e

# Wait for MySQL to be ready
/wait-for-it.sh db:3306 -t 60

# Start your Flask application
exec uwsgi --ini /app/uwsgi.ini
