# -*- coding:utf-8 -*-
"""
Django settings for xsadmin project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
# -*- coding:utf-8 -*-
import os, datetime
from user import utils as user_utils

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_summernote',
    'rest_framework',
    #'django_celery_beat',
    #'django_celery_results',
    'password_reset',
    'home',
    'user.apps.UserConfig',
    'api.apps.ApiConfig',
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

ROOT_URLCONF = 'xsadmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'xsadmin.wsgi.application'

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
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/upload/'

def uploaded_filepath(instance, filename):
    if instance.rename:
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (user_utils.gen_api_key(), ext)
    today = datetime.datetime.now()
    return os.path.join(str(today.year), str(today.month), filename)

SUMMERNOTE_CONFIG = {
    'attachment_upload_to': uploaded_filepath,
    'attachment_model': 'user.Attachment',
    # Using SummernoteWidget - iframe mode
    'iframe': False,  # or set False to use SummernoteInplaceWidget - no iframe mode
    # Using Summernote Air-mode
    'airMode': False,
    'lang': 'zh-CN',
    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,
    # Set text direction : 'left to right' is default.
    'direction': 'ltr',
    # Customize toolbar buttons
    'width': '72%',
    'height': 500,
    'toolbar': [
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript', 'strikethrough', 'clear']],
        ['fontname', ['fontname']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'hr']],
        ['view', ['fullscreen', 'codeview']],
        ['help', ['help']],
    ],
    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,
    'default_css': (
        '//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css',
        '//cdn.bootcss.com/summernote/0.8.2/summernote.css',
    ),
    'default_js': (
        '//cdn.bootcss.com/jquery/1.12.4/jquery.min.js',
        '//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js',
        '//cdn.bootcss.com/jqueryui/1.10.4/jquery.ui.widget.min.js',
        '//cdn.bootcss.com/jquery.iframe-transport/1.0.1/jquery.iframe-transport.min.js',
        '//cdn.bootcss.com/blueimp-file-upload/9.17.0/js/jquery.fileupload.min.js',
        '//cdn.bootcss.com/summernote/0.8.2/summernote.min.js',
    ),
    'default_css_for_inplace': (
        '//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css',
        '//cdn.bootcss.com/summernote/0.8.2/summernote.css',
        os.path.join(STATIC_URL, 'django_summernote/django_summernote_inplace.css'),
    ),
    'default_js_for_inplace': (
        '//cdn.bootcss.com/jquery/1.12.4/jquery.min.js',
        '//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js',
        '//cdn.bootcss.com/jqueryui/1.10.4/jquery.ui.widget.min.js',
        '//cdn.bootcss.com/jquery.iframe-transport/1.0.1/jquery.iframe-transport.min.js',
        '//cdn.bootcss.com/blueimp-file-upload/9.17.0/js/jquery.fileupload.min.js',
        '//cdn.bootcss.com/summernote/0.8.2/summernote.min.js',
    ),
    'codemirror': {'theme': 'monokai',},
}

#自定义用户模型
AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = (
    'home.authentication.EmailUsernameAuthBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    )
}

CRISPY_TEMPLATE_PACK  =  'bootstrap3'
LOGIN_REDIRECT_URL = '/user/'
LOGIN_URL = '/login/'

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://www.along.party:16379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CELERY_BROKER_TRANSPORT = 'redis'
CELERY_BROKER_URL = 'redis://www.along.party:16379/1'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIME_ZONE = TIME_ZONE
#CELERY_RESULT_BACKEND = 'django-cache'
#CELERY_RESULT_BACKEND = 'django-db'

USER_PORTS_CACHE_TIME = 45

PROJECT_CONFIG = {
    'PROJECT_NAME':'xsadmin',
    'PROJECT_URL':'https://github.com/alishtory/xsadmin',
    'PROJECT_VERSION':'1.0.3',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }, # 针对 DEBUG = True 的情况
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
        }, # 对日志信息进行格式化，每个字段对应了日志格式中的一个字段，更多字段参考官网文档，我认为这些字段比较合适，输出类似于下面的内容
        # INFO 2016-09-03 16:25:20,067 /home/ubuntu/mysite/views.py views.py views get 29: some info...
    },
    'handlers': {
        'console':{
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers' :['console'],
            'level':'DEBUG',
            'propagate': True # 是否继承父类的log信息
        }, # handlers 来自于上面的 handlers 定义的内容
        'xsadminloger': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

#放在底部
from .settings_custom import *



