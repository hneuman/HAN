"""
WSGI config for proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
"""
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "han.settings")
"""
application = get_wsgi_application()

application = DjangoWhiteNoise(application)
"""

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise
import django.core.handlers.wsgi

application = get_wsgi_application()
application = DjangoWhiteNoise(application)


# This application object is used by the development server
# as well as any WSGI server configured to use this file.
#application = django.core.handlers.wsgi.WSGIHandler()