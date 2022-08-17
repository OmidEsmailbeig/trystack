from os import environ

class Config:
    ENV = environ.get('TRYSTACK_API_ENV', 'production')
    DEBUG = environ.get('TRYSTACK_API_DEBUG', '0')
    TESTING = DEBUG
