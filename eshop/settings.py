"""
Django settings for eshop project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'me$dd!2zgs2(-skx6n08g4e7m)-*$#d-uhu5d0_kog%5i=k4yh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'sausage',
    'members',
    # the third party app
    'social_django',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eshop.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'eshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# #    '/var/www/static/',
# ]

STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]


# LOGIN_REDIRECT_URL = 'sausage-list'


AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend'
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',
    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    # 'social_core.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social_core.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social_core.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social_core.pipeline.disconnect.disconnect',
)

SOCIAL_AUTH_FACEBOOK_KEY = '956577584443991'
SOCIAL_AUTH_FACEBOOK_SECRET = '24fe36d97a74e2b7afa3e1a13b9ab879'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'zh_TW',
  'fields': 'id, name, email, age_range'
}

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/sausage'


#####

AWS_ACCESS_KEY_ID = "AKIAIIN46DGE3XBJITDA"
AWS_SECRET_ACCESS_KEY = "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"


AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'eshop.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'eshop.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'sdlfkorg-for-eshop'
# S3DIRECT_REGION = 'us-west-2'
# S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_ROOT = MEDIA_URL
# STATIC_URL = S3_URL + 'static/'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'




AWS_S3_HOST = 's3-ap-northeast-1.amazonaws.com'

S3DIRECT_REGION = 'ap-northeast-1' # your region here

S3_URL = '//s3-ap-northeast-1.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = S3_URL + 'media/'

MEDIA_ROOT = MEDIA_URL

STATIC_URL = S3_URL + 'static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'







import datetime

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}




#####


# the following code are set for heroku deployment
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
import dj_database_url
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass




