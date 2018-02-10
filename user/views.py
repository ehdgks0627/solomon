from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from .models import Account


@require_http_methods(['POST'])
def login_view(request):
    user = authenticate(username=request.POST.get('uid'), password=request.POST.get('upw'))
    if user is not None:
        login(request, user)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        # TODO login error
        return redirect(request.META.get('HTTP_REFERER', '/'))


@require_http_methods(['GET'])
def logout_view(request):
    logout(request=request)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_http_methods(['POST'])
def register_view(request):
    try:
        user = Account.objects.create_user(
            id=request.POST.get('uid'),
            password=request.POST.get('upw'),
            email=request.POST.get('uemail'),
            name=request.POST.get('uname'),
            nickname=request.POST.get('unickname'),
            phone=request.POST.get('uphone')
        )
    except IntegrityError:
        user = None
    if user is not None:
        login(request, user)
        # TODO register success
        return redirect('/')
    else:
        # TODO register error
        return redirect('/')
