from django.db import models


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    REQUIRED_FIELDS = ['title', 'description', 'price', 'period']
