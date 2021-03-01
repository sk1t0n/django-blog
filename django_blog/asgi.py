"""
ASGI config for django_blog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

DJANGO_SETTINGS_MODULE = os.environ.get(
    'DJANGO_SETTINGS_MODULE', 'django_blog.settings.production'
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

application = get_asgi_application()
