"""
Django settings for project src.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(BASE_DIR,'app')
API_DIR = os.path.join(BASE_DIR,'api')
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')
STATIC_PATH = os.path.join(APP_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wmf(fc)l3jitafjt1^ys8x@&2@++p589vfg++1(@_+^=rqfqft'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'api',
    'rest_framework',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['app/templates'], # to enable registration templates overriding
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
	STATIC_PATH,
]

# Media files (Downloadable files)

MEDIA_ROOT = os.path.join(APP_DIR,'media')
MEDIA_URL = '/media/'

# Rest API framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

# Absolute Path for tool.jar
# The online tool uses spdx-tools-2.1.6-SNAPSHOT-jar-with-dependencies.jar from the compiled target folder of java tools
# renamed (for now) as tool.jar in the main src directory of spdx-online tool

JAR_ABSOLUTE_PATH =  os.path.abspath(".")+"/tool.jar"
# URL Path Variables

LOGIN_REDIRECT_URL = "/app/"
REGISTER_REDIRECT_UTL = "/app/login/"
LOGIN_URL = "/app/login/"
HOME_URL="/app/"

# Online tool usage without login
ANONYMOUS_LOGIN_ENABLED = True

# Password reset link expiration limit (in days)
PASSWORD_RESET_TIMEOUT_DAYS = 3

# this will output emails in the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# change to EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# after configuring the smtp correctly

# EMAIL_HOST = 'smtp.<smtp provider>.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'email@<smtp provider>.com'
# EMAIL_HOST_PASSWORD = 'password'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'SPDX Team <noreply@spdx.com>'
