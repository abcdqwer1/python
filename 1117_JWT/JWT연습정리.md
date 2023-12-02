python -m venv venv 

.\venv\Scripts\activate # window

pip install django

django-admin startproject jwtproject .

python manage.py startapp accounts

# jwtproject > settings.py 
INSTALLED_APPS = [
    'accounts',
]

AUTH_USER_MODEL = 'accounts.CustomUser'