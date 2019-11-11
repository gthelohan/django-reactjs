from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

import json
import jwt
import requests

class OAuthBackend:
    def authenticate(self, request):
        access_token = json.loads(request.body.decode('utf-8')).get('access_token')
        encoded_jwt = jwt.encode({'id': access_token}, settings.OAUTH_CONFIG['GOOGLE']['APP_ID'])
        user_data = json.loads(requests.get(settings.OAUTH_CONFIG['GOOGLE']['URL'], params={'access_token': access_token, 'alt': 'json'}).text)
        print(user_data)
        if user_data['name']:
            username = user_data['name']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
