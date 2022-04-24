import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'django-insecure-taljbe&lunc(pa5%+%!t7yokj%yk0(_iy%*p5k-gf82k*fen3o'

DEBUG = True #ローカルでDebugできるようになります