from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'', main),
    path(r'admin/', admin.site.urls),
    path(r'chat/', include('chat.urls')),
    path(r'contact/', include('contact.urls')),
    path(r'contract/', include('contract.urls')),
    path(r'order/', include('order.urls')),
    path(r'product/', include('product.urls')),
    path(r'project/', include('project.urls')),
    path(r'review/', include('review.urls')),
    path(r'user/', include('user.urls')),
    path(r'favicon.ico', favicon_view),
]
