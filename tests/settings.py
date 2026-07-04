import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'test-secret-key'
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'badgify',
]

MIDDLEWARE = []

ROOT_URLCONF = 'tests.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
