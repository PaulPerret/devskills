from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECRET_KEY='your_secret_key'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or local Postgres
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}