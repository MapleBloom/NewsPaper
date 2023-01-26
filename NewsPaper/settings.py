"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
env_path = Path('./NewsPaper/venv')/'settings.env'
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',

    'news.apps.NewsConfig',
    'accounts',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

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
                'news.context_processors.navbarcreateperm.count_post_create',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

LOGIN_REDIRECT_URL = "/posts"
LOGIN_URL = "/simpleaccounts/login"
LOGOUT_REDIRECT_URL = "/simpleaccounts/login"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMINS = [('admin', os.getenv('EMAIL_HOST_EMAIL'))]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'   # 'mandatory', 'optional', 'none'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}
SOCIALACCOUNT_ADAPTER = "accounts.forms.CustomSocialAccountAdapter"

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
EMAIL_HOST_EMAIL = os.getenv('EMAIL_HOST_EMAIL')
DEFAULT_FROM_EMAIL = f'News Portal <{EMAIL_HOST_EMAIL}>'
SERVER_EMAIL = f'News Portal <{EMAIL_HOST_EMAIL}>'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{asctime} | {levelname} | {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'simple_add_warning': {
            'format': '{asctime} | {levelname} | {message} |\n{pathname}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'simple_add_error': {
            'format': '{asctime} | {levelname} | {message} |\n{pathname} |\n{exc_info}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'general': {
            'format': '{asctime} | {levelname} | {module} | {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'filter_warning_level': {
            '()': 'log.log_middleware.FilterLevels',
            'filter_levels': ['WARNING']
        },
        'filter_error_level': {
            '()': 'log.log_middleware.FilterLevels',
            'filter_levels': ['ERROR', 'CRITICAL']
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true', 'filter_warning_level'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_add_warning'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true', 'filter_error_level'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_add_error'
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': './log/general.log',
            'formatter': 'general'
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './log/errors.log',
            'formatter': 'simple_add_error'
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './log/security.log',
            'formatter': 'general'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple_add_warning'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'mail_admins', ],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins', ],
            'level': 'INFO',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors', ],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['errors', ],
            'level': 'INFO',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security', ],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
