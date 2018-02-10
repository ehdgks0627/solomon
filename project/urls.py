from django.urls import path
from .views import *

urlpatterns = [
    path(r'', get_project),
    path(r'<int:category>/', get_project),
    path(r'create/', create_project),
    path(r'delete/<int:project_id>/', delete_project),
    path(r'detail/<int:project_id>/', detail_project),
    path(r'edit/<int:id>/', edit_project),
    path(r'own/', own_project),
]
