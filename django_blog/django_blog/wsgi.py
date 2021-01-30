"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('DJANGO_BLOG_PROFILE', 'django_blog.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'django_blog.settings.{profile}')

application = get_wsgi_application()
