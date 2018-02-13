from django.db import models


class Review(models.Model):
    owner = models.ForeignKey(
        'user.Account',
        related_name='%(app_label)s_%(class)s_owner',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    product = models.ForeignKey(
        'product.Product',
        related_name='%(app_label)s_%(class)s_product',
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
