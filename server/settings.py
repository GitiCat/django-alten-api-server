import os
import json
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'wzc4z3*_p=xbj@mc_!^1^+q3rz343i^qo*4b+3bv8+_$0pp@%@'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tinymce',
    'api_v0.article',
    'api_v0.images',
    'api_v0.vacancies',
    'api_v0.files',
    'api_v0.documents',
    'api_v0.product',
    'api_v0.emails',
    'api_v0.personnel',
    'frontend'
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

ROOT_URLCONF = 'server.urls'
DEFAULT_FILE_STORAGE = 'django_hashedfilenamestorage.storage.HashedFilenameFileSystemStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'frontend', 'templates')
        ],
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

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

TINYMCE_DEFAULT_CONFIG = {
    'language': 'ru',
    'height': 480,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'valid_styles': {
        'div': '', 
        'p': '', 
        'table': '', 
        'tr': '', 
        'td': ''
    },
    'valid_classes': {
        '*': ['left', 'right'],
    },
    'extended_valid_elements': 'table[class],td[class],span[class],img[class, img, width, height, alt]',
    'invalid_elements': 'span',
    'cleanup': True,
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image'
}

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
with open(os.path.join(BASE_DIR, "config", "db_conn.json")) as db_conf_file:
    db_conf = json.load(db_conf_file)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "OPTIONS": {
            "host": db_conf["host"],
            "port": db_conf["port"],
            "db": db_conf["db_name"],
            "user": db_conf["user"]["name"],
            "passwd": db_conf["user"]["password"],
            "charset": "utf8",
            "use_unicode": True
        },
        "CONN_MAX_AGE": db_conf["options"]["TTL"]
    }
}

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

with open(os.path.join(BASE_DIR, 'config', 'email.json')) as email_config_file:
    email_config = json.load(email_config_file)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_USE_SSL = email_config['EMAIL_SSL']
EMAIL_USE_TLS = email_config['EMAIL_TLS']
EMAIL_TIMEOUT = email_config['EMAIL_TIMEOUT']

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_UTF8 = True
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ('assepts', os.path.join(BASE_DIR, 'static', 'assepts'))
]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760
