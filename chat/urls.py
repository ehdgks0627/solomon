from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView


urlpatterns = [
    path('<str:receiver_id>/', test_view),
]
