from django.urls import path
from .views import *

urlpatterns = [
    path(r'', get_project),
    path(r'create/', create_project),
    path(r'delete/<int:id>/', delete_project),
    path(r'detail/<int:id>/', detail_project),
    path(r'edit/<int:id>/', edit_project),
]
