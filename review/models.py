from django.db import models
import ujson


class ReviewManager(models.Manager):
    def create_review(self, tags=None, **kwargs):
        order = self.model(**kwargs)
        if tags:
            order.tags = tags
        order.save()
        return order


class Review(models.Model):
    owner = models.ForeignKey(
        'user.Account',
        related_name='%(app_label)s_%(class)s_owner',
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

    _tags = models.TextField(
        blank=False,
        null=False,
        default='[]'
    )

    @property
    def tags(self):
        return ujson.loads(self._tags)

    @tags.setter
    def tags(self, value):
        self._tags = ujson.dumps(value)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
