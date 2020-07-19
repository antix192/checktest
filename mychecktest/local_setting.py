import os

# settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#6kks)*q@)q-uf2#(+d*bttx3zfz14vw8z#g$ig%%9ork&3y!f'

# settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True  # ローカルでDebugできるようになります
