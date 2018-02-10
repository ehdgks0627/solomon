from django.urls import path
from .views import *

urlpatterns = [
    path(r'detail/<int:category>/', detail_contract),
    path(r'edit/<int:contract_id>/', edit_contract),
    path(r'form/<int:contract_id>/', form_contract),
]
