from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
def login_view(request):
    user = authenticate(username=request.POST.get('uid'), password=request.POST.get('upw'))
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        # TODO login error
        return redirect('/')


@require_http_methods(['GET'])
def logout_view(request):
    logout(request=request)
    return redirect('/')
