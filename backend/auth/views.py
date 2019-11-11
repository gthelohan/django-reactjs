# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def oauth(request):
    user = authenticate(request)
    if user is not None:
        login(request, user)
        return HttpResponse("ok")
    else:
        return HttpResponse("veuillez vous identifier")

