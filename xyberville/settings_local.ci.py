TEST = True
DEBUG = True
PIPELINE_ENABLED = False
RAVEN_CONFIG = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'circle_ci',
        'USER': 'ubuntu',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
