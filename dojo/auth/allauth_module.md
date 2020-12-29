`pip install django-allauth`
<br />settings.py append this to settings.py:
```python
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
```
 append this to settings.INSTALLED_APPS and define SITE_ID:
 ```python
    INSTALLED_APPS = ['django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',]
SITE_ID = 1
```
append this to main urls.py:
```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

finally migrate:
`python manage.py migrate`