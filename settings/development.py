# Uncomment to put the application in non-debug mode. This is useful
# for testing error handling and messages.
DEBUG = False
TEMPLATE_DEBUG = DEBUG

FORCE_SCRIPT_NAME = '/harvest-site'

DATABASES = {'default': {'ENGINE': 'django.db.backends.dummy'}}
