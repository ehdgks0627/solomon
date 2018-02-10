from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView


urlpatterns = [
    path('test/', test_view),
]
