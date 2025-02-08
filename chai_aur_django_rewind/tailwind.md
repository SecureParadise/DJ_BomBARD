pip install django-tailwind

pip install 'django-tailwind[reload]'

python -m ensurepip --upgrade

python -m pip install --upgrade pip

<!-- In settings.py update tailwind  -->

INSTALLED_APPS = [
    'tailwind'
]

python manage.py tailwind init

you will get theme app

INSTALLED_APPS = [
    'tailwind',
    'theme'
]

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']

<code>
PS C:\Users\ankit> node -v
v23.6.0
PS C:\Users\ankit> npm -v
10.9.2
PS C:\Users\ankit> where npm
PS C:\Users\ankit> cmd
Microsoft Windows [Version 10.0.26100.2894]
(c) Microsoft Corporation. All rights reserved.

C:\Users\ankit>where npm
C:\Program Files\nodejs\npm
C:\Program Files\nodejs\npm.cmd

C:\Users\ankit>
</code>

### C:\Program Files\nodejs\npm.cmd

is the needed one

## Set NPM path

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

## Install Tailwind

python manage.py tailwind install

now run two terminal

1) for runserver
python manage.py runserver
2) for tailwind
python manage.py tailwind start

<!-- for production -->
python manage.py tailwind build
