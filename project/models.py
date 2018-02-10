from django.db import models
from user.models import Account


class Project(models.Model):
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    title = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )

    description = models.CharField(
        max_length=8192,
        blank=False,
        null=False
    )

    price = models.IntegerField(
        blank=False,
        null=False
    )

    period = models.IntegerField(
        blank=False,
        null=False
    )

    category = models.IntegerField(
        blank=False,
        null=False
    )

    file = models.FileField(
        upload_to='static/files/project/'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
