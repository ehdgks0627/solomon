from django.db import models
from User.models import Account
from Product.models import Product


class Review(models.Model):
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    title = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )

    content = models.CharField(
        max_length=8192,
        blank=False,
        null=False
    )

    star = models.IntegerField(
        blank=False,
        null=False
    )

    tags = models.TextField(
        max_length=256,
        blank=True,
        null=False,
        default='[]'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
