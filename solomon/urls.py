"""solomon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)

urlpatterns = [
    path(r'', main),
    path(r'admin/', admin.site.urls),
    path(r'chat/', include('Chat.urls')),
    path(r'contact/', include('Contact.urls')),
    path(r'contract/', include('Contract.urls')),
    path(r'order/', include('Order.urls')),
    path(r'product/', include('Product.urls')),
    path(r'project/', include('Project.urls')),
    path(r'review/', include('Review.urls')),
    path(r'user/', include('User.urls')),
    path(r'favicon.ico', favicon_view),
]
