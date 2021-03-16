# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

from .common import *  # noqa
import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

INTERNAL_IPS = []

ALLOWED_HOSTS = ['grabovsky.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}

# WhiteNoise
WHITENOISE_MAX_AGE = 3600  # Time (in seconds) for which browsers and proxies should cache non-versioned files  # noqa
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
