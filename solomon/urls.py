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
from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include('Contact.urls')),
    url(r'^contract/', include('Contract.urls')),
    url(r'^order/', include('Order.urls')),
    url(r'^product/', include('Product.urls')),
    url(r'^project/', include('Project.urls')),
    url(r'^review/', include('Review.urls')),
    url(r'^user/', include('User.urls')),
    url(r'^$', main),
    url('^account/', include('django.contrib.auth.urls')),
]
