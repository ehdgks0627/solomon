from django.db import models
from User.models import Account
from Order.models import Order

class Contact(models.Model):
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    title = models.CharField(
        verbose_name='title',
        max_length=100,
        unique=True,
        default=''
    )

    content = models.CharField(
        verbose_name='main',
        max_length=1000,
        unique=True,
        default=''
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to='static/file/contact/'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)