from .common import *  # noqa

INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')  # noqa

SECRET_KEY = 'dev_key'

DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa
    }
}
