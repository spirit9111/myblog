"""
Django settings for MyBlog project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ya&%m2@8952qgk#==5n3(jflwcnq4vg*-%%p$m@5@tf6#dxkb'

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
	# apps
	'mdeditor',  # markdown
	'blog.apps.BlogConfig',
	'user.apps.UserConfig',
	'comment.apps.CommentConfig',
	'other.apps.OtherConfig',
	# 'captcha'
	'haystack.apps.HaystackConfig',  # 搜索
	# xadmin
	'xadmin',
	'crispy_forms',
	'reversion',
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

ROOT_URLCONF = 'MyBlog.urls'

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

WSGI_APPLICATION = 'MyBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'myblog',
		'HOST': '127.0.0.1',
		'USER': 'root',
		'PASSWORD': 'w92z12x14',
		'PORT': '3306',
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

# MEDIA_ROOT
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
MEDIA_URL = '/static/images/'

# redis
CACHES = {
	"default": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": "redis://127.0.0.1:6379/0",
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		}
	},
	"sms_code": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": "redis://127.0.0.1:6379/1",
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		}
	},
	"session": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": "redis://127.0.0.1:6379/2",
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		}
	}
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

AUTH_USER_MODEL = "user.User"  # 用户认证

# 搜索配置
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'blog.whoosh_cn_backends.WhooshEngine',
		'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
	},
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# logging日志
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
	'formatters': {  # 日志信息显示的格式
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
		},
	},
	'filters': {  # 对日志进行过滤
		'require_debug_true': {  # django在debug模式下才输出日志
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'handlers': {  # 日志处理方法
		'console': {  # 向终端中输出日志
			'level': 'DEBUG',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
		'file': {  # 向文件中输出日志
			'level': 'INFO',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(BASE_DIR, "logs/MyBlog.log"),  # 日志文件的位置
			'maxBytes': 300 * 1024 * 1024,
			'backupCount': 10,
			'formatter': 'verbose'
		},
	},
	'loggers': {  # 日志器
		'django': {  # 定义了一个名为django的日志器
			'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
			'propagate': True,  # 是否继续传递日志信息
			'level': 'DEBUG',  # 日志器接收的最低日志级别
			# 'level': 'ERROR',  # 日志器接收的最低日志级别
		},
	}
}
