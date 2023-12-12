"""
WSGI config for blango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
""" import django config first"""
# from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application


#only use in production env, import module before the package
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blango.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

application = get_wsgi_application()
