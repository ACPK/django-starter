import os

import dj_database_url

from .common import *

DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_DEFAULT_FROM')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# May need these for newer S3 regions
# AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
# AWS_S3_SIGNATURE_VERSION = os.envi.get('AWS_S3_SIGNATURE_VERSION')

# ===== Celery and AMQP
BROKER_URL = os.environ.get('AMQP_URL')
# # Producers
# RABBITMQ_BIGWIG_RX_URL = os.environ.get('RABBITMQ_BIGWIG_RX_URL')
# # Consumers
# RABBITMQ_BIGWIG_TX_URL = os.environ.get('RABBITMQ_BIGWIG_TX_URL')