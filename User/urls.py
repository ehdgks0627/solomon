from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path(r'login/', login_view),
    path(r'logout/', logout_view),
    path(r'register/', register_view),
]
