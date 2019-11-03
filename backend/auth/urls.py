from django.conf.urls import url

from . import views

urlpatterns = [
    url('oauth', views.oauth, name='oauth'),
]
