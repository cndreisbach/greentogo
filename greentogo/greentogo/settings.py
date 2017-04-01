"""
Django settings for greentogo project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import environ
from django.contrib.messages import constants as messages

__root__ = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
# set default values and casting
__env__ = environ.Env(DEBUG=(bool, False), EMAIL_SECURE=(bool, True))

SITE_ROOT = __root__()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1+rc*=eii(d_im=1%x(q4di-_)14=ksa6u70nzs_h61m(+1zda'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = __env__('DEBUG')

ALLOWED_HOSTS = ['purchase.durhamgreentogo.com', 'greentogo.ngrok.io', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    # core
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "registration",  # third-party, needs to be above django.contrib.auth
    'django.contrib.auth',

    # third-party
    'compressor',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    "pinax.stripe",

    # wagtail
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.modeladmin',
    'wagtailmenus',
    'modelcluster',
    'taggit',

    # ours
    'beta_signup',
    'core',
    'apiv1',
    'cms',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

if not DEBUG:
    MIDDLEWARE += [
        'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    ]

ROOT_URLCONF = 'greentogo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

WSGI_APPLICATION = 'greentogo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {'default': __env__.db()}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authentication

AUTH_USER_MODEL = 'core.User'

# API

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', ),
    'DEFAULT_PERMISSION_CLASSES': (
        #        'rest_framework.permissions.IsAuthenticated',
        'apiv1.permissions.IsSubscriber',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(__root__.path("staticfiles/"))
STATICFILES_DIRS = [
    str(__root__.path('bower_components/')),
    str(__root__.path('greentogo/static/')),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = str(__root__.path("media/"))

# Django compressor

COMPRESS_PRECOMPILERS = (
    (
        'text/scss', 'node-sass ' +
        " ".join(["--include-path {}".format(d) for d in STATICFILES_DIRS]) + ' {infile}'
    ),
)

# Secret settings

GOOGLE_API_KEY = __env__('GOOGLE_API_KEY')

STRIPE_SECRET_KEY = __env__('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = __env__('STRIPE_PUBLISHABLE_KEY')

PINAX_STRIPE_PUBLIC_KEY = __env__('STRIPE_PUBLISHABLE_KEY')
PINAX_STRIPE_SECRET_KEY = __env__('STRIPE_SECRET_KEY')

# Email
EMAIL_HOST_USER = __env__('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD = __env__('EMAIL_PASSWORD')
EMAIL_HOST = __env__('EMAIL_SMTP_SERVER')
EMAIL_PORT = __env__('EMAIL_SMTP_PORT')
# EMAIL_USE_TLS = __env__('EMAIL_SECURE')
EMAIL_USE_SSL = __env__('EMAIL_SECURE')
EMAIL_REPLY_TO = __env__('EMAIL_REPLY_TO')
EMAIL_ADMINS = __env__('EMAIL_ADMINS')
if isinstance(EMAIL_ADMINS, str):
    EMAIL_ADMINS = EMAIL_ADMINS.split(",")
else:
    EMAIL_ADMINS = [EMAIL_REPLY_TO]

if len(EMAIL_ADMINS) == 1 and not EMAIL_ADMINS[0]:
    EMAIL_ADMINS = [EMAIL_REPLY_TO]

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            # Include the default Django email handler for errors
            # This is what you'd get without configuring logging at all.
            'mail_admins': {
                'class': 'django.utils.log.AdminEmailHandler',
                'level': 'ERROR',
                # But the emails are plain text by default - HTML is nicer
                'include_html': True,
            },
            # Log to a text file that can be rotated by logrotate
            'logfile': {
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': '/opt/greentogo/logs/django.log'
            },
        },
        'loggers': {
            # Again, default Django configuration to email unhandled exceptions
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            # Might as well log any errors anywhere else in Django
            'django': {
                'handlers': ['logfile'],
                'level': 'ERROR',
                'propagate': False,
            },
            # Your own app - this assumes all your logger names start with
            # "myapp."
            'greentogo': {
                'handlers': ['logfile'],
                'level': 'WARNING',  # Or maybe INFO or DEBUG
                'propagate': False
            },
        },
    }

ROLLBAR = {
    'access_token': __env__('ROLLBAR_KEY'),
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/opt/greentogo/src',
}

## Registration

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

## Message tags

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'primary',
    messages.ERROR: 'alert',
}

WAGTAIL_SITE_NAME = 'GreenToGo'
