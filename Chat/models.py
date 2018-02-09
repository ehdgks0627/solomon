from django.db import models
from User.models import Account


class Chat(models.Model):
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    receiver = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)