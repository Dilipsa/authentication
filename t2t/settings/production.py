DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xyz',
        'USER': 'xyz',
        'PASSWORD': 'xyz',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = '/path/to/static_root/'
MEDIA_ROOT = '/path/to/media_root/'