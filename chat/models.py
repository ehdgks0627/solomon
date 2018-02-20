from django.db import models


class ChatManager(models.Manager):
    def get_message(self, owner, receiver):
        messages = list(self.filter(owner=owner, receiver=receiver)) + \
                   list(self.filter(owner=receiver, receiver=owner))

        messages = sorted(messages, key=lambda item: item.created_at)
        return messages


class Chat(models.Model):
    objects = ChatManager()
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

    message = models.TextField(
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
