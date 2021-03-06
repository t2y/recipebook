# coding: utf-8
# Django settings for recipebook project.
import os
BASE_PATH = os.path.abspath(os.path.split(__file__)[0])

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#    ('username', 'mailaddress'),
)

MANAGERS = ADMINS

# Settings for database.
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'data.sqlite'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

CACHE_BACKEND = 'dummy:///'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Tokyo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ja'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: '/home/media/media.lawrence.com/'
MEDIA_ROOT = '%s/site_media/' % BASE_PATH

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: 'http://media.lawrence.com', 'http://example.com/media/'
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: 'http://foo.com/media/', '/media/'.
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'YOUR_SECRET_KEY'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'recipebook.maricilib.django.core.context_processors.csrf',
    'recipebook.maricilib.django.core.context_processors.current_site',
    'recipebook.maricilib.django.core.context_processors.settings',
    'recipebook.recipes.context_processors.side1',
    'recipebook.maricilib.django.apps.feedback.context_processors.form',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'recipebook.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.formtools',
    'django.contrib.humanize',
    'recipebook.maricilib.django.apps.sitenews',
    'recipebook.maricilib.django.apps.documents',
    'recipebook.maricilib.django.apps.search',
    'recipebook.maricilib.django.apps.daily',
    'recipebook.maricilib.django.apps.taskqueue',
    'recipebook.maricilib.django.apps.feedback',
    'recipebook.recipes',
)

LOGIN_REDIRECT_URL = '/home/'

AUTH_PROFILE_MODULE = 'recipes.UserProfile'

COPYRIGHT = u'&copy; 2009 recipebook.jp'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_FROM = ''
EMAIL_USE_TLS = False

# Settings for Amazon S3.
USE_AWS = False
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_HOST = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_IS_SECURE = True

# Settings for taskqueue.
QUEUE_BACKEND = 'immediate' # immediate or activemq
QUEUE_HOST = 'localhost'
QUEUE_PORT = 61613
QUEUE_USER = ''
QUEUE_PASSWORD = ''
QUEUENAME_EMAIL = 'recipebook.email'
QUEUENAME_SENDS3 = 'recipebook.s3'
QUEUENAME_RECIPE = 'recipebook.recipe'
TASKQUEUE_USE_SIGNAL = True

# Settings for search.
SEARCH_USE_SOLR = False
SEARCH_INDEXER_URL = 'http://localhost:8983/solr'
SEARCH_SEARCHER_URL = 'http://localhost:8983/solr'

FEEDBACK_SENDMAIL = False
FEEDBACK_SENDMAIL_FROM = ''
FEEDBACK_SENDMAIL_TO = (
#    'mailaddress',
)
