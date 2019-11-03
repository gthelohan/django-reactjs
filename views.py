import json
import jwt
import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def google_auth(request):
    access_token = json.loads(request.body.decode('utf-8')).get('access_token')
    resp = render(request, 'auth.html')
    encoded_jwt = jwt.encode({'id': access_token}, '724692086964-q4mu9fdsa1qg4teqd9r9rfqoj6rpsdbr.apps.googleusercontent.com')
    resp['x-auth-token'] = encoded_jwt
    print(requests.get('https://openidconnect.googleapis.com/v1/userinfo', params={'access_token': access_token, 'alt': 'json'}).text)
    return resp