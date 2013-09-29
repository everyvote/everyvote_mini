# Django settings for everyvote_mini project.

# Adding cwd to config for development purposes.
# Perhaps this should eventually break out into a settings.devel.py
# or something of the like.
import os
cwd = os.getcwd();

# Set to false for non-development instances.
DEBUG = True

ADMINS = (
    ('Everyvote-Admin', 'admin@example.com'),
)

# This needs to be annotated.
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(cwd, 'everyvote_mini/storage.db'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# This needs to be annotated.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(cwd, 'static/uploaded_files/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static/uploaded_files/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(cwd, 'static/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ()


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(fz)$w6=306q_-ja+6$6t_dk%%epq2k&-6v4929gzp*wfw8te2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'everyvote_mini.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'everyvote_mini.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(cwd, 'templates'),
    os.path.join(cwd, 'everyvote_mini/templates'),
    os.path.join(cwd, 'everyvote_mini/templates/about'),
    os.path.join(cwd, 'everyvote_mini/templates/candidates'),
    os.path.join(cwd, 'everyvote_mini/templates/constituencies'),
    os.path.join(cwd, 'everyvote_mini/templates/contact'),
    os.path.join(cwd, 'everyvote_mini/templates/elections'),
    os.path.join(cwd, 'everyvote_mini/templates/offices'),
    os.path.join(cwd, 'everyvote_mini/templates/parent_constituencies'),
    os.path.join(cwd, 'everyvote_mini/templates/registration'),
    os.path.join(cwd, 'everyvote_mini/templates/users'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',
    'everyvote_mini',
    'registration',
    'captcha',
)

# These need to be annotated.
RECAPTCHA_PUBLIC_KEY='6Ld9tOYSAAAAAO18CkzrO2jTp3RPQIIgPplU6UxY'

RECAPTCHA_PRIVATE_KEY='6Ld9tOYSAAAAAHB4QJly625VuFG5GRsFY32AEijW'

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window



LOGIN_URL='/accounts/login/'
LOGIN_REDIRECT_URL='/'
LOGOUT_URL='/accounts/logout/'



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# provide our get_profile()
AUTH_PROFILE_MODULE = 'everyvote_mini.UserProfile'

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages")


# These need to be annotated.
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'registration@everyvote.org'
EMAIL_HOST_PASSWORD = 'i;Fi,-4+Hf"<Nhy'
EMAIL_PORT = 587
EMAIL_USE_TLS = True