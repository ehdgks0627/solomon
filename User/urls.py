from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'login/$', login_view),
    url(r'logout/$', logout_view),
]
