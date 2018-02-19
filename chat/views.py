from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat
from user.models import Account


@login_required(login_url='/')
def test_view(request, receiver_id):
    receiver = Account.objects.get(id=receiver_id)
    messages = Chat.objects.get_message(owner=request.user, receiver=receiver)
    return render(request, 'chat/test.html', {'messages': messages, 'receiver_id': receiver_id})
