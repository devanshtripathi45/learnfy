"""
ASGI config for learnify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnify.settings')

application = get_asgi_application()

# Log current DEBUG and ALLOWED_HOSTS so deployment logs show the active settings.
import logging
try:
	from django.conf import settings as _settings
	logger = logging.getLogger('learnify.startup')
	logger.info('Django startup - DEBUG=%s, ALLOWED_HOSTS=%s', _settings.DEBUG, _settings.ALLOWED_HOSTS)
except Exception:
	logging.getLogger('learnify.startup').exception('Failed to log startup settings')
