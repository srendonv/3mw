"""
WSGI config for srv_3megawatt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "srv_3megawatt.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
