from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'supersecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
