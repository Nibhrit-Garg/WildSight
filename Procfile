release: python manage.py makeigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn WildSight.wsgi