"""
Django settings for messages_blog project.

Generated by 'django-admin startproject' using Django 1.10.6.

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
SECRET_KEY = '1)he0oz1($gnt^obp8z!a1-sd(erdk_&wy-i1_%8ve3+!!^nk$'

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

    'comment',
    'mptt'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'messages_blog.middleware.Redirect404Middleware',
    'messages_blog.middleware.RedirectAuthUserFromLoginPage'
]

ROOT_URLCONF = 'messages_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'messages_blog.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

DOMAIN = 'http://127.0.0.1:8000'

VK_CLIENT = ''
VK_SECRET = ''

VK_REDIRECT = 'https://oauth.vk.com/authorize?client_id={client_id}&display=page&' \
              'redirect_uri={domain}/vk_callback&scope=email&' \
              'response_type=code&v=5.56&revoke=1'.format(client_id=VK_CLIENT,
                                                          domain=DOMAIN)
VK_URL = 'https://oauth.vk.com/access_token?client_id={client}&' \
         'client_secret={secret}&' \
         'redirect_uri={domain}/vk_callback&' \
         'code='.format(secret=VK_SECRET, client=VK_CLIENT, domain=DOMAIN)


FACEBOOK_URL = 'https://graph.facebook.com/v2.7/oauth/access_token?client_id={client_id}&' \
               'client_secret={client_secret}&' \
               'redirect_uri={domain}/facebook_callback/&'\
               'code={code}'

FACEBOOK_APP = ''
FACEBOOK_SECRET = ''
FACEBOOK_TOKEN = ''
FACEBOOK_REDIRECT = 'https://www.facebook.com/v2.7/dialog/oauth?' \
                    'client_id={client_id}&redirect_uri={domain}/facebook_callback/'\
    .format(client_id=FACEBOOK_APP, domain=DOMAIN)

GITHUB_CLIENT = ''
GITHUB_SECRET = ''
GITHUB_REDIRECT = 'https://github.com/login/oauth/authorize?scope=user:email&client_id=' + GITHUB_CLIENT
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_URL = 'https://api.github.com/user?'

