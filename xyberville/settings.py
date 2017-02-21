"""
Django settings for xyberville project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(SETTINGS_DIR)
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^=gelp_)v^^=0o5*4bi!huic(0*a2m$l7+i-&+7j$$5zsv%rn^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'dal',
    'dal_select2',
    'dal_queryset_sequence',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sorl.thumbnail',
    'pipeline',
    'django_extensions',
    'favicon',

    'xyberville.apps.users',
    'xyberville.apps.keluarga',
    'xyberville.apps.pekerjaan',
    'xyberville.apps.profiles',
    'xyberville.apps.permissions',
    'xyberville.apps.logs',
    'xyberville.apps.regions',
    'xyberville.apps.products',
    'xyberville.apps.sales',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'xyberville.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

WSGI_APPLICATION = 'xyberville.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'users.User'
CACHED_AUTH_PREPROCESSOR = \
    'xyberville.apps.users.models.cached_auth_preprocessor'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'id-ID'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


FIXTURE_DIRS = ['fixtures']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = SETTINGS_DIR + '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_files"),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'STYLESHEETS': {
        'bootstrap': {
            'source_filenames': (
                'bower/AdminLTE/bootstrap/css/bootstrap.css',
            ),
            'output_filename': 'AdminLTE/bootstrap/css/bootstrap.css'
        },
        'adminLTE': {
            'source_filenames': (
                'bower/AdminLTE/dist/css/AdminLTE.css',
            ),
            'output_filename': 'AdminLTE/dist/css/AdminLTE.css'
        },
        'adminLTESkins': {
            'source_filenames': (
                'bower/AdminLTE/dist/css/skins/_all-skins.css',
            ),
            'output_filename': 'AdminLTE/dist/css/skins/_all-skins.css'
        },
        'dataTables': {
            'source_filenames': (
                'bower/AdminLTE/plugins/datatables/dataTables.bootstrap.css',
            ),
            'output_filename':
                'AdminLTE/plugins/datatables/dataTables.bootstrap.css'
        },
        'iCheck': {
            'source_filenames': (
                'bower/AdminLTE/plugins/iCheck/all.css',
            ),
            'output_filename': 'AdminLTE/plugins/iCheck/all.css'
        },
        'FontAwesome': {
            'source_filenames': (
                'bower/components-font-awesome/css/font-awesome.css',
            ),
            'output_filename': 'components-font-awesome/css/font-awesome.css'
        },
        'ionicons': {
            'source_filenames': (
                'bower/ionicons/css/ionicons.css',
            ),
            'output_filename': 'ionicons/css/ionicons.css'
        },
        'customSkin': {
            'source_filenames': (
                'css/skin.css',
            ),
            'output_filename': 'css/skin.css'
        },
        'jqueryuicss': {
            'source_filenames': (
                'bower/jquery-ui/themes/ui-lightness/jquery-ui.css',
            ),
            'output_filename': 'jquery-ui/themes/ui-lightness/jquery-ui.css'
        },
        'themeroller': {
            'source_filenames': (
                'jqueryui_custom_theme/jquery-ui.theme.css',
            ),
            'output_filename': 'jqueryui_custom_theme/jquery-ui.theme.css'
        },
        'cropper': {
            'source_filenames': (
                'bower/cropper/dist/cropper.css',
            ),
            'output_filename': 'cropper/dist/cropper.css'
        },
        'select2': {
            'source_filenames': (
                'bower/select2/dist/css/select2.css',
            ),
            'output_filename': 'select2/dist/css/select2.css'
        },
        'datepicker': {
            'source_filenames': (
                'bower/AdminLTE/plugins/datepicker/datepicker3.css',
            ),
            'output_filename': 'AdminLTE/plugins/datepicker/datepicker3.css'
        },
    },
    'JAVASCRIPT': {
        'jquery': {
            'source_filenames': (
                'bower/jquery/dist/jquery.js',
            ),
            'output_filename': 'jquery/dist/jquery.js',
        },
        'jqueryui': {
            'source_filenames': (
                'bower/jquery-ui/jquery-ui.js',
            ),
            'output_filename': 'jquery-ui/jquery-ui.js'
        },
        'bootstrap': {
            'source_filenames': (
                'bower/AdminLTE/bootstrap/js/bootstrap.js',
            ),
            'output_filename': 'AdminLTE/bootstrap/js/bootstrap.min.js'
        },
        'slimscroll': {
            'source_filenames': (
                'bower/AdminLTE/plugins/slimScroll/jquery.slimscroll.min.js',
            ),
            'output_filename':
                'AdminLTE/plugins/slimScroll/jquery.slimscroll.min.js'
        },
        'fastclick': {
            'source_filenames': (
                'bower/AdminLTE/plugins/fastclick/fastclick.min.js',
            ),
            'output_filename': 'AdminLTE/plugins/fastclick/fastclick.min.js'
        },
        'app': {
            'source_filenames': (
                'bower/AdminLTE/dist/js/app.min.js',
            ),
            'output_filename': 'AdminLTE/dist/js/app.min.js'
        },
        'dataTables': {
            'source_filenames': (
                'bower/AdminLTE/plugins/datatables/jquery.dataTables.min.js',
            ),
            'output_filename':
                'AdminLTE/plugins/datatables/jquery.dataTables.min.js'
        },
        'dataTablesBootstrap': {
            'source_filenames': (
                'bower/AdminLTE/plugins/datatables/dataTables.bootstrap.min.js',
            ),
            'output_filename':
                'AdminLTE/plugins/datatables/dataTables.bootstrap.min.js'
        },
        'iCheck': {
            'source_filenames': (
                'bower/AdminLTE/plugins/iCheck/icheck.js',
            ),
            'output_filename': 'AdminLTE/plugins/iCheck/icheck.js'
        },
        'cropper': {
            'source_filenames': (
                'bower/cropper/dist/cropper.js',
            ),
            'output_filename': 'cropper/dist/cropper.js'
        },
        'select2': {
            'source_filenames': (
                'bower/select2/dist/js/select2.full.js',
            ),
            'output_filename': 'select2/dist/js/select2.full.js'
        },
        'datepicker': {
            'source_filenames': (
                'bower/AdminLTE/plugins/datepicker/bootstrap-datepicker.js',
            ),
            'output_filename': 'AdminLTE/plugins/datepicker/bootstrap-datepicker.js'
        },
    }
}

# Caches Redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'TIMEOUT': 3699 * 24,  # 1 day
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'log': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'TIMEOUT': None,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

FAVICON_CONFIG = {
    'shortcut icon': [16 ,32 ,48 ,128, 192],
    'touch-icon': [196],
    'icon': [196],
    'apple-touch-icon': [57, 72, 114, 144, 180],
    'apple-touch-icon-precomposed': [57, 72, 76, 114, 120, 144, 152,180],
}

# Configuring LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    "formatters": {
        "post_office": {
            "format": "[%(levelname)s]%(asctime)s PID %(process)d: %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        'simple': {
            'format': '[%(levelname)s]%(asctime)s PID %(process)d: %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S',
        },
    },
    'handlers': {
        'stdout': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        "post_office": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "post_office"
        }
    },
}


if 'test' in os.sys.argv:
    TEST = True
else:
    TEST = False

try:
    from settings_local import *
except ImportError:
    pass
