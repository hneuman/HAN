"""
Django settings for han project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

DATABASE_URL = "postgres://jmvpnlqmvcutqs:73L581r4N4-aip6FQPK-q3kYna@ec2-54-225-197-30.compute-1.amazonaws.com:5432/d4n5h8nb8a1rip"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yna648b$h0^qb^b*+_inq*37!t07=e#=-^u5!n7awv9e3-gd99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'han.han_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'han.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'han.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases



#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'han',
#        'USER' : 'django',
#        'PASSWORD' : 'django',
#        'HOST' : 'localhost',
#        'PORT' : '5432',
#
#
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'han',
        'USER' : 'django',
        'PASSWORD' : 'django',
        'HOST' : 'localhost',
        'PORT' : '5432',


    }
}

DATABASES['default'] =  dj_database_url.config("postgres://jmvpnlqmvcutqs:73L581r4N4-aip6FQPK-q3kYna@ec2-54-225-197-30.compute-1.amazonaws.com:5432/d4n5h8nb8a1rip")

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



#STATIC_URL = 'constancia_projecto/constancia_app'
##
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
#)


#print " STATICFILES_DIRS === %s " %STATICFILES_DIRS
#MEDIA_ROOT = os.path.join(BASE_DIR, "/static/media/")
#MEDIA_URL = '/media/'

STATIC_URL = '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR,    MEDIA_URL)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "/static"),
)


STATIC_ROOT = os.path.join(BASE_DIR, '/han_app/static/')
print ">>>>>>>",STATICFILES_DIRS
print ">>>>>>>>>>   ",BASE_DIR


#STATIC_ROOT = '/home/project_name/your_app/static/'    
#STATIC_URL = '/static/'    
#STATICFILES_DIRS =(     
#PROJECT_DIR+'/static',    
##//don.t forget comma    
#)