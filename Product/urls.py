from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'get-categories/$', get_categories),
]
