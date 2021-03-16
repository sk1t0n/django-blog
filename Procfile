release: python manage.py migrate --settings django_blog.settings.production
web: gunicorn django_blog.wsgi --log-file -