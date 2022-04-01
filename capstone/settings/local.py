from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    #  'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'cns-webpage',
    #     'USER': 'cgrs27',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sismosdb',
        'USER': 'postgres',
        'PASSWORD': 'Carlos1978_',
        'HOST': 'localhost',
    },
}

 
STATIC_URL = '/static/'