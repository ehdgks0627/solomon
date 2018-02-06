from django.urls import path
from .views import *

urlpatterns = [
    path(r'', get_product),
    path(r'<int:category>/', get_product),
    path(r'add/', add_product),
    path(r'categories/', get_categories),
    path(r'delete/<int:id>/', delete_product),
    path(r'detail/<int:id>/', detail_product),
    path(r'edit/<int:id>/', edit_product),
]
