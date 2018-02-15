from django.urls import path
from .views import *

urlpatterns = [
    path(r'create/', create_order),
]
