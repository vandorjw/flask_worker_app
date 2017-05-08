import os

class Config(object):
    """Base configuration."""
    SECRET_KEY = os.environ.get('APP_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG = os.environ.get('DEBUG', False)

    SQS_REGION = os.environ.setdefault('SQS_REGION', 'us-west-2')
    SQS_QUEUE_NAME = os.environ.setdefault('SQS_QUEUE_NAME', '')
