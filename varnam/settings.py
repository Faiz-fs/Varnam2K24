

    OpenToAllCTF
    /
    OTA-University

Code
Issues 16
Pull requests 7
Actions
Projects
Security

    Insights

The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting. #9
Closed
Corb3nik opened this issue Jan 25, 2018 · 3 comments
Comments
@Corb3nik
Collaborator
Corb3nik commented Jan 25, 2018

When running the command python3 manage.py runserver, I get the following message :

$ python3 manage.py runserver
Performing system checks...

Unhandled exception in thread started by <function check_errors.<locals>.wrapper at 0x1112599d8>
Traceback (most recent call last):
  File "/Users/Corb3nik/.pyenv/versions/3.6.0/lib/python3.6/site-packages/django/utils/autoreload.py", line 225, in wrapper
    fn(*args, **kwargs)
  File "/Users/Corb3nik/.pyenv/versions/3.6.0/lib/python3.6/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/Corb3nik/.pyenv/versions/3.6.0/lib/python3.6/site-packages/django/core/management/base.py", line 410, in check
    raise SystemCheckError(msg)
django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:

ERRORS:
?: (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.

System check identified 1 issue (0 silenced).

@Corb3nik Corb3nik added the bug label Jan 25, 2018
@reznok reznok closed this as completed in ff7684c Jan 26, 2018
reznok added a commit that referenced this issue Jan 26, 2018
@reznok
Merge pull request #11 from OpenToAllCTF/corb-9-static-root-bug
fd6c245
@sergiocampos
sergiocampos commented Jun 15, 2020

I only alter STATIC_ROOT = os.path.join(BASE_DIR, 'static') to STATIC_ROOT = '/static/'
@rezacloner1372
rezacloner1372 commented Sep 10, 2022 •

You have to enter complete path of static directory:
STATIC_ROOT = '/home/reza/blog/static/'

Or If you want to use Collects the static files into STATIC_ROOT by django-admin collectstatic command you have to use :

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
@sousa2323
sousa2323 commented Oct 22, 2023

    Eu apenas altero STATIC_ROOT = os.path.join(BASE_DIR, 'static') para STATIC_ROOT = '/static/'

I used
@Faiz-fs
Add a comment
Comment

Add your comment here...
Remember, contributions to this repository should follow our GitHub Community Guidelines.
Assignees
No one assigned
Labels
bug
Projects
None yet
Milestone
No milestone
Development

No branches or pull requests
"""
Django settings for varnam project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

    OpenToAllCTF
    /
    OTA-University

Code
Issues 16
Pull requests 7
Actions
Projects
Security

    Insights

The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting. #9
Closed
Corb3nik opened this issue Jan 25, 2018 · 3 comments
Comments
@Corb3nik
Collaborator
Corb3nik commented Jan 25, 2018

When running the command python3 manage.py runserver, I get the following message :

$ python3 manage.py runserver
Performing system checks...

Unhandled exception in thread started by <function check_errors.<locals>.wrapper at 0x1112599d8>
Traceback (most recent call last):
  File "/Users/Corb3nik/.pyenv/versions/3.6.0/lib/python3.6/site-packages/django/utils/autoreload.py", line 225, in wrapper
    fn(*args, **kwargs)
  File "/Users/Corb3nik/.pyenv/versions/3.6.0/lib/python3.6/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Users/Corb3nik/.pyenv/versions/3.6.0/lib/python3.6/site-packages/django/core/management/base.py", line 410, in check
    raise SystemCheckError(msg)
django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:

ERRORS:
?: (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.

System check identified 1 issue (0 silenced).

@Corb3nik Corb3nik added the bug label Jan 25, 2018
@reznok reznok closed this as completed in ff7684c Jan 26, 2018
reznok added a commit that referenced this issue Jan 26, 2018
@reznok
Merge pull request #11 from OpenToAllCTF/corb-9-static-root-bug
fd6c245
@sergiocampos
sergiocampos commented Jun 15, 2020

I only alter STATIC_ROOT = os.path.join(BASE_DIR, 'static') to STATIC_ROOT = '/static/'
@rezacloner1372
rezacloner1372 commented Sep 10, 2022 •

You have to enter complete path of static directory:
STATIC_ROOT = '/home/reza/blog/static/'

Or If you want to use Collects the static files into STATIC_ROOT by django-admin collectstatic command you have to use :

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
@sousa2323
sousa2323 commented Oct 22, 2023

    Eu apenas altero STATIC_ROOT = os.path.join(BASE_DIR, 'static') para STATIC_ROOT = '/static/'

I used
@Faiz-fs
Add a comment
Comment

Add your comment here...
Remember, contributions to this repository should follow our GitHub Community Guidelines.
Assignees
No one assigned
Labels
bug
Projects
None yet
Milestone
No milestone
Development

No branches or pull requests



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6bmq6c*%dk)32m35i@lp3bj#$^)ea)$f8#*8q0q8xeid3bplxe"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "event",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "varnam.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "varnam.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres.xhxlshqfnpahspghxyxy",
        "PASSWORD": "Moh@Faiz543",
        "HOST": "aws-0-ap-south-1.pooler.supabase.com",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS=[BASE_DIR/"static"]
STATIC_ROOT=BASE_DIR/"staticfiles"

# Default primary key field type
# https://docs    'whitenoise.middleware.WhiteNoiseMiddleware',.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
