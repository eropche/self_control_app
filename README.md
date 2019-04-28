Install

```
pip install django-bootstrap4
pip install django-summernote
pip install django-user-accounts
```


Add to settings.py

```
INSTALLED_APPS = [
    ...
    'bootstrap4',
    'django_summernote',
    'django.contrib.sites',
    'account',
    'notes',
]

...


MIDDLEWARE = [
    ...

    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware'
]

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
                'account.context_processors.account'
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'postgres_name',
        'PASSWORD': 'postgres_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = [
    'account.auth_backends.EmailAuthenticationBackend',
]

# mail

EMAIL_USE_SSL = True
EMAIL_HOST = 'stmp'
DEFAULT_FROM_EMAIL = 'email'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'email_password'
EMAIL_PORT = port


ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

ACCOUNT_LOGIN_URL = 'account_login'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = ACCOUNT_LOGIN_URL
ACCOUNT_PASSWORD_RESET_REDIRECT_URL = ACCOUNT_LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_URL = "account_confirm_email"
ACCOUNT_SETTINGS_REDIRECT_URL = 'account_settings'
ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "account_password"



SUMMERNOTE_THEME = 'bs4'

```
add site
```
python manage.py shell
>>> from django.contrib.sites.models import Site
>>> site = Site(domain='localhost:8000', name='localhost:8000')
>>> site.save()
>>> site.id
2
```

SITE_ID = 2 to settings.py