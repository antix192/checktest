from django.core.management.utils import get_random_secret_key
generate_secretkey_setting.py


secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text)
