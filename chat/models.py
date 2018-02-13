from django.db import models


class Chat(models.Model):
    owner = models.ForeignKey(
        'user.Account',
        related_name='%(app_label)s_%(class)s_owner',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    receiver = models.ForeignKey(
        'user.Account',
        related_name='%(app_label)s_%(class)s_receiver',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    is_read = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    is_hidden = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
