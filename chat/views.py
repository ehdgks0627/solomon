from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def test_view(request):
    return render(request, 'chat/test.html')
